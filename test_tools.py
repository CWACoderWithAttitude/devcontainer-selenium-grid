from selenium_tools.tools import sabitize_string
import pytest


def test_no_substitution_needed():
    input = "abcdef"
    assert sabitize_string(input) == input


def test_replace_single_space_with_underscore():
    input = "abc def"
    expected_output = "abc_def"
    assert sabitize_string(input) == expected_output


def test_replace_single_dot_with_underscore():
    input = "abc.def"
    expected_output = "abc_def"
    assert sabitize_string(input) == expected_output


def test_replace_dot_space_dot_with_underscore():
    input = "abc. .def"
    expected_output = "abc___def"
    assert sabitize_string(input) == expected_output
