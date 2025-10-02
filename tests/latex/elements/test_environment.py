# File: test_environment.py
# Description: Unit tests for Environment class methods using fixture-based testing
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import os
import sys
import pytest

from latex_parser.latex.elements.environment import Environment


def load_test_cases():
    """Load test cases from the fixtures directory."""
    fixtures_dir = os.path.join(os.path.dirname(__file__), '..', 'fixtures')
    sys.path.insert(0, fixtures_dir)
    
    try:
        from environment_test_cases import (
            FIND_ALL_BEGIN_ENVIRONMENTS_BASIC_TESTS,
            FIND_ALL_BEGIN_ENVIRONMENTS_WHITESPACE_TESTS,
            FIND_ALL_BEGIN_ENVIRONMENTS_EDGE_CASE_TESTS,
            FIND_ALL_END_ENVIRONMENTS_BASIC_TESTS,
            FIND_BEGIN_ENVIRONMENT_BASIC_TESTS,
            FIND_BEGIN_ENVIRONMENT_WHITESPACE_TESTS,
            FIND_BEGIN_ENVIRONMENT_EDGE_CASE_TESTS,
            FIND_END_ENVIRONMENT_BASIC_TESTS,
            FIND_END_ENVIRONMENT_WHITESPACE_TESTS,
            INTEGRATION_TESTS,
            INVALID_INPUT_TESTS
        )
        return {
            'find_all_begin_basic': FIND_ALL_BEGIN_ENVIRONMENTS_BASIC_TESTS,
            'find_all_begin_whitespace': FIND_ALL_BEGIN_ENVIRONMENTS_WHITESPACE_TESTS,
            'find_all_begin_edge_case': FIND_ALL_BEGIN_ENVIRONMENTS_EDGE_CASE_TESTS,
            'find_all_end_basic': FIND_ALL_END_ENVIRONMENTS_BASIC_TESTS,
            'find_begin_basic': FIND_BEGIN_ENVIRONMENT_BASIC_TESTS,
            'find_begin_whitespace': FIND_BEGIN_ENVIRONMENT_WHITESPACE_TESTS,
            'find_begin_edge_case': FIND_BEGIN_ENVIRONMENT_EDGE_CASE_TESTS,
            'find_end_basic': FIND_END_ENVIRONMENT_BASIC_TESTS,
            'find_end_whitespace': FIND_END_ENVIRONMENT_WHITESPACE_TESTS,
            'integration': INTEGRATION_TESTS,
            'invalid_input': INVALID_INPUT_TESTS
        }
    finally:
        sys.path.pop(0)


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