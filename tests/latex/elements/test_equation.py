# File: test_equation.py
# Description: Test cases for equation math delimiter modernization using fixtures
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import pytest

from latex_parser.latex.elements.equation import Equation
from tests.latex.fixtures.equation_test_cases import (
    EQUATION_MODERNIZE_BASIC_TESTS,
    EQUATION_MODERNIZE_MULTIPLE_TESTS,
    EQUATION_MODERNIZE_COMPLEX_TESTS,
    EQUATION_MODERNIZE_EDGE_TESTS
)


class TestEquationModernizeDelimiters:
    """Test the modernize_math_delimiters functionality using fixtures."""
    
    @pytest.mark.parametrize("test_case", EQUATION_MODERNIZE_BASIC_TESTS)
    def test_basic_replacements(self, test_case):
        """Test basic math delimiter replacements."""
        content = test_case["input"]
        expected = test_case["expected"]
        result = Equation.modernize_math_delimiters(content)
        assert result == expected, f"Failed for test case: {test_case['id']} - {test_case['description']}"
    
    @pytest.mark.parametrize("test_case", EQUATION_MODERNIZE_MULTIPLE_TESTS)
    def test_multiple_delimiters(self, test_case):
        """Test multiple math delimiter replacements."""
        content = test_case["input"]
        expected = test_case["expected"]
        result = Equation.modernize_math_delimiters(content)
        assert result == expected, f"Failed for test case: {test_case['id']} - {test_case['description']}"
    
    @pytest.mark.parametrize("test_case", EQUATION_MODERNIZE_COMPLEX_TESTS)
    def test_complex_content(self, test_case):
        """Test complex content with nested LaTeX commands."""
        content = test_case["input"]
        expected = test_case["expected"]
        result = Equation.modernize_math_delimiters(content)
        assert result == expected, f"Failed for test case: {test_case['id']} - {test_case['description']}"
    
    @pytest.mark.parametrize("test_case", EQUATION_MODERNIZE_EDGE_TESTS)
    def test_edge_cases(self, test_case):
        """Test edge cases and error conditions."""
        content = test_case["input"]
        expected = test_case["expected"]
        result = Equation.modernize_math_delimiters(content)
        assert result == expected, f"Failed for test case: {test_case['id']} - {test_case['description']}"