# File: test_def_command.py
# Description: Test cases for LaTeX \def command parsing using fixtures
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import pytest
import sys
import os
from latex_parser.latex.elements.command import Command

# Add the tests directory to the path to import fixtures
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from latex.fixtures.def_command_test_cases import (
    DEF_COMMAND_BASIC_TESTS,
    DEF_COMMAND_COMPLEX_TESTS,
    DEF_COMMAND_EDGE_TESTS,
    DEF_COMMAND_ERROR_TESTS,
    DEF_COMMAND_INTEGRATION_TESTS,
    DEF_COMMAND_SPECIAL_TESTS
)


class TestDefCommandParsing:
    r"""Test class for TeX \def command parsing functionality using fixtures."""

    @pytest.mark.parametrize("test_case", DEF_COMMAND_SPECIAL_TESTS)
    def test_def_command_special_handling_in_parse_arguments(self, test_case):
        r"""Test that \def commands are handled specially in parse_arguments."""
        result = Command.parse_arguments(
            test_case['content'], 
            test_case['command_name'], 
            test_case['start_pos'], 
            test_case['end_pos'], 
            test_case['syntax'], 
            test_case['is_environment']
        )
        
        assert result is not None
        assert 'arguments' in result
        assert 'pattern' in result['arguments']
        assert 'replacement' in result['arguments']
        
        # Check key fields from expected
        expected = test_case['expected']
        assert result['arguments']['pattern']['value'] == expected['arguments']['pattern']['value']
        assert result['arguments']['replacement']['value'] == expected['arguments']['replacement']['value']

    @pytest.mark.parametrize("test_case", DEF_COMMAND_BASIC_TESTS)
    def test_def_command_basic_parsing(self, test_case):
        r"""Test basic \def command parsing cases."""
        result = Command.parse_def_command(test_case['content'], test_case['start_pos'], test_case['end_pos'])
        
        if test_case['expected'] is None:
            assert result is None
        else:
            assert result is not None
            expected = test_case['expected']
            
            # Check complete structure for full test cases
            if 'command_name' in expected:
                assert result == expected
            else:
                # Check key arguments for partial test cases
                assert result['arguments']['pattern']['value'] == expected['arguments']['pattern']['value']
                assert result['arguments']['replacement']['value'] == expected['arguments']['replacement']['value']

    @pytest.mark.parametrize("test_case", DEF_COMMAND_COMPLEX_TESTS)
    def test_def_command_complex_patterns(self, test_case):
        r"""Test complex \def command patterns with multiple parameters and delimiters."""
        result = Command.parse_def_command(test_case['content'], test_case['start_pos'], test_case['end_pos'])
        
        assert result is not None
        expected = test_case['expected']
        
        # Verify pattern structure
        pattern = result['arguments']['pattern']
        expected_pattern = expected['arguments']['pattern']
        
        assert pattern['value'] == expected_pattern['value']
        assert len(pattern['parameters']) == len(expected_pattern['parameters'])
        assert len(pattern['delimiters']) == len(expected_pattern['delimiters'])
        
        # Verify parameters
        for i, param in enumerate(expected_pattern['parameters']):
            assert pattern['parameters'][i]['number'] == param['number']
            assert pattern['parameters'][i]['text'] == param['text']
        
        # Verify delimiters
        for i, delimiter in enumerate(expected_pattern['delimiters']):
            result_delimiter = pattern['delimiters'][i]
            assert result_delimiter['text'] == delimiter['text']
            if 'before_param' in delimiter:
                assert result_delimiter['before_param'] == delimiter['before_param']
            if 'after_last_param' in delimiter:
                assert result_delimiter['after_last_param'] == delimiter['after_last_param']

    @pytest.mark.parametrize("test_case", DEF_COMMAND_EDGE_TESTS)
    def test_def_command_edge_cases(self, test_case):
        r"""Test edge cases for \def command parsing."""
        result = Command.parse_def_command(test_case['content'], test_case['start_pos'], test_case['end_pos'])
        
        if test_case['expected'] is None:
            assert result is None
        else:
            assert result is not None
            expected = test_case['expected']
            
            # Check pattern and replacement
            assert result['arguments']['pattern']['value'] == expected['arguments']['pattern']['value']
            assert result['arguments']['replacement']['value'] == expected['arguments']['replacement']['value']
            
            # Check parameters and delimiters counts for edge cases
            if 'parameters' in expected['arguments']['pattern']:
                assert len(result['arguments']['pattern']['parameters']) == len(expected['arguments']['pattern']['parameters'])
            if 'delimiters' in expected['arguments']['pattern']:
                assert len(result['arguments']['pattern']['delimiters']) == len(expected['arguments']['pattern']['delimiters'])

    @pytest.mark.parametrize("test_case", DEF_COMMAND_ERROR_TESTS)
    def test_def_command_error_cases(self, test_case):
        r"""Test error cases for \def command parsing."""
        result = Command.parse_def_command(test_case['content'], test_case['start_pos'], test_case['end_pos'])
        assert result == test_case['expected']

    @pytest.mark.parametrize("test_case", DEF_COMMAND_INTEGRATION_TESTS)
    def test_def_command_integration_with_parse_command_arguments(self, test_case):
        r"""Test integration between parse_command_arguments and def parsing."""
        result = Command.parse_command_arguments(
            test_case['content'], 
            test_case['command_name'], 
            test_case['start_pos'], 
            test_case['end_pos'], 
            test_case['syntax']
        )
        
        assert result is not None
        assert 'arguments' in result
        
        expected = test_case['expected']
        assert result['arguments']['pattern']['value'] == expected['arguments']['pattern']['value']
        assert result['arguments']['replacement']['value'] == expected['arguments']['replacement']['value']

    def test_def_command_not_environment(self):
        r"""Test that \def is not processed when is_environment=True."""
        content = r'\def\mycommand{replacement}'
        
        # With is_environment=True, should not trigger def parsing but will fail
        # because the syntax doesn't match environment pattern
        with pytest.raises(ValueError, match="doesn't match expected pattern for environment"):
            Command.parse_arguments(
                content, r'\def', 0, 4, r'\def⟨pattern⟩{⟨replacement⟩}', is_environment=True
            )

    def test_def_command_parameter_parsing_edge_cases(self):
        r"""Test edge cases in parameter parsing."""
        # Test with parameter at end of pattern
        content = r'\def\cmd#1{replacement}'
        result = Command.parse_def_command(content, 0, 4)
        
        assert result is not None
        assert len(result['arguments']['pattern']['parameters']) == 1
        assert len(result['arguments']['pattern']['delimiters']) == 1
        assert result['arguments']['pattern']['delimiters'][0]['text'] == r'\cmd'

    def test_def_command_advanced_edge_cases(self):
        r"""Test additional edge cases for complete coverage."""
        # Test case where we need to track brace nesting properly
        # The parser should skip over balanced braces in the pattern
        # This pattern is artificial but tests the brace counting logic
        content = r'\def\mycommand{pattern}more{replacement}'
        result = Command.parse_def_command(content, 0, 4)
        
        assert result is not None
        # The first { should start replacement since brace_count == 0
        assert result['arguments']['pattern']['value'] == r'\mycommand'
        assert result['arguments']['replacement']['value'] == 'pattern'
        
        # Test case with no delimiter text between parameters
        content2 = r'\def\cmd#1#2{replacement}'
        result2 = Command.parse_def_command(content2, 0, 4)
        
        assert result2 is not None
        assert len(result2['arguments']['pattern']['parameters']) == 2
        delimiters = result2['arguments']['pattern']['delimiters']
        assert len(delimiters) == 1
        assert delimiters[0]['text'] == r'\cmd'
        
        # Test case with whitespace-only delimiter that gets stripped to empty
        content3 = r'\def\cmd#1   #2{replacement}'
        result3 = Command.parse_def_command(content3, 0, 4)
        
        assert result3 is not None
        delimiters3 = result3['arguments']['pattern']['delimiters']
        assert len(delimiters3) == 1
        assert delimiters3[0]['text'] == r'\cmd'

    def test_def_command_brace_counting_coverage(self):
        r"""Test brace counting logic to cover edge cases."""
        # Test case 1: Standard \def usage
        content1 = r'\def\mycommand{replacement}'
        result1 = Command.parse_def_command(content1, 0, 4)
        
        assert result1 is not None
        assert result1['arguments']['pattern']['value'] == r'\mycommand'
        assert result1['arguments']['replacement']['value'] == 'replacement'
        
        # Test case 2: Even with complex patterns, first { is always replacement start
        content2 = r'\def\complex#1[#2]#3{replacement}'
        result2 = Command.parse_def_command(content2, 0, 4)
        
        assert result2 is not None
        assert result2['arguments']['pattern']['value'] == r'\complex#1[#2]#3'
        assert result2['arguments']['replacement']['value'] == 'replacement'
        
        # Test case 3: What if we had no braces in pattern? Still first { wins
        content3 = r'\def\simple{replacement}'
        result3 = Command.parse_def_command(content3, 0, 4)
        
        assert result3 is not None
        assert result3['arguments']['pattern']['value'] == r'\simple'
        assert result3['arguments']['replacement']['value'] == 'replacement'

    def test_def_command_advanced_brace_counting(self):
        r"""Test to identify if brace counting logic is reachable."""
        # Analysis: The current logic has brace_count starting at 0
        # The first { when brace_count == 0 always breaks the loop
        # This means lines 411 (brace_count += 1) and 413 (brace_count -= 1) 
        # are unreachable dead code under the current implementation
        
        # Test case 1: Standard \def usage
        content1 = r'\def\mycommand{replacement}'
        result1 = Command.parse_def_command(content1, 0, 4)
        
        assert result1 is not None
        assert result1['arguments']['pattern']['value'] == r'\mycommand'
        assert result1['arguments']['replacement']['value'] == 'replacement'
        
        # Test case 2: Even with complex patterns, first { is always replacement start
        content2 = r'\def\complex#1[#2]#3{replacement}'
        result2 = Command.parse_def_command(content2, 0, 4)
        
        assert result2 is not None
        assert result2['arguments']['pattern']['value'] == r'\complex#1[#2]#3'
        assert result2['arguments']['replacement']['value'] == 'replacement'
        
        # Test case 3: What if we had no braces in pattern? Still first { wins
        content3 = r'\def\simple{replacement}'
        result3 = Command.parse_def_command(content3, 0, 4)
        
        assert result3 is not None
        assert result3['arguments']['pattern']['value'] == r'\simple'
        assert result3['arguments']['replacement']['value'] == 'replacement'

    def test_def_command_comprehensive_coverage_edge_cases(self):
        r"""Test edge cases to achieve 100% coverage of parse_def_command."""
        
        # Test case 1: Empty pattern (whitespace-only pattern that strips to empty)
        # This should trigger the false branch of "if pattern.strip():" (lines 467-471)
        content1 = '\\def   {replacement}'  # Only whitespace as pattern
        result1 = Command.parse_def_command(content1, 0, 4)
        
        assert result1 is not None
        assert len(result1['arguments']['pattern']['parameters']) == 0
        # Should have no delimiters because pattern.strip() is empty
        assert len(result1['arguments']['pattern']['delimiters']) == 0
        
        # Test case 2: Pattern with actual content to ensure true branches still work
        content2 = '\\def\\cmd#1end{replacement}'
        result2 = Command.parse_def_command(content2, 0, 4)
        
        assert result2 is not None
        delimiters2 = result2['arguments']['pattern']['delimiters']
        assert len(delimiters2) == 2
        # Should have delimiter after last parameter
        after_last_delims2 = [d for d in delimiters2 if d.get('after_last_param')]
        assert len(after_last_delims2) == 1
        assert after_last_delims2[0]['text'] == 'end'
        
        # Test case 3: Try different approaches to hit the edge case
        # The missing coverage in 460->473 might be the false branch of 'if delimiter_text:'
        # But this may be unreachable because if last_end < len(pattern) and pattern is stripped,
        # there should always be non-empty delimiter_text
        
        # Let's test a pattern that ends exactly at the parameter
        content3 = '\\def\\cmd#1{replacement}'  # No text after #1
        result3 = Command.parse_def_command(content3, 0, 4)
        
        assert result3 is not None
        delimiters3 = result3['arguments']['pattern']['delimiters']
        assert len(delimiters3) == 1  # Only '\\cmd'
        # No after_last_param delimiter should exist
        after_last_delims3 = [d for d in delimiters3 if d.get('after_last_param')]
        assert len(after_last_delims3) == 0