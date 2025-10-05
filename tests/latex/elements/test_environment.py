# File: test_environment.py
# Description: Unit tests for Environment class methods using fixture-based testing
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import os
import sys
import pytest

from latex_parser.latex.elements.environment import Environment
from latex_parser.latex.elements.command import Command


def load_test_cases():
    """Load test cases from external fixtures."""
    from latex.fixtures.environment_test_cases import (
        FIND_ALL_BEGIN_ENVIRONMENTS_BASIC_TESTS,
        FIND_ALL_BEGIN_ENVIRONMENTS_WHITESPACE_TESTS,
        FIND_ALL_BEGIN_ENVIRONMENTS_EDGE_CASE_TESTS,
        FIND_ALL_BEGIN_ENVIRONMENTS_STAR_TESTS,
        FIND_ALL_END_ENVIRONMENTS_BASIC_TESTS,
        FIND_ALL_END_ENVIRONMENTS_STAR_TESTS,
        FIND_BEGIN_ENVIRONMENT_BASIC_TESTS,
        FIND_BEGIN_ENVIRONMENT_WHITESPACE_TESTS,
        FIND_BEGIN_ENVIRONMENT_EDGE_CASE_TESTS,
        FIND_BEGIN_ENVIRONMENT_STAR_TESTS,
        FIND_END_ENVIRONMENT_BASIC_TESTS,
        FIND_END_ENVIRONMENT_WHITESPACE_TESTS,
        FIND_END_ENVIRONMENT_STAR_TESTS,
        INTEGRATION_TESTS,
        INVALID_INPUT_TESTS
    )
    from latex.fixtures.environment_parse_arguments_test_cases import (
        PARSE_ENVIRONMENT_ARGUMENTS_BASIC_TESTS,
        PARSE_ENVIRONMENT_ARGUMENTS_WHITESPACE_TESTS,
        PARSE_ENVIRONMENT_ARGUMENTS_OPTIONAL_TESTS,
        PARSE_ENVIRONMENT_ARGUMENTS_EDGE_CASE_TESTS,
        PARSE_ENVIRONMENT_ARGUMENTS_NESTED_TESTS,
        PARSE_ENVIRONMENT_ARGUMENTS_COMPLEX_TESTS,
        PARSE_ENVIRONMENT_ARGUMENTS_ERROR_HANDLING_TESTS,
        PARSE_ENVIRONMENT_ARGUMENTS_EDGE_COVERAGE_TESTS,
        PARSE_ENVIRONMENT_ARGUMENTS_STAR_TESTS,
        PARSE_ENVIRONMENT_ARGUMENTS_MULTIPLE_REQUIRED_TESTS,
        PARSE_ENVIRONMENT_ARGUMENTS_ERROR_COVERAGE_TESTS
    )
    
    return {
        'find_all_begin_basic': FIND_ALL_BEGIN_ENVIRONMENTS_BASIC_TESTS,
        'find_all_begin_whitespace': FIND_ALL_BEGIN_ENVIRONMENTS_WHITESPACE_TESTS,
        'find_all_begin_edge_case': FIND_ALL_BEGIN_ENVIRONMENTS_EDGE_CASE_TESTS,
        'find_all_begin_star': FIND_ALL_BEGIN_ENVIRONMENTS_STAR_TESTS,
        'find_all_end_basic': FIND_ALL_END_ENVIRONMENTS_BASIC_TESTS,
        'find_all_end_star': FIND_ALL_END_ENVIRONMENTS_STAR_TESTS,
        'find_begin_basic': FIND_BEGIN_ENVIRONMENT_BASIC_TESTS,
        'find_begin_whitespace': FIND_BEGIN_ENVIRONMENT_WHITESPACE_TESTS,
        'find_begin_edge_case': FIND_BEGIN_ENVIRONMENT_EDGE_CASE_TESTS,
        'find_begin_star': FIND_BEGIN_ENVIRONMENT_STAR_TESTS,
        'find_end_basic': FIND_END_ENVIRONMENT_BASIC_TESTS,
        'find_end_whitespace': FIND_END_ENVIRONMENT_WHITESPACE_TESTS,
        'find_end_star': FIND_END_ENVIRONMENT_STAR_TESTS,
        'integration': INTEGRATION_TESTS,
        'invalid_input': INVALID_INPUT_TESTS,
        'parse_args_basic': PARSE_ENVIRONMENT_ARGUMENTS_BASIC_TESTS,
        'parse_args_whitespace': PARSE_ENVIRONMENT_ARGUMENTS_WHITESPACE_TESTS,
        'parse_args_optional': PARSE_ENVIRONMENT_ARGUMENTS_OPTIONAL_TESTS,
        'parse_args_edge_case': PARSE_ENVIRONMENT_ARGUMENTS_EDGE_CASE_TESTS,
        'parse_args_nested': PARSE_ENVIRONMENT_ARGUMENTS_NESTED_TESTS,
        'parse_args_complex': PARSE_ENVIRONMENT_ARGUMENTS_COMPLEX_TESTS,
        'parse_args_error_handling': PARSE_ENVIRONMENT_ARGUMENTS_ERROR_HANDLING_TESTS,
        'parse_args_edge_coverage': PARSE_ENVIRONMENT_ARGUMENTS_EDGE_COVERAGE_TESTS,
        'parse_args_star': PARSE_ENVIRONMENT_ARGUMENTS_STAR_TESTS,
        'parse_args_multiple_required': PARSE_ENVIRONMENT_ARGUMENTS_MULTIPLE_REQUIRED_TESTS,
        'parse_args_error_coverage': PARSE_ENVIRONMENT_ARGUMENTS_ERROR_COVERAGE_TESTS
    }


class TestEnvironment:
    """Test the Environment class methods using fixture-based test cases."""

    @pytest.mark.parametrize("test_case", load_test_cases()['find_all_begin_basic'])
    def test_find_all_begin_environments_basic(self, test_case):
        """Test find_all_begin_environments with basic test cases."""
        result = Environment.find_all_begin_environments(test_case['content'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['find_all_begin_whitespace'])
    def test_find_all_begin_environments_whitespace(self, test_case):
        """Test find_all_begin_environments with whitespace variations."""
        result = Environment.find_all_begin_environments(test_case['content'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['find_all_begin_edge_case'])
    def test_find_all_begin_environments_edge_cases(self, test_case):
        """Test find_all_begin_environments with edge cases."""
        result = Environment.find_all_begin_environments(test_case['content'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['find_all_end_basic'])
    def test_find_all_end_environments_basic(self, test_case):
        """Test find_all_end_environments with basic test cases."""
        result = Environment.find_all_end_environments(test_case['content'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['find_begin_basic'])
    def test_find_begin_environment_basic(self, test_case):
        """Test find_begin_environment with basic test cases."""
        result = Environment.find_begin_environment(test_case['content'], test_case['environment_name'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['find_begin_whitespace'])
    def test_find_begin_environment_whitespace(self, test_case):
        """Test find_begin_environment with whitespace variations."""
        result = Environment.find_begin_environment(test_case['content'], test_case['environment_name'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['find_begin_edge_case'])
    def test_find_begin_environment_edge_cases(self, test_case):
        """Test find_begin_environment with edge cases."""
        result = Environment.find_begin_environment(test_case['content'], test_case['environment_name'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['find_end_basic'])
    def test_find_end_environment_basic(self, test_case):
        """Test find_end_environment with basic test cases."""
        result = Environment.find_end_environment(test_case['content'], test_case['environment_name'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['find_end_whitespace'])
    def test_find_end_environment_whitespace(self, test_case):
        """Test find_end_environment with whitespace variations."""
        result = Environment.find_end_environment(test_case['content'], test_case['environment_name'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['integration'])
    def test_integration_tests(self, test_case):
        """Test integration scenarios with multiple environment methods."""
        if 'expected_begins' in test_case:
            begin_result = Environment.find_all_begin_environments(test_case['content'])
            assert begin_result == test_case['expected_begins'], f"Begin test failed for {test_case['description']}"
        
        if 'expected_ends' in test_case:
            end_result = Environment.find_all_end_environments(test_case['content'])
            assert end_result == test_case['expected_ends'], f"End test failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['invalid_input'])
    def test_invalid_input_handling(self, test_case):
        """Test handling of invalid input types."""
        result = Environment.find_all_begin_environments(test_case['content'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['parse_args_basic'])
    def test_parse_environment_arguments_basic(self, test_case):
        """Test parse_environment_arguments with basic test cases."""
        result = Environment.parse_environment_arguments(
            test_case['content'],
            test_case['environment_name'],
            test_case['begin_start'],
            test_case['begin_end'],
            test_case['syntax']
        )
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['parse_args_whitespace'])
    def test_parse_environment_arguments_whitespace(self, test_case):
        """Test parse_environment_arguments with whitespace variations."""
        result = Environment.parse_environment_arguments(
            test_case['content'],
            test_case['environment_name'],
            test_case['begin_start'],
            test_case['begin_end'],
            test_case['syntax']
        )
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['parse_args_optional'])
    def test_parse_environment_arguments_optional(self, test_case):
        """Test parse_environment_arguments with optional arguments."""
        result = Environment.parse_environment_arguments(
            test_case['content'],
            test_case['environment_name'],
            test_case['begin_start'],
            test_case['begin_end'],
            test_case['syntax']
        )
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['parse_args_edge_case'])
    def test_parse_environment_arguments_edge_cases(self, test_case):
        """Test parse_environment_arguments with edge cases."""
        result = Environment.parse_environment_arguments(
            test_case['content'],
            test_case['environment_name'],
            test_case['begin_start'],
            test_case['begin_end'],
            test_case['syntax']
        )
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['parse_args_nested'])
    def test_parse_environment_arguments_nested(self, test_case):
        """Test parse_environment_arguments with nested brackets/braces."""
        result = Environment.parse_environment_arguments(
            test_case['content'],
            test_case['environment_name'],
            test_case['begin_start'],
            test_case['begin_end'],
            test_case['syntax']
        )
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['parse_args_complex'])
    def test_parse_environment_arguments_complex(self, test_case):
        """Test parse_environment_arguments with complex real-world cases."""
        result = Environment.parse_environment_arguments(
            test_case['content'],
            test_case['environment_name'],
            test_case['begin_start'],
            test_case['begin_end'],
            test_case['syntax']
        )
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['parse_args_error_handling'])
    def test_parse_environment_arguments_error_handling(self, test_case):
        """Test parse_environment_arguments error handling with malformed input."""
        result = Environment.parse_environment_arguments(
            test_case['content'],
            test_case['environment_name'],
            test_case['begin_start'],
            test_case['begin_end'],
            test_case['syntax']
        )
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['parse_args_edge_coverage'])
    def test_parse_environment_arguments_edge_coverage(self, test_case):
        """Test parse_environment_arguments edge cases for coverage."""
        result = Environment.parse_environment_arguments(
            test_case['content'],
            test_case['environment_name'],
            test_case['begin_start'],
            test_case['begin_end'],
            test_case['syntax']
        )
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['parse_args_star'])
    def test_parse_environment_arguments_star(self, test_case):
        """Test parse_environment_arguments with star environments."""
        result = Environment.parse_environment_arguments(
            test_case['content'],
            test_case['environment_name'],
            test_case['begin_start'],
            test_case['begin_end'],
            test_case['syntax']
        )
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['find_all_begin_star'])
    def test_find_all_begin_environments_star(self, test_case):
        """Test find_all_begin_environments with star environments."""
        result = Environment.find_all_begin_environments(test_case['content'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['find_all_end_star'])
    def test_find_all_end_environments_star(self, test_case):
        """Test find_all_end_environments with star environments."""
        result = Environment.find_all_end_environments(test_case['content'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['find_begin_star'])
    def test_find_begin_environment_star(self, test_case):
        """Test find_begin_environment with star environments."""
        result = Environment.find_begin_environment(
            test_case['content'],
            test_case['environment_name']
        )
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", load_test_cases()['find_end_star'])
    def test_find_end_environment_star(self, test_case):
        """Test find_end_environment with star environments."""
        result = Environment.find_end_environment(
            test_case['content'],
            test_case['environment_name']
        )
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    # Internal method tests for 100% coverage
    def test_parse_bracket_argument_invalid_start_pos(self):
        """Test _parse_bracket_argument with invalid start position."""
        content = r'[test]'
        
        # Test with start_pos >= len(content)
        result = Command._parse_bracket_argument(content, 10)
        assert result is None
        
        # Test with start_pos pointing to non-bracket character
        result = Command._parse_bracket_argument(content, 1)  # Points to 't'
        assert result is None

    def test_parse_brace_argument_invalid_start_pos(self):
        """Test _parse_brace_argument with invalid start position."""
        content = r'{test}'
        
        # Test with start_pos >= len(content)
        result = Command._parse_brace_argument(content, 10)
        assert result is None
        
        # Test with start_pos pointing to non-brace character  
        result = Command._parse_brace_argument(content, 1)  # Points to 't'
        assert result is None

    def test_parse_bracket_argument_valid_cases(self):
        """Test _parse_bracket_argument with valid inputs."""
        # Simple case
        content = r'[test]'
        result = Command._parse_bracket_argument(content, 0)
        expected = {'value': 'test', 'start': 0, 'end': 6}
        assert result == expected
        
        # Nested brackets
        content = r'[test[nested]more]'
        result = Command._parse_bracket_argument(content, 0)
        expected = {'value': 'test[nested]more', 'start': 0, 'end': 18}
        assert result == expected
        
        # Empty brackets
        content = r'[]'
        result = Command._parse_bracket_argument(content, 0)
        expected = {'value': '', 'start': 0, 'end': 2}
        assert result == expected

    def test_parse_brace_argument_valid_cases(self):
        """Test _parse_brace_argument with valid inputs."""
        # Simple case
        content = r'{test}'
        result = Command._parse_brace_argument(content, 0)
        expected = {'value': 'test', 'start': 0, 'end': 6}
        assert result == expected
        
        # Nested braces
        content = r'{test{nested}more}'
        result = Command._parse_brace_argument(content, 0)
        expected = {'value': 'test{nested}more', 'start': 0, 'end': 18}
        assert result == expected
        
        # Empty braces
        content = r'{}'
        result = Command._parse_brace_argument(content, 0)
        expected = {'value': '', 'start': 0, 'end': 2}
        assert result == expected

    def test_parse_environment_arguments_branch_coverage(self):
        """Test specific branch that hits the break statement when arg_result is None."""
        # This should trigger the specific branch where _parse_brace_argument returns None
        # causing the break statement at line ~197
        content = r'\begin{array}{incomplete'  # No closing brace
        result = Environment.parse_environment_arguments(
            content,
            'array',
            0,
            13,
            r'\begin{array}{cols}'
        )
        # Should return with empty arguments since parsing fails
        expected = {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 13,
            'arguments': {}
        }
        assert result == expected

    @pytest.mark.parametrize("test_case", load_test_cases()['parse_args_multiple_required'])
    def test_parse_environment_arguments_multiple_required(self, test_case):
        """Test parse_environment_arguments with multiple required arguments to hit 182->156 branch."""
        result = Environment.parse_environment_arguments(
            test_case['content'],
            test_case['environment_name'],
            test_case['begin_start'],
            test_case['begin_end'],
            test_case['syntax']
        )
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    def test_parse_environment_arguments_error_coverage(self):
        """Test the ValueError path in parse_environment_arguments for 100% coverage."""
        # We need to directly test the internal parsing logic that can trigger the ValueError
        # This involves manually creating a malformed syntax_args list with an invalid argument type
        
        content = r'\begin{foo}{arg}'
        environment_name = 'foo'
        begin_start = 0
        begin_end = 11
        
        # Mock the syntax parsing to return an invalid arg_type
        import unittest.mock
        
        with unittest.mock.patch.object(Command, 'parse_syntax_arguments') as mock_parse_syntax:
            # Make parse_syntax_arguments return an invalid argument type
            mock_parse_syntax.return_value = [
                {'type': 'invalid_type', 'name': 'test'}  # This should trigger the ValueError
            ]
            
            # Verify that the ValueError is raised for invalid argument types
            with pytest.raises(ValueError, match="is not required or optional"):
                Environment.parse_environment_arguments(
                    content,
                    environment_name,
                    begin_start,
                    begin_end,
                    r'\begin{foo}{arg}'
                )