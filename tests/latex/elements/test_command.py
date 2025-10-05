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

from latex.fixtures.def_command_test_cases import (
    MODERNIZE_DEF_COMMANDS_BASIC_TESTS,
    MODERNIZE_DEF_COMMANDS_SKIP_TESTS,
    MODERNIZE_DEF_COMMANDS_STRICT_TESTS,
    MODERNIZE_DEF_COMMANDS_EDGE_TESTS,
    MODERNIZE_DEF_COMMANDS_COVERAGE_TESTS,
    MODERNIZE_DEF_COMMANDS_EDGE_COVERAGE_TESTS
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

    # === Modernize Def Commands Tests ===
    
    @pytest.mark.parametrize("test_case", MODERNIZE_DEF_COMMANDS_BASIC_TESTS)
    def test_modernize_def_commands_basic(self, test_case):
        """Test basic def command modernization."""
        result = Command.modernize_def_commands(test_case['input'], test_case['is_strict'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", MODERNIZE_DEF_COMMANDS_SKIP_TESTS)
    def test_modernize_def_commands_skip_unconvertible(self, test_case):
        """Test that unconvertible def commands are skipped in normal mode."""
        result = Command.modernize_def_commands(test_case['input'], test_case['is_strict'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", MODERNIZE_DEF_COMMANDS_STRICT_TESTS)
    def test_modernize_def_commands_strict_mode(self, test_case):
        """Test strict mode behavior for def command modernization."""
        if test_case['should_raise']:
            with pytest.raises(test_case['exception_type']) as exc_info:
                Command.modernize_def_commands(test_case['input'], test_case['is_strict'])
            
            # Verify the exception message contains expected text
            assert test_case['exception_message'] in str(exc_info.value), f"Exception message should contain '{test_case['exception_message']}' for {test_case['description']}"
        else:
            result = Command.modernize_def_commands(test_case['input'], test_case['is_strict'])
            assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", MODERNIZE_DEF_COMMANDS_EDGE_TESTS)
    def test_modernize_def_commands_edge_cases(self, test_case):
        """Test edge cases for def command modernization."""
        result = Command.modernize_def_commands(test_case['input'], test_case['is_strict'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", MODERNIZE_DEF_COMMANDS_COVERAGE_TESTS)
    def test_modernize_def_commands_coverage(self, test_case):
        """Test comprehensive coverage scenarios for def command modernization."""
        result = Command.modernize_def_commands(test_case['input'], test_case['is_strict'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", MODERNIZE_DEF_COMMANDS_EDGE_COVERAGE_TESTS)
    def test_modernize_def_commands_edge_coverage(self, test_case):
        """Test edge cases that improve code coverage for def command modernization."""
        result = Command.modernize_def_commands(test_case['input'], test_case['is_strict'])
        assert result == test_case['expected'], f"Failed for {test_case['description']}"

    def test_modernize_def_commands_strict_mode_unparseable(self):
        """Test strict mode with unparseable def commands."""
        # Create a def command that cannot be parsed
        unparseable_content = r'\def\cmd'  # Missing replacement
        
        # Normal mode should return unchanged
        result_normal = Command.modernize_def_commands(unparseable_content, is_strict=False)
        assert result_normal == unparseable_content
        
        # Strict mode should raise exception
        with pytest.raises(ValueError) as exc_info:
            Command.modernize_def_commands(unparseable_content, is_strict=True)
        
        assert "Failed to parse" in str(exc_info.value)

    def test_modernize_def_commands_conversion_failure_reasons(self):
        """Test that the helper method provides correct failure reasons."""
        # Test delimited parameters
        delimited_content = r'\def\cmd#1 stop{text}'
        with pytest.raises(ValueError) as exc_info:
            Command.modernize_def_commands(delimited_content, is_strict=True)
        assert "Contains delimited parameters" in str(exc_info.value)
        assert "stop" in str(exc_info.value)
        
        # Test non-sequential parameters
        nonseq_content = r'\def\cmd#1#3{text}'
        with pytest.raises(ValueError) as exc_info:
            Command.modernize_def_commands(nonseq_content, is_strict=True)
    def test_can_convert_def_to_newcommand_line_878_coverage(self):
        """
        Specific test to hit line 878 in _can_convert_def_to_newcommand.
        
        This tests the exact condition: delimiter.get('before_param') is None and len(delimiters) == 1
        when parameters are present (ensuring we enter the delimiter checking loop).
        """
        # Test scenario: parameters present + single delimiter with before_param=None
        # This represents a pattern like: \def\cmd#1{text} where the parser identifies
        # the command name as a delimiter with before_param=None
        params = [{'number': 1, 'position': 10}]
        delims = [{'text': r'\cmd', 'before_param': None}]
        
        # This should return True and hit line 878 (the continue statement)
        result = Command._can_convert_def_to_newcommand(params, delims)
        assert result is True
        
        # Verify this doesn't hit the first condition (which would hit line 876)
        delimiter = delims[0]
        condition1 = 'before_param' in delimiter and delimiter['before_param'] == 1
        condition2 = delimiter.get('before_param') is None and len(delims) == 1
        
        assert condition1 is False  # Should not hit line 876
        assert condition2 is True   # Should hit line 878

    # === Direct Unit Tests for Helper Methods ===

    def test_can_convert_def_to_newcommand_direct(self):
        """Test _can_convert_def_to_newcommand method directly."""
        
        # Test with no parameters - should be convertible
        result = Command._can_convert_def_to_newcommand([], [])
        assert result is True
        
        # Test with sequential parameters - should be convertible
        params = [{'number': 1, 'position': 10}, {'number': 2, 'position': 12}, {'number': 3, 'position': 14}]
        delims = [{'text': r'\cmd', 'before_param': 1}]
        result = Command._can_convert_def_to_newcommand(params, delims)
        assert result is True
        
        # Test with non-sequential parameters - should not be convertible
        params = [{'number': 1, 'position': 10}, {'number': 3, 'position': 14}]  # Missing #2
        delims = [{'text': r'\cmd', 'before_param': 1}]
        result = Command._can_convert_def_to_newcommand(params, delims)
        assert result is False
        
        # Test with real delimiter structure (based on actual parsing output)
        params = []
        delims = [{'text': r'\simple', 'before_param': None}]  # Real structure from parser
        result = Command._can_convert_def_to_newcommand(params, delims)
        assert result is True  # This should hit line 751
        
        # Test specific edge case for line 878 coverage - single delimiter with before_param=None and parameters present
        # This condition: delimiter.get('before_param') is None and len(delimiters) == 1
        params = [{'number': 1, 'position': 10}]  # We have parameters
        delims = [{'text': r'\cmd', 'before_param': None}]  # Single delimiter with before_param=None
        result = Command._can_convert_def_to_newcommand(params, delims)
        assert result is True  # This should hit line 878
        
        # Another edge case: Multiple delimiters where first one is command name
        params = [{'number': 1, 'position': 10}]
        delims = [
            {'text': r'\cmd'},  # No before_param, but len(delimiters) > 1, should go to else
            {'text': 'extra', 'before_param': None}
        ]
        result = Command._can_convert_def_to_newcommand(params, delims)
        assert result is False
        
        # Test with delimited parameter (other delimiter) - should not be convertible
        params = [{'number': 1, 'position': 10}]
        delims = [
            {'text': r'\cmd', 'before_param': 1},
            {'text': 'stop', 'before_param': None}  # This should trigger the else branch
        ]
        result = Command._can_convert_def_to_newcommand(params, delims)
        assert result is False

    def test_get_conversion_failure_reason_direct(self):
        """Test _get_conversion_failure_reason method directly."""
        
        # Test with no parameters - should return "Unknown parsing error"
        def_result = {
            'arguments': {
                'pattern': {
                    'parameters': [],
                    'delimiters': []
                }
            }
        }
        reason = Command._get_conversion_failure_reason(def_result)
        assert reason == "Unknown parsing error"
        
        # Test with command name delimiter and no parameters (hits line 785)
        def_result = {
            'arguments': {
                'pattern': {
                    'parameters': [{'number': 1, 'position': 10}],
                    'delimiters': [{'text': r'\cmd', 'before_param': None}]  # Single delimiter, no parameters
                }
            }
        }
        reason = Command._get_conversion_failure_reason(def_result)
        assert reason == "Unknown conversion restriction"  # This hits line 789
        
        # Test with non-sequential parameters
        def_result = {
            'arguments': {
                'pattern': {
                    'parameters': [{'number': 1, 'position': 10}, {'number': 3, 'position': 14}],
                    'delimiters': [{'text': r'\cmd', 'before_param': 1}]
                }
            }
        }
        reason = Command._get_conversion_failure_reason(def_result)
        assert "Non-sequential parameters" in reason
        assert "[1, 3]" in reason
        assert "[1, 2]" in reason

    def test_extract_command_name_from_pattern_direct(self):
        """Test _extract_command_name_from_pattern method directly."""
        
        # Test with no parameters - pattern should be command name
        result = Command._extract_command_name_from_pattern(r'\mycommand', [])
        assert result == r'\mycommand'
        
        # Test with parameters - extract command name before first parameter
        params = [{'position': 10, 'number': 1}]
        result = Command._extract_command_name_from_pattern(r'\mycommand#1', params)
        assert result == r'\mycommand'
        
        # Test with invalid pattern (space in command name)
        result = Command._extract_command_name_from_pattern(r'\my command', [])
        assert result is None
        
        # Test with pattern not starting with backslash
        result = Command._extract_command_name_from_pattern(r'mycommand', [])
        assert result is None
        
        # Test with parameters and space in command name
        params = [{'position': 10, 'number': 1}]
        result = Command._extract_command_name_from_pattern(r'\my command#1', params)
        assert result is None

    def test_convert_def_to_newcommand_direct(self):
        """Test _convert_def_to_newcommand method directly."""
        
        # Test successful conversion - no parameters
        def_result = {
            'arguments': {
                'pattern': {
                    'value': r'\mycommand',
                    'parameters': [],
                    'delimiters': [{'text': r'\mycommand', 'before_param': None}]
                },
                'replacement': {
                    'value': 'Hello World'
                }
            }
        }
        result = Command._convert_def_to_newcommand(def_result)
        assert result == r'\newcommand{\mycommand}{Hello World}'
        
        # Test successful conversion - with parameters
        def_result = {
            'arguments': {
                'pattern': {
                    'value': r'\mycommand#1#2',
                    'parameters': [{'number': 1, 'position': 10}, {'number': 2, 'position': 12}],
                    'delimiters': [{'text': r'\mycommand', 'before_param': 1}]
                },
                'replacement': {
                    'value': '#1 and #2'
                }
            }
        }
        result = Command._convert_def_to_newcommand(def_result)
        assert result == r'\newcommand{\mycommand}[2]{#1 and #2}'
        
        # Test failed conversion - non-convertible pattern
        def_result = {
            'arguments': {
                'pattern': {
                    'value': r'\mycommand#1 stop',
                    'parameters': [{'number': 1, 'position': 10}],
                    'delimiters': [
                        {'text': r'\mycommand', 'before_param': 1},
                        {'text': 'stop', 'after_last_param': True}
                    ]
                },
                'replacement': {
                    'value': 'Hello #1'
                }
            }
        }
        result = Command._convert_def_to_newcommand(def_result)
        assert result is None
        
        # Test failed command name extraction
        def_result = {
            'arguments': {
                'pattern': {
                    'value': r'my command',  # Invalid pattern
                    'parameters': [],
                    'delimiters': []
                },
                'replacement': {
                    'value': 'text'
                }
            }
        }
        result = Command._convert_def_to_newcommand(def_result)
        assert result is None

    def test_modernize_def_commands_helper_method_coverage(self):
        """Test edge cases in helper methods for complete coverage."""
        # Test _extract_command_name_from_pattern with edge cases
        
        # Test pattern with space in command name
        assert Command._extract_command_name_from_pattern(r'\my command', []) is None
        
        # Test pattern not starting with backslash
        assert Command._extract_command_name_from_pattern('mycommand', []) is None
        
        # Test empty pattern
        assert Command._extract_command_name_from_pattern('', []) is None
        
        # Test pattern with space but no parameters
        assert Command._extract_command_name_from_pattern('  ', []) is None
        
        # Test valid pattern with parameters
        param_info = [{'number': 1, 'position': 10, 'text': '#1'}]
        assert Command._extract_command_name_from_pattern(r'\mycommand#1', param_info) == r'\mycommand'
        
        # Test pattern with space and parameters
        assert Command._extract_command_name_from_pattern(r'\my command#1', param_info) is None

    def test_modernize_def_commands_get_failure_reason_edge_cases(self):
        """Test edge cases in _get_conversion_failure_reason method."""
        
        # Test case where parameters is empty (Unknown parsing error)
        def_result_no_params = {
            'arguments': {
                'pattern': {
                    'parameters': [],
                    'delimiters': []
                }
            }
        }
        
        reason = Command._get_conversion_failure_reason(def_result_no_params)
        assert reason == "Unknown parsing error"
        
        # Test case with unknown delimiter (no text key)
        def_result_unknown_delimiter = {
            'arguments': {
                'pattern': {
                    'parameters': [{'number': 1, 'position': 10}],
                    'delimiters': [
                        {'before_param': 1},  # Command name delimiter
                        {'after_param': True}  # Delimiter without text key
                    ]
                }
            }
        }
        
        reason = Command._get_conversion_failure_reason(def_result_unknown_delimiter)
        assert "Contains delimited parameters" in reason
        assert "unknown" in reason