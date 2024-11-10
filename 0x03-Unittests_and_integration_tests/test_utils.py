#!/usr/bin/env python3
"""Unit tests for the utils module functions: access_nested_map, get_json, and memoize.
   Each function is tested for expected behavior and error handling.
"""

import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map function in utils module.
    
    This function retrieves values from a nested dictionary using a given path.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """
        Tests that access_nested_map returns the correct value given a path.

        Args:
            nested_map (Dict): The nested dictionary to search.
            path (Tuple[str]): Sequence of keys representing the path.
            expected (Union[Dict, int]): Expected output based on the given path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """
        Tests that access_nested_map raises a KeyError for invalid paths.

        Args:
            nested_map (Dict): The nested dictionary to search.
            path (Tuple[str]): Sequence of keys representing the path.
            exception (Exception): Expected exception for invalid paths.
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test cases for get_json function in utils module.
    
    This function fetches JSON data from a given URL and returns it.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """
        Tests that get_json fetches data from a URL and returns the correct JSON payload.

        Args:
            test_url (str): The URL to fetch JSON data from.
            test_payload (Dict): The expected payload to be returned by the mock request.
        """
        # Mock the requests.get method to return the test payload as a JSON response
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test cases for memoize decorator in utils module.
    
    This decorator caches the output of a method and returns the cached result on subsequent calls.
    """

    def test_memoize(self) -> None:
        """
        Tests that memoize caches a method's output and does not re-call the method on subsequent access.
        """
        class TestClass:
            """Example class to test the memoize decorator."""
            def a_method(self):
                """Method that returns a constant value, representing a calculation or retrieval."""
                return 42

            @memoize
            def a_property(self):
                """Method decorated with memoize, which caches its return value after the first call."""
                return self.a_method()
                
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            # Call a_property twice and verify that a_method is only called once due to caching
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()  # Ensure a_method is called only once
