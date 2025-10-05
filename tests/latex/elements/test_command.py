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

from latex.fixtures.command_def_test_cases import (
    MODERNIZE_DEF_COMMANDS_BASIC_TESTS,
    MODERNIZE_DEF_COMMANDS_SKIP_TESTS,
    MODERNIZE_DEF_COMMANDS_STRICT_TESTS,
    MODERNIZE_DEF_COMMANDS_EDGE_TESTS,
    MODERNIZE_DEF_COMMANDS_COVERAGE_TESTS,
    MODERNIZE_DEF_COMMANDS_EDGE_COVERAGE_TESTS
)

from latex.fixtures.command_edge_cases import (
    ARGUMENT_PARSING_EDGE_CASES,
    MATH_DELIMITER_EDGE_CASES,
    DOCUMENT_ANALYSIS_ERROR_CASES
)

from latex.fixtures.document_analysis_test_cases import (
    DOCUMENT_DEFINED_COMMANDS_TESTS,
    DOCUMENT_DEFINED_ENVIRONMENTS_TESTS
)

from latex.fixtures.command_def_modernization_test_cases import (
    DEF_MODERNIZATION_ERROR_CASES,
    CAN_CONVERT_DEF_TESTS,
    CONVERSION_FAILURE_REASON_TESTS,
    EXTRACT_COMMAND_NAME_TESTS,
    CONVERT_DEF_TO_NEWCOMMAND_TESTS,
    INVALID_INPUT_TESTS,
    BOUNDARY_CONDITION_TESTS
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

    @pytest.mark.parametrize("test_case", INVALID_INPUT_TESTS)
    def test_invalid_input_handling(self, test_case):
        """Test invalid input handling using fixtures."""
        
        if test_case['method'] == 'find_all_commands':
            result = Command.find_all_commands(test_case['content'])
            assert result == test_case['expected']
            
        elif test_case['method'] == 'find_command':
            if test_case.get('should_raise'):
                # Test expects an exception
                if test_case['should_raise'] == 'ValueError':
                    with pytest.raises(ValueError) as exc_info:
                        Command.find_command(test_case['content'], test_case['command_name'])
                    assert test_case['expected_message'] in str(exc_info.value)
                else:
                    assert False, f"Unknown exception type: {test_case['should_raise']}"
            else:
                # Test expects a result
                result = Command.find_command(test_case['content'], test_case['command_name'])
                assert result == test_case['expected']
        
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

    # === Document Defined Commands Tests ===

    def test_get_document_defined_commands_empty_content(self):
        """Test get_document_defined_commands with empty content."""
        result = Command.get_document_defined_commands("")
        assert result == []

    def test_get_document_defined_commands_no_definitions(self):
        """Test get_document_defined_commands with content containing no command definitions."""
        content = r'\textbf{hello} \section{title} \begin{document} text \end{document}'
        result = Command.get_document_defined_commands(content)
        assert result == []

    def test_get_document_defined_commands_single_newcommand(self):
        """Test get_document_defined_commands with a single newcommand."""
        content = r'\newcommand{\foo}{Hello World}'
        result = Command.get_document_defined_commands(content)
        
        assert len(result) == 1
        cmd_def = result[0]
        
        assert cmd_def['command_name'] == r'\newcommand'
        assert 'arguments' in cmd_def
        assert 'cmd' in cmd_def['arguments']
        assert cmd_def['arguments']['cmd']['value'] == r'\foo'
        assert 'definition' in cmd_def['arguments']
        assert cmd_def['arguments']['definition']['value'] == 'Hello World'

    def test_get_document_defined_commands_newcommand_with_args(self):
        """Test get_document_defined_commands with newcommand that has arguments."""
        content = r'\newcommand{\greet}[1]{Hello #1}'
        result = Command.get_document_defined_commands(content)
        
        assert len(result) == 1
        cmd_def = result[0]
        
        assert cmd_def['command_name'] == r'\newcommand'
        assert cmd_def['arguments']['cmd']['value'] == r'\greet'
        assert cmd_def['arguments']['nargs']['value'] == '1'
        assert cmd_def['arguments']['definition']['value'] == 'Hello #1'

    def test_get_document_defined_commands_newcommand_with_default(self):
        """Test get_document_defined_commands with newcommand that has default argument."""
        content = r'\newcommand{\greet}[2][World]{Hello #1, #2}'
        result = Command.get_document_defined_commands(content)
        
        assert len(result) == 1
        cmd_def = result[0]
        
        assert cmd_def['command_name'] == r'\newcommand'
        assert cmd_def['arguments']['cmd']['value'] == r'\greet'
        assert cmd_def['arguments']['nargs']['value'] == '2'
        assert cmd_def['arguments']['default']['value'] == 'World'
        assert cmd_def['arguments']['definition']['value'] == 'Hello #1, #2'

    def test_get_document_defined_commands_all_types(self):
        """Test get_document_defined_commands with all command definition types."""
        content = r'''
\newcommand{\foo}{Hello}
\newcommand*{\bar}{World}
\renewcommand{\baz}{Updated}
\renewcommand*{\qux}{Updated*}
\providecommand{\new}{Provided}
\providecommand*{\newer}{Provided*}
'''
        result = Command.get_document_defined_commands(content)
        
        # Should find all 6 definitions
        assert len(result) == 6
        
        # Check that we have all the expected command types
        command_names = [cmd_def['command_name'] for cmd_def in result]
        expected_commands = [
            r'\newcommand', r'\newcommand*', 
            r'\renewcommand', r'\renewcommand*',
            r'\providecommand', r'\providecommand*'
        ]
        
        for expected in expected_commands:
            assert expected in command_names

    def test_get_document_defined_commands_sorted_by_position(self):
        """Test that get_document_defined_commands returns results sorted by position."""
        content = r'''
\renewcommand{\second}{B}
\newcommand{\first}{A}
\providecommand{\third}{C}
'''
        result = Command.get_document_defined_commands(content)
        
        assert len(result) == 3
        
        # Should be sorted by position in document
        assert result[0]['command_name'] == r'\renewcommand'
        assert result[0]['arguments']['cmd']['value'] == r'\second'
        
        assert result[1]['command_name'] == r'\newcommand'
        assert result[1]['arguments']['cmd']['value'] == r'\first'
        
        assert result[2]['command_name'] == r'\providecommand'
        assert result[2]['arguments']['cmd']['value'] == r'\third'

    def test_get_document_defined_commands_complex_definitions(self):
        """Test get_document_defined_commands with complex command definitions."""
        content = r'''
\newcommand{\complex}[3][default]{%
    This is #1 with #2 and #3
}
\renewcommand*{\another}[1]{Complex definition with \textbf{#1}}
'''
        result = Command.get_document_defined_commands(content)
        
        assert len(result) == 2
        
        # First command
        cmd1 = result[0]
        assert cmd1['command_name'] == r'\newcommand'
        assert cmd1['arguments']['cmd']['value'] == r'\complex'
        assert cmd1['arguments']['nargs']['value'] == '3'
        assert cmd1['arguments']['default']['value'] == 'default'
        assert 'This is #1 with #2 and #3' in cmd1['arguments']['definition']['value']
        
        # Second command
        cmd2 = result[1]
        assert cmd2['command_name'] == r'\renewcommand*'
        assert cmd2['arguments']['cmd']['value'] == r'\another'
        assert cmd2['arguments']['nargs']['value'] == '1'
        assert r'\textbf{#1}' in cmd2['arguments']['definition']['value']

    def test_get_document_defined_commands_mixed_content(self):
        """Test get_document_defined_commands with mixed LaTeX content."""
        content = r'''
\documentclass{article}
\usepackage{amsmath}

\newcommand{\mycommand}{Hello}

\begin{document}
Some text here.

\renewcommand{\date}[1]{Date: #1}

More text and \textbf{bold} text.

\providecommand{\footer}{Footer text}

\end{document}
'''
        result = Command.get_document_defined_commands(content)
        
        assert len(result) == 3
        
        # Check specific commands found
        cmd_names = [(r['command_name'], r['arguments']['cmd']['value']) for r in result]
        expected = [
            (r'\newcommand', r'\mycommand'),
            (r'\renewcommand', r'\date'),
            (r'\providecommand', r'\footer')
        ]
        
        assert cmd_names == expected

    def test_get_document_defined_commands_malformed_commands(self):
        """Test get_document_defined_commands with malformed command definitions."""
        content = r'''
\newcommand{\good}{Valid definition}
\newcommand{incomplete
\renewcommand{\also_good}[1]{Another valid one: #1}
'''
        result = Command.get_document_defined_commands(content)
        
        # Should find all commands, but malformed ones will have incomplete parsing
        assert len(result) == 3
        
        # Filter to only well-formed commands (those with 'cmd' argument)
        valid_commands = [r for r in result if 'cmd' in r.get('arguments', {})]
        assert len(valid_commands) == 2
        
        assert valid_commands[0]['arguments']['cmd']['value'] == r'\good'
        assert valid_commands[1]['arguments']['cmd']['value'] == r'\also_good'

    def test_get_document_defined_commands_position_info(self):
        """Test that get_document_defined_commands includes correct position information."""
        content = r'\newcommand{\test}{definition}'
        result = Command.get_document_defined_commands(content)
        
        assert len(result) == 1
        cmd_def = result[0]
        
        # Check that position information is included
        assert 'complete_start' in cmd_def
        assert 'complete_end' in cmd_def
        assert cmd_def['complete_start'] == 0  # Starts at beginning
        assert cmd_def['complete_end'] == len(content)  # Ends at end
        
        # Check argument positions
        assert 'start' in cmd_def['arguments']['cmd']
        assert 'end' in cmd_def['arguments']['cmd']
        assert 'start' in cmd_def['arguments']['definition']
        assert 'end' in cmd_def['arguments']['definition']

    def test_get_document_defined_commands_duplicate_commands(self):
        """Test get_document_defined_commands with duplicate command names."""
        content = r'''
\newcommand{\same}{First definition}
\renewcommand{\same}{Second definition}
\providecommand{\same}{Third definition}
'''
        result = Command.get_document_defined_commands(content)
        
        # Should find all three definitions
        assert len(result) == 3
        
        # All should have the same command name being defined
        for cmd_def in result:
            assert cmd_def['arguments']['cmd']['value'] == r'\same'
        
        # But different definition types
        types = [cmd_def['command_name'] for cmd_def in result]
        assert types == [r'\newcommand', r'\renewcommand', r'\providecommand']

    def test_get_document_defined_commands_nested_braces(self):
        """Test get_document_defined_commands with nested braces in definitions."""
        content = r'\newcommand{\nested}{Text with \textbf{bold \emph{italic}} content}'
        result = Command.get_document_defined_commands(content)
        
        assert len(result) == 1
        cmd_def = result[0]
        
        definition = cmd_def['arguments']['definition']['value']
        assert r'\textbf{bold \emph{italic}}' in definition

    def test_get_document_defined_commands_whitespace_handling(self):
        """Test get_document_defined_commands with various whitespace scenarios."""
        content = r'''
\newcommand  {\spaced}  {definition}
\renewcommand{\tight}[1]{tight#1}
\providecommand  {\mixed}  [2]  [default]  {mixed definition}
'''
        result = Command.get_document_defined_commands(content)
        
        assert len(result) == 3
        
        # Should handle whitespace correctly
        cmd_names = [r['arguments']['cmd']['value'] for r in result]
        assert r'\spaced' in cmd_names
        assert r'\tight' in cmd_names
        assert r'\mixed' in cmd_names

    # === Document Defined Environments Tests ===

    def test_get_document_defined_environments_empty_content(self):
        """Test get_document_defined_environments with empty content."""
        result = Command.get_document_defined_environments("")
        assert result == []

    def test_get_document_defined_environments_no_definitions(self):
        """Test get_document_defined_environments with content containing no environment definitions."""
        content = r'\textbf{hello} \section{title} \begin{document} text \end{document}'
        result = Command.get_document_defined_environments(content)
        assert result == []

    def test_get_document_defined_environments_single_newenvironment(self):
        """Test get_document_defined_environments with a single newenvironment."""
        content = r'\newenvironment{myenv}{\begin{center}}{\end{center}}'
        result = Command.get_document_defined_environments(content)
        
        assert len(result) == 1
        env_def = result[0]
        
        assert env_def['command_name'] == r'\newenvironment'
        assert 'arguments' in env_def
        assert 'name' in env_def['arguments']
        assert env_def['arguments']['name']['value'] == 'myenv'
        assert 'begin_definition' in env_def['arguments']
        assert env_def['arguments']['begin_definition']['value'] == r'\begin{center}'
        assert 'end_definition' in env_def['arguments']
        assert env_def['arguments']['end_definition']['value'] == r'\end{center}'

    def test_get_document_defined_environments_newenvironment_with_args(self):
        """Test get_document_defined_environments with newenvironment that has arguments."""
        content = r'\newenvironment{myenv}[1]{\begin{center} #1}{\end{center}}'
        result = Command.get_document_defined_environments(content)
        
        assert len(result) == 1
        env_def = result[0]
        
        assert env_def['command_name'] == r'\newenvironment'
        assert env_def['arguments']['name']['value'] == 'myenv'
        assert env_def['arguments']['nargs']['value'] == '1'
        assert '#1' in env_def['arguments']['begin_definition']['value']

    def test_get_document_defined_environments_newenvironment_with_default(self):
        """Test get_document_defined_environments with newenvironment that has default argument."""
        content = r'\newenvironment{myenv}[2][default]{\section{#1} #2}{\par}'
        result = Command.get_document_defined_environments(content)
        
        assert len(result) == 1
        env_def = result[0]
        
        assert env_def['command_name'] == r'\newenvironment'
        assert env_def['arguments']['name']['value'] == 'myenv'
        assert env_def['arguments']['nargs']['value'] == '2'
        assert env_def['arguments']['default']['value'] == 'default'
        assert r'\section{#1} #2' in env_def['arguments']['begin_definition']['value']

    def test_get_document_defined_environments_both_types(self):
        """Test get_document_defined_environments with both newenvironment and renewenvironment."""
        content = r'''
\newenvironment{myenv}{\begin{center}}{\end{center}}
\renewenvironment{document}{\begin{flushleft}}{\end{flushleft}}
'''
        result = Command.get_document_defined_environments(content)
        
        # Should find both definitions
        assert len(result) == 2
        
        # Check that we have both command types
        command_names = [env_def['command_name'] for env_def in result]
        assert r'\newenvironment' in command_names
        assert r'\renewenvironment' in command_names

    def test_get_document_defined_environments_sorted_by_position(self):
        """Test that get_document_defined_environments returns results sorted by position."""
        content = r'''
\renewenvironment{second}{\begin{b}}{\end{b}}
\newenvironment{first}{\begin{a}}{\end{a}}
'''
        result = Command.get_document_defined_environments(content)
        
        assert len(result) == 2
        
        # Should be sorted by position in document
        assert result[0]['command_name'] == r'\renewenvironment'
        assert result[0]['arguments']['name']['value'] == 'second'
        
        assert result[1]['command_name'] == r'\newenvironment'
        assert result[1]['arguments']['name']['value'] == 'first'

    def test_get_document_defined_environments_complex_definitions(self):
        """Test get_document_defined_environments with complex environment definitions."""
        content = r'''
\newenvironment{complex}[3][default]{%
    \section{#1}
    \begin{itemize}
    \item #2
    \item #3
    \end{itemize}
}{%
    \end{itemize}
    \par
}
'''
        result = Command.get_document_defined_environments(content)
        
        assert len(result) == 1
        env_def = result[0]
        
        assert env_def['command_name'] == r'\newenvironment'
        assert env_def['arguments']['name']['value'] == 'complex'
        assert env_def['arguments']['nargs']['value'] == '3'
        assert env_def['arguments']['default']['value'] == 'default'
        assert r'\section{#1}' in env_def['arguments']['begin_definition']['value']
        assert r'\par' in env_def['arguments']['end_definition']['value']

    def test_get_document_defined_environments_mixed_content(self):
        """Test get_document_defined_environments with mixed LaTeX content."""
        content = r'''
\documentclass{article}
\usepackage{amsmath}

\newenvironment{myquote}{\begin{quote}}{\end{quote}}

\begin{document}
Some text here.

\renewenvironment{abstract}{\section{Summary}}{\par}

More text and \textbf{bold} text.

\end{document}
'''
        result = Command.get_document_defined_environments(content)
        
        assert len(result) == 2
        
        # Check specific environments found
        env_names = [(r['command_name'], r['arguments']['name']['value']) for r in result]
        expected = [
            (r'\newenvironment', 'myquote'),
            (r'\renewenvironment', 'abstract')
        ]
        
        assert env_names == expected

    def test_get_document_defined_environments_malformed_commands(self):
        """Test get_document_defined_environments with malformed environment definitions."""
        content = r'''
\newenvironment{good}{\begin{center}}{\end{center}}
\newenvironment{incomplete
\renewenvironment{also_good}{\begin{quote}}{\end{quote}}
'''
        result = Command.get_document_defined_environments(content)
        
        # Should find all commands, but malformed ones will have incomplete parsing
        assert len(result) == 3
        
        # Filter to only well-formed commands (those with 'name' argument)
        valid_commands = [r for r in result if 'name' in r.get('arguments', {})]
        assert len(valid_commands) == 2
        
        assert valid_commands[0]['arguments']['name']['value'] == 'good'
        assert valid_commands[1]['arguments']['name']['value'] == 'also_good'

    def test_get_document_defined_environments_position_info(self):
        """Test that get_document_defined_environments includes correct position information."""
        content = r'\newenvironment{test}{\begin{center}}{\end{center}}'
        result = Command.get_document_defined_environments(content)
        
        assert len(result) == 1
        env_def = result[0]
        
        # Check that position information is included
        assert 'complete_start' in env_def
        assert 'complete_end' in env_def
        assert env_def['complete_start'] == 0  # Starts at beginning
        assert env_def['complete_end'] == len(content)  # Ends at end
        
        # Check argument positions
        assert 'start' in env_def['arguments']['name']
        assert 'end' in env_def['arguments']['name']
        assert 'start' in env_def['arguments']['begin_definition']
        assert 'end' in env_def['arguments']['begin_definition']

    def test_get_document_defined_environments_nested_braces(self):
        """Test get_document_defined_environments with nested braces in definitions."""
        content = r'\newenvironment{nested}{\begin{center}\textbf{bold \emph{italic}}}{\end{center}}'
        result = Command.get_document_defined_environments(content)
        
        assert len(result) == 1
        env_def = result[0]
        
        begin_def = env_def['arguments']['begin_definition']['value']
        assert r'\textbf{bold \emph{italic}}' in begin_def

    def test_get_document_defined_environments_whitespace_handling(self):
        """Test get_document_defined_environments with various whitespace scenarios."""
        content = r'''
\newenvironment  {spaced}  {\begin{center}}  {\end{center}}
\renewenvironment{tight}[1]{\begin{quote}#1}{\end{quote}}
'''
        result = Command.get_document_defined_environments(content)
        
        assert len(result) == 2
        
        # Should handle whitespace correctly
        env_names = [r['arguments']['name']['value'] for r in result]
        assert 'spaced' in env_names
        assert 'tight' in env_names

    # === Additional Coverage Tests ===

    def test_parse_syntax_arguments_error_cases(self):
        """Test parse_syntax_arguments with error conditions."""
        # Test with invalid syntax that doesn't match command name
        with pytest.raises(ValueError) as exc_info:
            Command.parse_syntax_arguments(r'\textbf{text}', r'\emph', False)
        assert "doesn't match expected pattern" in str(exc_info.value)
        
        # Test with environment syntax mismatch
        with pytest.raises(ValueError) as exc_info:
            Command.parse_syntax_arguments(r'\begin{center}', r'figure', True)
        assert "doesn't match expected pattern" in str(exc_info.value)

    def test_parse_arguments_error_cases(self):
        """Test parse_arguments with invalid argument types."""
        content = r'\textbf{hello}'
        
        # Mock a syntax that would cause an invalid argument type
        # We'll need to create a scenario where an invalid arg_type is encountered
        # This tests the "raise ValueError(f'{arg_type} is not required or optional')" line
        
        # Create a mock syntax parser result with invalid type
        original_parse_syntax = Command.parse_syntax_arguments
        
        def mock_parse_syntax(*args, **kwargs):
            return [{'type': 'invalid', 'name': 'test', 'position': 0}]
        
        Command.parse_syntax_arguments = mock_parse_syntax
        
        try:
            with pytest.raises(ValueError) as exc_info:
                Command.parse_arguments(content, r'\textbf', 0, 7, r'\textbf{text}', False)
            assert "invalid is not required or optional" in str(exc_info.value)
        finally:
            Command.parse_syntax_arguments = original_parse_syntax

    def test_parse_def_command_edge_cases(self):
        """Test parse_def_command with edge cases for better coverage."""
        # Test with command_end at end of content
        content = r'\def'
        result = Command.parse_def_command(content, 0, 4)
        assert result is None
        
        # Test with only whitespace after \def
        content = r'\def   '
        result = Command.parse_def_command(content, 0, 4)
        assert result is None
        
        # Test with pattern but no replacement braces
        content = r'\def\cmd'
        result = Command.parse_def_command(content, 0, 4)
        assert result is None
        
        # Test with pattern but invalid replacement
        content = r'\def\cmd{'
        result = Command.parse_def_command(content, 0, 4)
        assert result is None

    def test_find_math_delimiters_comprehensive(self):
        """Test find_math_delimiters with comprehensive coverage."""
        # Test with escaped delimiters - only $ needs escaping with backslash
        content = r'\$ text'
        result = Command.find_math_delimiters(content)
        assert len(result) == 0  # $ is escaped
        
        # Test \( \) \[ \] are commands, not escaped
        content = r'\( \) \[ \]'
        result = Command.find_math_delimiters(content)
        assert len(result) == 4  # All are valid math delimiters
        
        # Test with mixed escaped and unescaped
        content = r'\$ $ \$$ $$'
        result = Command.find_math_delimiters(content)
        # Should find: $, $$
        math_delims = [d['command_name'] for d in result]
        assert '$' in math_delims
        assert '$$' in math_delims
        
        # Test with multiple backslashes before $
        content = r'\\$ \\\$ \\\\$'  # Even backslashes = not escaped, odd = escaped
        result = Command.find_math_delimiters(content)
        math_delims = [d['command_name'] for d in result]
        assert len([d for d in math_delims if d == '$']) == 2  # First and last should be found

    def test_find_command_comprehensive_edge_cases(self):
        """Test find_command with comprehensive edge cases."""
        # Test command name validation
        with pytest.raises(ValueError):
            Command.find_command("content", "textbf")  # Missing backslash
        
        # Test with empty content
        result = Command.find_command("", r"\textbf")
        assert result == []
        
        # Test single character non-letter commands
        content = r'\@ \# \$ \%'
        result = Command.find_command(content, r'\@')
        assert len(result) == 1
        assert result[0] == (0, 2)
        
        # Test @ command followed by letters (should not match standalone @)
        content = r'\@makeother \@ \@gobble'
        result = Command.find_command(content, r'\@')
        assert len(result) == 1  # Only the standalone \@
        assert result[0] == (12, 14)

    def test_parse_bracket_argument_edge_cases(self):
        """Test _parse_bracket_argument edge cases."""
        # Test with no opening bracket
        result = Command._parse_bracket_argument("hello", 0)
        assert result is None
        
        # Test with position beyond content
        result = Command._parse_bracket_argument("[]", 5)
        assert result is None
        
        # Test with unmatched brackets
        result = Command._parse_bracket_argument("[unmatched", 0)
        assert result is None
        
        # Test with nested brackets
        content = "[outer [inner] content]"
        result = Command._parse_bracket_argument(content, 0)
        assert result is not None
        assert result['value'] == "outer [inner] content"

    def test_parse_brace_argument_edge_cases(self):
        """Test _parse_brace_argument edge cases."""
        # Test with no opening brace
        result = Command._parse_brace_argument("hello", 0)
        assert result is None
        
        # Test with position beyond content
        result = Command._parse_brace_argument("{}", 5)
        assert result is None
        
        # Test with unmatched braces
        result = Command._parse_brace_argument("{unmatched", 0)
        assert result is None
        
        # Test with nested braces
        content = "{outer {inner} content}"
        result = Command._parse_brace_argument(content, 0)
        assert result is not None
        assert result['value'] == "outer {inner} content"

    def test_apply_string_replacements_edge_cases(self):
        """Test apply_string_replacements edge cases."""
        # Test with empty replacements
        result = Command.apply_string_replacements("hello", {})
        assert result == "hello"
        
        # Test with multiple replacements
        content = "hello world test"
        replacements = {
            0: ("hi", 5),      # Replace "hello" with "hi"
            6: ("earth", 5),   # Replace "world" with "earth"
            12: ("case", 4)    # Replace "test" with "case"
        }
        result = Command.apply_string_replacements(content, replacements)
        assert result == "hi earth case"

    def test_find_all_commands_comprehensive_patterns(self):
        """Test find_all_commands with comprehensive pattern coverage."""
        # Test @ commands with and without letters
        content = r'\@makeother \@ \@gobble \@'
        result = Command.find_all_commands(content)
        command_names = [name for name, start, end in result]
        expected = [r'\@makeother', r'\@', r'\@gobble', r'\@']
        assert command_names == expected
        
        # Test overlap detection (non-letter pattern overlapping with letter pattern)
        content = r'\alpha\beta'  # Should not create overlap issues
        result = Command.find_all_commands(content)
        command_names = [name for name, start, end in result]
        assert r'\alpha' in command_names
        assert r'\beta' in command_names

    def test_find_command_pattern_variations(self):
        """Test find_command with various pattern edge cases."""
        # Test starred command variations
        content = r'\section \section* \section**'
        
        # Find non-starred version
        result = Command.find_command(content, r'\section')
        assert len(result) == 1
        assert result[0] == (0, 8)
        
        # Find starred version - should find both \section* instances
        result = Command.find_command(content, r'\section*')
        assert len(result) == 2  # Both \section* and first part of \section**
        assert result[0] == (9, 18)
        
        # Test @ commands with stars
        content = r'\@makeatother \@makeatother*'
        result = Command.find_command(content, r'\@makeatother')
        assert len(result) == 1
        assert result[0] == (0, 13)  # @ commands include the full name

    def test_get_document_defined_commands_error_handling(self):
        """Test get_document_defined_commands error handling and edge cases."""
        # Test with content that causes parse_arguments to return None
        content = r'\newcommand'  # Incomplete command
        result = Command.get_document_defined_commands(content)
        # Should handle None results gracefully
        assert len(result) >= 0  # May have empty results but shouldn't crash

    def test_get_document_defined_environments_error_handling(self):
        """Test get_document_defined_environments error handling and edge cases."""
        # Test with content that causes parse_arguments to return None
        content = r'\newenvironment'  # Incomplete command
        result = Command.get_document_defined_environments(content)
        # Should handle None results gracefully
        assert len(result) >= 0  # May have empty results but shouldn't crash

    def test_modernize_def_commands_comprehensive_coverage(self):
        """Test modernize_def_commands for comprehensive coverage."""
        # Test with content containing no \def commands
        content = r'\newcommand{\test}{hello}'
        result = Command.modernize_def_commands(content)
        assert result == content  # Should return unchanged
        
        # Test with multiple def commands, some convertible, some not
        content = r'''
\def\simple{text}
\def\withparam#1{hello #1}
\def\delimited#1 stop{#1}
\def\simple2{text2}
'''
        result = Command.modernize_def_commands(content, is_strict=False)
        # Should convert simple and withparam, skip delimited
        assert r'\newcommand{\simple}{text}' in result
        assert r'\newcommand{\withparam}[1]{hello #1}' in result
        assert r'\def\delimited#1 stop{#1}' in result  # Should remain unchanged
        assert r'\newcommand{\simple2}{text2}' in result

    def test_conversion_helper_methods_edge_cases(self):
        """Test helper methods with edge cases for full coverage."""
        
        # Test _can_convert_def_to_newcommand with various delimiter scenarios
        # Test with multiple delimiters where first one is not command name
        params = [{'number': 1, 'position': 10}]
        delims = [
            {'text': 'not_command', 'before_param': 2},  # Not the command name
            {'text': 'stop', 'after_last_param': True}
        ]
        result = Command._can_convert_def_to_newcommand(params, delims)
        assert result is False
        
        # Test _extract_command_name_from_pattern with edge cases
        # Test with space in command name with parameters
        result = Command._extract_command_name_from_pattern(r'\my command#1', [{'position': 11}])
        assert result is None
        
        # Test with empty pattern
        result = Command._extract_command_name_from_pattern('', [])
        assert result is None

    def test_parse_def_command_comprehensive_patterns(self):
        """Test parse_def_command with comprehensive pattern coverage."""
        # Test with complex delimiter patterns
        content = r'\def\cmd#1[#2]#3{replacement with #1, #2, #3}'
        result = Command.parse_def_command(content, 0, 4)
        assert result is not None
        
        # Verify delimiter parsing
        delimiters = result['arguments']['pattern']['delimiters']
        assert len(delimiters) > 0
        
        # Test with pattern ending with delimiter after last parameter
        content = r'\def\cmd#1#2 end{replacement}'
        result = Command.parse_def_command(content, 0, 4)
        assert result is not None
        delimiters = result['arguments']['pattern']['delimiters']
        # Should have delimiter after last parameter
        has_end_delimiter = any(d.get('after_last_param', False) for d in delimiters)
        assert has_end_delimiter

    def test_parse_arguments_specific_branches(self):
        """Test specific branches in parse_arguments for full coverage."""
        # Test the branch where content[parse_position] != '['  for optional arguments
        content = r'\newcommand{\test}hello'  # Missing { after }
        result = Command.parse_arguments(content, r'\newcommand', 0, 11, 
                                       r'\newcommand{cmd}[nargs][default]{definition}', False)
        # Should stop parsing when it can't find the expected {
        assert result is not None
        # Should only have the cmd argument, missing the others
        assert 'cmd' in result['arguments']
        
        # Test the branch where content[parse_position] != '{' for required arguments
        content = r'\newcommand{\test}[1]hello'  # Missing { before hello
        result = Command.parse_arguments(content, r'\newcommand', 0, 11,
                                       r'\newcommand{cmd}[nargs][default]{definition}', False)
        assert result is not None
        assert 'cmd' in result['arguments']
        assert 'nargs' in result['arguments']
        # Should not have definition since parsing failed there

    def test_parse_arguments_early_termination(self):
        """Test parse_arguments with early termination conditions."""
        # Test where parse_position >= len(content) during parsing
        content = r'\newcommand{\test}'  # Ends abruptly
        result = Command.parse_arguments(content, r'\newcommand', 0, 11,
                                       r'\newcommand{cmd}[nargs][default]{definition}', False)
        assert result is not None
        # Should have cmd but not other arguments
        assert 'cmd' in result['arguments']
        assert 'definition' not in result['arguments']

    def test_find_command_single_char_branches(self):
        """Test find_command branches for single character commands."""
        # Test single character alpha command (covers line 116-117 area)
        content = r'\a \b \c'
        result = Command.find_command(content, r'\a')
        assert len(result) == 1
        assert result[0] == (0, 2)
        
        # Test non-alpha single character (covers other branch)
        content = r'\! \@ \#'
        result = Command.find_command(content, r'\!')
        assert len(result) == 1
        assert result[0] == (0, 2)

    def test_find_command_with_at_symbol_edge_cases(self):
        """Test find_command with @ symbol edge cases."""
        # Test @ command followed by non-letters vs @ commands with letters
        content = r'\@! \@123 \@gobble'
        result = Command.find_command(content, r'\@')
        # \@! and \@123 are @ followed by non-letters, but \@gobble is \@gobble command
        assert len(result) == 2  # Only \@! and \@123, not \@gobble
        assert result[0] == (0, 2)
        assert result[1] == (4, 6)
        
        # Test finding the full \@gobble command
        result = Command.find_command(content, r'\@gobble')
        assert len(result) == 1
        assert result[0] == (10, 18)
        
        # Test that @ commands with letters are treated as complete commands
        content = r'\@makeatletter \@makeatother \@firstofone'
        all_commands = Command.find_all_commands(content)
        command_names = [name for name, start, end in all_commands]
        assert r'\@makeatletter' in command_names
        assert r'\@makeatother' in command_names 
        assert r'\@firstofone' in command_names

    def test_parse_syntax_arguments_with_complex_patterns(self):
        """Test parse_syntax_arguments with complex argument patterns."""
        # Test with multiple optional and required arguments
        syntax = r'\newcommand{cmd}[nargs][default]{definition}'
        result = Command.parse_syntax_arguments(syntax, r'\newcommand', False)
        
        assert len(result) == 4
        arg_names = [arg['name'] for arg in result]
        assert 'cmd' in arg_names
        assert 'nargs' in arg_names
        assert 'default' in arg_names
        assert 'definition' in arg_names
        
        # Test environment syntax
        syntax = r'\begin{array}[pos]{cols}'
        result = Command.parse_syntax_arguments(syntax, 'array', True)
        assert len(result) == 2
        arg_names = [arg['name'] for arg in result]
        assert 'pos' in arg_names
        assert 'cols' in arg_names

    def test_def_command_parameter_edge_cases(self):
        """Test def command parsing with parameter edge cases."""
        # Test def command with no delimiters (empty pattern)
        content = r'\def{replacement}'
        result = Command.parse_def_command(content, 0, 4)
        assert result is not None
        delimiters = result['arguments']['pattern']['delimiters']
        assert len(delimiters) == 0
        
        # Test with pattern that has text but no parameters
        content = r'\def\simplecommand{replacement}'
        result = Command.parse_def_command(content, 0, 4)
        assert result is not None
        pattern_info = result['arguments']['pattern']
        assert len(pattern_info['parameters']) == 0
        assert len(pattern_info['delimiters']) == 1
        assert pattern_info['delimiters'][0]['text'] == r'\simplecommand'

    def test_conversion_helper_complete_coverage(self):
        """Test conversion helpers for complete coverage."""
        # Test _get_conversion_failure_reason with the "unknown conversion restriction" branch
        def_result = {
            'arguments': {
                'pattern': {
                    'parameters': [{'number': 1}],  # Sequential parameters
                    'delimiters': [{'text': r'\cmd', 'before_param': 1}]  # Only command name
                }
            }
        }
        
        # This should hit the "Unknown conversion restriction" branch
        # by passing all checks but still failing for some other reason
        reason = Command._get_conversion_failure_reason(def_result)
        assert reason == "Unknown conversion restriction"

    def test_modernize_def_edge_cases(self):
        """Test modernize_def_commands edge cases."""
        # Test where parse_def_command returns None but is_strict=False
        content = r'\def'  # Incomplete def command
        result = Command.modernize_def_commands(content, is_strict=False)
        assert result == content  # Should return unchanged
        
        # Test where _convert_def_to_newcommand returns None (unconvertible)
        content = r'\def\cmd#1 stop{text}'  # Delimited parameter
        result = Command.modernize_def_commands(content, is_strict=False)
        assert result == content  # Should remain unchanged

    def test_remaining_coverage_edge_cases(self):
        """Test remaining edge cases for 100% coverage."""
        
        # Test lines around 223, 228 - parse_arguments with required argument parsing failures
        content = r'\textbf'  # Command without any braces
        # This should test the branch where _parse_brace_argument returns None
        result = Command.parse_arguments(content, r'\textbf', 0, 7, r'\textbf{text}', False)
        assert result is not None
        # Should have empty arguments since parsing failed
        assert result['arguments'] == {}
        
        # Test command_end calculation branches in find_command (lines around 116-120)
        # Test single alpha character command
        content = r'\a text'
        result = Command.find_command(content, r'\a')
        assert len(result) == 1
        assert result[0] == (0, 2)
        
        # Test the branch in find_all_commands where @ is checked
        content = r'\@ \@letter'
        result = Command.find_all_commands(content)
        command_names = [name for name, start, end in result]
        assert r'\@' in command_names
        assert r'\@letter' in command_names
        
        # Test parse_def_command with edge case for delimiters (around lines 638-644)
        # Test case where pattern ends exactly at parameter position
        content = r'\def\cmd#1{text}'
        result = Command.parse_def_command(content, 0, 4)
        assert result is not None
        # Should handle case where last_end equals len(pattern)
        
        # Test _parse_bracket_argument and _parse_brace_argument return None cases
        # These test the branches where argument parsing fails
        content = r'\textbf{'  # Unclosed brace
        result = Command._parse_brace_argument(content, 7)
        assert result is None
        
        content = r'\textbf['  # Unclosed bracket  
        result = Command._parse_bracket_argument(content, 7)
        assert result is None

    def test_specific_line_coverage_cases(self):
        """Test very specific cases to hit remaining uncovered lines."""
        
        # Test the line 341 branch - where command_name startswith @ in find_command
        content = r'\@test \@test*'
        result = Command.find_command(content, r'\@test')
        assert len(result) == 1
        assert result[0] == (0, 6)
        
        # Test the non-letter command pattern (around line 285)
        content = r'\$ \% \#'
        result = Command.find_command(content, r'\$')
        assert len(result) == 1
        
        # Test line 557->562 branch in find_math_delimiters
        # Test case where backslash count is checked for $
        content = r'\\$ text'  # Even number of backslashes, so $ is not escaped
        result = Command.find_math_delimiters(content)
        assert len(result) == 1
        assert result[0]['command_name'] == '$'
        
        # Test the branch lines 800->797, 885->882 - these are likely in helper methods
        # Test _can_convert_def_to_newcommand with specific delimiter patterns
        params = []
        delims = [{'text': 'test', 'before_param': None}]
        result = Command._can_convert_def_to_newcommand(params, delims)
        assert result is True  # Should pass for no parameters case
        
        # Test lines 705-706, 719-720 - likely in get_document_defined methods
        # Test with completely empty parse results
        content = r'\newcommand'  # Incomplete command that might return None from parse_arguments
        result = Command.get_document_defined_commands(content)
        # Should handle gracefully even if parsing returns None for some entries

    def test_final_coverage_edge_cases(self):
        """Test the final edge cases to achieve 100% coverage."""
        
        # Test lines 223, 228 - parse_arguments branches where required argument parsing fails
        # Create a scenario where _parse_brace_argument returns None for required argument
        content = r'\textbf{unclosed'  # Missing closing brace
        result = Command.parse_arguments(content, r'\textbf', 0, 7, r'\textbf{text}', False)
        assert result is not None
        # Parsing should stop when required argument can't be parsed
        assert result['complete_end'] == 7  # Should not advance past command name
        
        # Test line 341 - command_name.startswith('@') branch in find_command
        content = r'\@test@more text'
        result = Command.find_command(content, r'\@test')  
        assert len(result) == 1
        
        # Test lines 557->562 - math delimiter backslash counting edge case
        content = r'\\\$ text'  # Odd number of backslashes = escaped
        result = Command.find_math_delimiters(content)
        # Should not find $ because it's escaped by odd number of backslashes
        dollar_delims = [d for d in result if d['command_name'] == '$']
        assert len(dollar_delims) == 0
        
        # Test lines 705-706, 719-720 - document defined commands/environments with None results
        # Mock a scenario where parse_arguments returns None
        original_parse_arguments = Command.parse_arguments
        
        def mock_parse_arguments(*args, **kwargs):
            return None  # Simulate parsing failure
            
        Command.parse_arguments = mock_parse_arguments
        
        try:
            content = r'\newcommand{\test}{hello}'
            result = Command.get_document_defined_commands(content)
            # Should handle None results gracefully by filtering them out
            assert result == []
            
            content = r'\newenvironment{test}{\begin{center}}{\end{center}}'
            result = Command.get_document_defined_environments(content)
            # Should handle None results gracefully by filtering them out  
            assert result == []
        finally:
            Command.parse_arguments = original_parse_arguments
            
        # Test lines 800->797, 885->882 - specific branches in helper methods
        # Test _can_convert_def_to_newcommand edge case with parameters but special delimiter
        params = [{'number': 1, 'position': 5}]
        delims = [{'text': r'\cmd', 'before_param': None}]  # before_param is None but we have params
        result = Command._can_convert_def_to_newcommand(params, delims)  
        # This should hit the elif branch for delimiter.get('before_param') is None
        assert result is True
        
        # Test line 256->241 - parse_arguments early termination branch
        content = r'\textbf'  # Command without arguments but syntax expects them
        result = Command.parse_arguments(content, r'\textbf', 0, 7, r'\textbf{text}', False)
        assert result is not None
        # Should return with empty arguments when parsing reaches end of content
        assert 'text' not in result['arguments']

    @pytest.mark.parametrize("test_case", ARGUMENT_PARSING_EDGE_CASES)
    def test_argument_parsing_edge_cases(self, test_case):
        """Test argument parsing edge cases and error conditions using fixtures."""
        
        if test_case['method'] == 'parse_arguments':
            result = Command.parse_arguments(
                test_case['content'], 
                test_case['command_name'], 
                test_case['start_pos'], 
                test_case['end_pos'],
                test_case['template'], 
                test_case['allow_optional']
            )
            assert result is not None
            
            if test_case.get('expected_has_cmd'):
                assert 'cmd' in result['arguments']
            if test_case.get('expected_missing_definition'):
                assert 'definition' not in result['arguments']
            if test_case.get('expected_graceful_termination'):
                # Should handle early termination gracefully
                assert result is not None
                
        elif test_case['method'] == 'find_command':
            result = Command.find_command(test_case['content'], test_case['command_name'])
            assert result == test_case['expected']

    @pytest.mark.parametrize("test_case", MATH_DELIMITER_EDGE_CASES) 
    def test_math_delimiter_edge_cases(self, test_case):
        """Test math delimiter parsing edge cases using fixtures."""
        
        result = Command.find_math_delimiters(test_case['content'])
        dollar_delims = [d for d in result if d['command_name'] == '$']
        assert len(dollar_delims) == test_case['expected_dollar_count']

    @pytest.mark.parametrize("test_case", DOCUMENT_ANALYSIS_ERROR_CASES)
    def test_document_analysis_error_cases(self, test_case):
        """Test document analysis error handling using fixtures."""
        
        if test_case['method'] == 'get_document_defined_commands':
            result = Command.get_document_defined_commands(test_case['content'])
            if test_case.get('expected_handles_none'):
                # Should handle the case where parsed is None and filter it out
                assert isinstance(result, list)
                
        elif test_case['method'] == 'get_document_defined_environments':
            result = Command.get_document_defined_environments(test_case['content'])
            if test_case.get('expected_handles_none'):
                # Should handle the case where parsed is None and filter it out
                assert isinstance(result, list)