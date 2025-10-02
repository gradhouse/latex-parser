# File: test_command.py
# Description: Test cases for LaTeX command methods using fixtures
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import pytest
import sys
import os

from latex_parser.latex.elements.command import Command

# Add the tests directory to the path to import fixtures
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from latex.fixtures.command_test_cases import (
    FIND_ALL_COMMANDS_BASIC_TESTS,
    FIND_ALL_COMMANDS_AT_SYMBOL_TESTS,
    FIND_ALL_COMMANDS_WHITESPACE_TESTS,
    FIND_ALL_COMMANDS_EDGE_TESTS,
    FIND_COMMAND_SPECIFIC_TESTS,
    FIND_COMMAND_AT_SYMBOL_TESTS,
    FIND_COMMAND_BOUNDARY_TESTS,
    FIND_ALL_COMMANDS_COMPLEX_TESTS,
    FIND_COMMANDS_ERROR_TESTS,
    FIND_COMMAND_COVERAGE_TESTS,
    FIND_ALL_COMMANDS_LATEX_CORNER_CASES,
    FIND_COMMAND_LATEX_CORNER_CASES
)


class TestCommand:
    """Test class for Command methods using fixtures."""

    @pytest.mark.parametrize("test_case", FIND_ALL_COMMANDS_BASIC_TESTS)
    def test_find_all_commands_basic(self, test_case):
        """Test basic find_all_commands functionality."""
        result = Command.find_all_commands(test_case['content'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", FIND_ALL_COMMANDS_AT_SYMBOL_TESTS)
    def test_find_all_commands_at_symbol(self, test_case):
        """Test find_all_commands with @ symbol in command names."""
        result = Command.find_all_commands(test_case['content'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", FIND_ALL_COMMANDS_WHITESPACE_TESTS)
    def test_find_all_commands_whitespace(self, test_case):
        """Test find_all_commands with whitespace handling."""
        result = Command.find_all_commands(test_case['content'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", FIND_ALL_COMMANDS_EDGE_TESTS)
    def test_find_all_commands_edge_cases(self, test_case):
        """Test find_all_commands edge cases."""
        result = Command.find_all_commands(test_case['content'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", FIND_COMMAND_SPECIFIC_TESTS)
    def test_find_command_specific(self, test_case):
        """Test find_command for specific commands."""
        result = Command.find_command(test_case['content'], test_case['command_name'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", FIND_COMMAND_AT_SYMBOL_TESTS)
    def test_find_command_at_symbol(self, test_case):
        """Test find_command with @ symbol commands."""
        result = Command.find_command(test_case['content'], test_case['command_name'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", FIND_COMMAND_BOUNDARY_TESTS)
    def test_find_command_boundary(self, test_case):
        """Test find_command boundary conditions."""
        result = Command.find_command(test_case['content'], test_case['command_name'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", FIND_ALL_COMMANDS_COMPLEX_TESTS)
    def test_find_all_commands_complex(self, test_case):
        """Test find_all_commands with complex content."""
        result = Command.find_all_commands(test_case['content'])
        command_names = [name for name, start, end in result]
        
        # Check that all expected commands are found
        for expected_command in test_case['expected_commands']:
            assert expected_command in command_names, f"Missing command '{expected_command}' in {test_case['description']}"

    @pytest.mark.parametrize("test_case", FIND_COMMANDS_ERROR_TESTS)
    def test_find_commands_error_handling(self, test_case):
        """Test error handling in command finding."""
        if 'should_raise' in test_case:
            # Test expects an exception
            if test_case['should_raise'] == 'ValueError':
                try:
                    Command.find_command(test_case['content'], test_case['command_name'])
                    assert False, f"Expected ValueError but no exception was raised for {test_case['description']}"
                except ValueError:
                    pass  # Expected exception
            else:
                assert False, f"Unknown exception type: {test_case['should_raise']}"
        else:
            # Test expects a result
            result = Command.find_command(test_case['content'], test_case['command_name'])
            assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", FIND_COMMAND_COVERAGE_TESTS)
    def test_find_command_coverage_completion(self, test_case):
        """Test cases to complete code coverage."""
        result = Command.find_command(test_case['content'], test_case['command_name'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", FIND_ALL_COMMANDS_LATEX_CORNER_CASES)
    def test_find_all_commands_latex_corner_cases(self, test_case):
        """Test LaTeX command corner cases."""
        result = Command.find_all_commands(test_case['content'])
        assert result == test_case['expected'], f"Failed for: {test_case['description']}"

    @pytest.mark.parametrize("test_case", FIND_COMMAND_LATEX_CORNER_CASES)
    def test_find_command_latex_corner_cases(self, test_case):
        """Test specific command finding corner cases."""
        result = Command.find_command(test_case['content'], test_case['command_name'])
        assert result == test_case['expected'], f"Failed for: {test_case['description']}"

    def test_find_all_commands_invalid_input(self):
        """Test with invalid input types."""
        # Empty string should return empty list, not error
        assert Command.find_all_commands("") == []

    def test_find_command_invalid_inputs(self):
        """Test with invalid inputs."""
        # Empty strings should return empty list, not error
        assert Command.find_command("", r"\textbf") == []
        
        # Test with empty command name should raise ValueError due to validation
        try:
            Command.find_command("content", "")
            assert False, "Should have raised ValueError for empty command name"
        except ValueError:
            pass  # Expected
        
    def test_find_all_commands_overlap_coverage(self):
        """Test case to cover the overlap detection branch in find_all_commands."""
        # This test is designed to hit the 'position_already_captured' branch
        # by creating a scenario where the regex patterns could potentially overlap
        content = r'\alpha* \beta@ \gamma!'
        
        result = Command.find_all_commands(content)
        
        # The important thing is that we don't crash and handle overlaps correctly
        command_names = [name for name, start, end in result]
        
        # Expected: \alpha*, \beta (@ is not part of command name), \gamma
        # The @ and ! are not captured because they follow letter commands
        expected_commands = [r'\alpha*', r'\beta', r'\gamma']
        assert command_names == expected_commands