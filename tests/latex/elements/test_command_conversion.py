# File: test_command_conversion.py
# Description: Unit tests for command and environment definition conversion methods
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import pytest
from typing import Dict, Optional

from src.latex_parser.latex.elements.command import Command
from tests.latex.fixtures.command_conversion_test_cases import (
    COMMAND_CONVERSION_BASIC_TESTS,
    COMMAND_CONVERSION_EDGE_TESTS,
    COMMAND_CONVERSION_ERROR_TESTS,
    ENVIRONMENT_CONVERSION_BASIC_TESTS,
    ENVIRONMENT_CONVERSION_EDGE_TESTS,
    ENVIRONMENT_CONVERSION_ERROR_TESTS,
    COMMAND_APPLICATION_BASIC_TESTS,
    COMMAND_APPLICATION_EDGE_TESTS,
    COMMAND_APPLICATION_ERROR_TESTS,
    COMMAND_APPLICATION_ADDITIONAL_ERROR_TESTS,
    COMMAND_APPLICATION_COVERAGE_TESTS,
    COMMAND_APPLICATION_COVERAGE_SPECIFIC_TESTS
)


class TestCommandConversion:
    """Test cases for Command._convert_command_definition_to_syntax method."""

    @pytest.mark.parametrize('test_case', COMMAND_CONVERSION_BASIC_TESTS)
    def test_convert_command_definition_to_syntax_basic(self, test_case: Dict):
        """Test basic command definition conversion scenarios."""
        result = Command._convert_command_definition_to_syntax(test_case['input'])
        
        assert result == test_case['expected'], (
            f"Failed for {test_case['description']}: "
            f"expected {test_case['expected']}, got {result}"
        )
    
    @pytest.mark.parametrize('test_case', COMMAND_CONVERSION_EDGE_TESTS)
    def test_convert_command_definition_to_syntax_edge_cases(self, test_case: Dict):
        """Test edge cases for command definition conversion."""
        result = Command._convert_command_definition_to_syntax(test_case['input'])
        
        assert result == test_case['expected'], (
            f"Failed for {test_case['description']}: "
            f"expected {test_case['expected']}, got {result}"
        )
    
    @pytest.mark.parametrize('test_case', COMMAND_CONVERSION_ERROR_TESTS)
    def test_convert_command_definition_to_syntax_error_handling(self, test_case: Dict):
        """Test error handling in command definition conversion."""
        with pytest.raises(test_case['should_raise']) as exc_info:
            Command._convert_command_definition_to_syntax(test_case['input'])
        
        assert test_case['expected_message'] in str(exc_info.value), (
            f"Failed for {test_case['description']}: "
            f"expected message containing '{test_case['expected_message']}', "
            f"got '{str(exc_info.value)}'"
        )
    
    def test_convert_command_definition_to_syntax_return_type(self):
        """Test that the return type is correctly typed as Dict[str, Optional[str]]."""
        test_input = {
            'arguments': {
                'cmd': {'value': '\\test'},
                'definition': {'value': 'test content'}
            }
        }
        
        result = Command._convert_command_definition_to_syntax(test_input)
        
        # Verify return type structure
        assert isinstance(result, dict)
        assert 'command_name' in result
        assert 'syntax' in result
        assert 'implementation' in result
        assert 'default' in result
        
        # Verify value types
        assert isinstance(result['command_name'], str)
        assert isinstance(result['syntax'], str)
        assert isinstance(result['implementation'], str)
        assert result['default'] is None or isinstance(result['default'], str)
    
    def test_convert_command_definition_with_default_value_type(self):
        """Test that default values are correctly handled as strings or None."""
        test_input = {
            'arguments': {
                'cmd': {'value': '\\test'},
                'nargs': {'value': '1'},
                'default': {'value': 'default_value'},
                'definition': {'value': 'test content #1'}
            }
        }
        
        result = Command._convert_command_definition_to_syntax(test_input)
        
        assert result['default'] == 'default_value'
        assert isinstance(result['default'], str)


class TestEnvironmentConversion:
    """Test cases for Command._convert_environment_definition_to_syntax method."""

    @pytest.mark.parametrize('test_case', ENVIRONMENT_CONVERSION_BASIC_TESTS)
    def test_convert_environment_definition_to_syntax_basic(self, test_case: Dict):
        """Test basic environment definition conversion scenarios."""
        result = Command._convert_environment_definition_to_syntax(test_case['input'])
        
        assert result == test_case['expected'], (
            f"Failed for {test_case['description']}: "
            f"expected {test_case['expected']}, got {result}"
        )
    
    @pytest.mark.parametrize('test_case', ENVIRONMENT_CONVERSION_EDGE_TESTS)
    def test_convert_environment_definition_to_syntax_edge_cases(self, test_case: Dict):
        """Test edge cases for environment definition conversion."""
        result = Command._convert_environment_definition_to_syntax(test_case['input'])
        
        assert result == test_case['expected'], (
            f"Failed for {test_case['description']}: "
            f"expected {test_case['expected']}, got {result}"
        )
    
    @pytest.mark.parametrize('test_case', ENVIRONMENT_CONVERSION_ERROR_TESTS)
    def test_convert_environment_definition_to_syntax_error_handling(self, test_case: Dict):
        """Test error handling in environment definition conversion."""
        with pytest.raises(test_case['should_raise']) as exc_info:
            Command._convert_environment_definition_to_syntax(test_case['input'])
        
        assert test_case['expected_message'] in str(exc_info.value), (
            f"Failed for {test_case['description']}: "
            f"expected message containing '{test_case['expected_message']}', "
            f"got '{str(exc_info.value)}'"
        )
    
    def test_convert_environment_definition_to_syntax_return_type(self):
        """Test that the return type is correctly typed as Dict[str, Optional[str]]."""
        test_input = {
            'arguments': {
                'name': {'value': 'test'},
                'begin_definition': {'value': 'begin content'},
                'end_definition': {'value': 'end content'}
            }
        }
        
        result = Command._convert_environment_definition_to_syntax(test_input)
        
        # Verify return type structure
        assert isinstance(result, dict)
        assert 'syntax' in result
        assert 'begin_implementation' in result
        assert 'end_implementation' in result
        assert 'default' in result
        
        # Verify value types
        assert isinstance(result['syntax'], str)
        assert isinstance(result['begin_implementation'], str)
        assert isinstance(result['end_implementation'], str)
        assert result['default'] is None or isinstance(result['default'], str)
    
    def test_convert_environment_definition_with_default_value_type(self):
        """Test that default values are correctly handled as strings or None."""
        test_input = {
            'arguments': {
                'name': {'value': 'test'},
                'nargs': {'value': '1'},
                'default': {'value': 'default_value'},
                'begin_definition': {'value': 'begin content #1'},
                'end_definition': {'value': 'end content'}
            }
        }
        
        result = Command._convert_environment_definition_to_syntax(test_input)
        
        assert result['default'] == 'default_value'
        assert isinstance(result['default'], str)


class TestCommandConversionIntegration:
    """Integration tests combining both conversion methods."""
    
    def test_command_and_environment_conversion_consistency(self):
        """Test that command and environment conversions follow consistent patterns."""
        # Test command with parameters
        command_input = {
            'arguments': {
                'cmd': {'value': '\\testcmd'},
                'nargs': {'value': '2'},
                'default': {'value': 'cmd_default'},
                'definition': {'value': 'Command: #1, #2'}
            }
        }
        
        # Test environment with same parameter structure
        env_input = {
            'arguments': {
                'name': {'value': 'testenv'},
                'nargs': {'value': '2'},
                'default': {'value': 'env_default'},
                'begin_definition': {'value': 'Begin: #1, #2'},
                'end_definition': {'value': 'End environment'}
            }
        }
        
        cmd_result = Command._convert_command_definition_to_syntax(command_input)
        env_result = Command._convert_environment_definition_to_syntax(env_input)
        
        # Both should have same parameter structure in syntax
        assert cmd_result['syntax'] == '\\testcmd[#1]{#2}'
        assert env_result['syntax'] == '\\begin{testenv}[#1]{#2}'
        
        # Both should preserve default values
        assert cmd_result['default'] == 'cmd_default'
        assert env_result['default'] == 'env_default'
    
    def test_parameter_numbering_consistency(self):
        """Test that parameter numbering is consistent across both methods."""
        # Test with multiple parameters
        for num_args in range(1, 6):  # Test 1-5 arguments
            cmd_input = {
                'arguments': {
                    'cmd': {'value': f'\\cmd{num_args}'},
                    'nargs': {'value': str(num_args)},
                    'definition': {'value': f'Cmd with {num_args} args'}
                }
            }
            
            env_input = {
                'arguments': {
                    'name': {'value': f'env{num_args}'},
                    'nargs': {'value': str(num_args)},
                    'begin_definition': {'value': f'Env begin with {num_args} args'},
                    'end_definition': {'value': 'End'}
                }
            }
            
            cmd_result = Command._convert_command_definition_to_syntax(cmd_input)
            env_result = Command._convert_environment_definition_to_syntax(env_input)
            
            # Extract parameter parts from syntax
            cmd_syntax = cmd_result['syntax']
            env_syntax = env_result['syntax']
            assert cmd_syntax is not None and env_syntax is not None
            
            cmd_params = cmd_syntax.replace(f'\\cmd{num_args}', '')
            env_params = env_syntax.replace(f'\\begin{{env{num_args}}}', '')
            
            # Parameter structure should be identical
            assert cmd_params == env_params, (
                f"Parameter structure mismatch for {num_args} args: "
                f"cmd='{cmd_params}', env='{env_params}'"
            )


class TestCommandApplication:
    """Test cases for Command._apply_command_definition method."""

    @pytest.mark.parametrize('test_case', COMMAND_APPLICATION_BASIC_TESTS)
    def test_apply_command_definition_basic(self, test_case: Dict):
        """Test basic command application scenarios."""
        result = Command._apply_command_definition(
            test_case['command_definition'], 
            test_case['parsed_arguments']
        )
        
        assert result == test_case['expected'], (
            f"Failed for {test_case['description']}: "
            f"expected '{test_case['expected']}', got '{result}'"
        )
    
    @pytest.mark.parametrize('test_case', COMMAND_APPLICATION_EDGE_TESTS)
    def test_apply_command_definition_edge_cases(self, test_case: Dict):
        """Test edge cases for command application."""
        result = Command._apply_command_definition(
            test_case['command_definition'], 
            test_case['parsed_arguments']
        )
        
        assert result == test_case['expected'], (
            f"Failed for {test_case['description']}: "
            f"expected '{test_case['expected']}', got '{result}'"
        )
    
    @pytest.mark.parametrize('test_case', COMMAND_APPLICATION_ERROR_TESTS)
    def test_apply_command_definition_error_handling(self, test_case: Dict):
        """Test error handling in command application."""
        with pytest.raises(test_case['should_raise']) as exc_info:
            Command._apply_command_definition(
                test_case['command_definition'], 
                test_case['parsed_arguments']
            )
        
        assert test_case['expected_message'] in str(exc_info.value), (
            f"Failed for {test_case['description']}: "
            f"expected message containing '{test_case['expected_message']}', "
            f"got '{str(exc_info.value)}'"
        )
    
    @pytest.mark.parametrize('test_case', COMMAND_APPLICATION_ADDITIONAL_ERROR_TESTS)
    def test_apply_command_definition_additional_error_handling(self, test_case: Dict):
        """Test additional error handling scenarios in command application."""
        with pytest.raises(test_case['should_raise']) as exc_info:
            Command._apply_command_definition(
                test_case['command_definition'], 
                test_case['parsed_arguments']
            )
        
        assert test_case['expected_message'] in str(exc_info.value), (
            f"Failed for {test_case['description']}: "
            f"expected message containing '{test_case['expected_message']}', "
            f"got '{str(exc_info.value)}'"
        )
    
    def test_apply_command_definition_return_type(self):
        """Test that the method returns a string."""
        command_def = {
            'command_name': '\\test',
            'syntax': '\\test{#1}',
            'implementation': 'Hello #1',
            'default': None
        }
        parsed_args = {
            'command_name': '\\test',
            'arguments': {
                '#1': {'value': 'World', 'type': 'required'}
            }
        }
        
        result = Command._apply_command_definition(command_def, parsed_args)
        
        assert isinstance(result, str)
        assert result == 'Hello World'
    
    def test_apply_command_definition_multiple_parameter_instances(self):
        """Test that parameters appearing multiple times in implementation are all replaced."""
        command_def = {
            'command_name': '\\repeat',
            'syntax': '\\repeat{#1}',
            'implementation': '#1 and #1 again, plus more #1',
            'default': None
        }
        parsed_args = {
            'command_name': '\\repeat',
            'arguments': {
                '#1': {'value': 'test', 'type': 'required'}
            }
        }
        
        result = Command._apply_command_definition(command_def, parsed_args)
        
        assert result == 'test and test again, plus more test'
        assert '#1' not in result  # Ensure all parameters were replaced
    
    def test_apply_command_definition_parameter_parsing_edge_cases(self):
        """Test edge cases in parameter parsing within syntax."""
        # Test with syntax that has parameters in different contexts
        command_def = {
            'command_name': '\\complex',
            'syntax': '\\complex[#1]{#2}[#3]',
            'implementation': 'First: #1, Second: #2, Third: #3',
            'default': None
        }
        parsed_args = {
            'command_name': '\\complex',
            'arguments': {
                '#1': {'value': 'opt1', 'type': 'optional'},
                '#2': {'value': 'req1', 'type': 'required'},
                '#3': {'value': 'opt2', 'type': 'optional'}
            }
        }
        
        result = Command._apply_command_definition(command_def, parsed_args)
        
        assert result == 'First: opt1, Second: req1, Third: opt2'
    
    def test_apply_command_definition_no_parameters_in_syntax(self):
        """Test command with implementation that has no parameter placeholders."""
        command_def = {
            'command_name': '\\simple',
            'syntax': '\\simple',
            'implementation': 'Just plain text with no parameters',
            'default': None
        }
        parsed_args = {
            'command_name': '\\simple',
            'arguments': {}
        }
        
        result = Command._apply_command_definition(command_def, parsed_args)
        
        assert result == 'Just plain text with no parameters'
    
    def test_apply_command_definition_empty_implementation(self):
        """Test command with empty implementation."""
        command_def = {
            'command_name': '\\empty',
            'syntax': '\\empty{#1}',
            'implementation': '',
            'default': None
        }
        parsed_args = {
            'command_name': '\\empty',
            'arguments': {
                '#1': {'value': 'anything', 'type': 'required'}
            }
        }
        
        result = Command._apply_command_definition(command_def, parsed_args)
        
        assert result == ''


    @pytest.mark.parametrize('test_case', COMMAND_APPLICATION_COVERAGE_TESTS)
    def test_apply_command_definition_coverage_tests(self, test_case: Dict):
        """Test additional edge cases for comprehensive coverage."""
        result = Command._apply_command_definition(
            test_case['command_definition'], 
            test_case['parsed_arguments']
        )
        
        assert result == test_case['expected'], (
            f"Failed for {test_case['description']}: "
            f"expected '{test_case['expected']}', got '{result}'"
        )

    @pytest.mark.parametrize('test_case', COMMAND_APPLICATION_COVERAGE_SPECIFIC_TESTS)
    def test_apply_command_definition_coverage_specific(self, test_case: Dict):
        """Test specific coverage cases to achieve 100% coverage"""
        # These tests specifically target lines 1374->1377, 1434 in command.py
        command_syntax = test_case['command_definition']
        args_structure = test_case['parsed_arguments']
        expected_or_error = test_case['expected']
        
        if isinstance(expected_or_error, str) and expected_or_error.startswith("Error:"):
            with pytest.raises(ValueError, match=expected_or_error.replace("Error: ", "")):
                Command._apply_command_definition(command_syntax, args_structure)
        else:
            result = Command._apply_command_definition(command_syntax, args_structure)
            assert result == expected_or_error


class TestCommandConversionInternalEdgeCases:
    """Test edge cases in internal helper methods for complete coverage."""
    
    def test_convert_command_definition_type_validation(self):
        """Test type validation for command definition fields."""
        from typing import cast, Any, Dict, Optional
        
        # Test with integer command_name (should raise ValueError)
        with pytest.raises(ValueError, match="Command name must be a string"):
            invalid_def = cast(Dict[str, Optional[str]], {'command_name': 123, 'syntax': '\\test', 'implementation': 'test'})
            Command._apply_command_definition(
                invalid_def,
                {'arguments': {}}
            )
        
        # Test with integer syntax (should raise ValueError)
        with pytest.raises(ValueError, match="Syntax must be a string"):
            invalid_def = cast(Dict[str, Optional[str]], {'command_name': '\\test', 'syntax': 456, 'implementation': 'test'})
            Command._apply_command_definition(
                invalid_def,
                {'arguments': {}}
            )
        
        # Test with integer implementation (should raise ValueError)
        with pytest.raises(ValueError, match="Implementation must be a string"):
            invalid_def = cast(Dict[str, Optional[str]], {'command_name': '\\test', 'syntax': '\\test', 'implementation': 789})
            Command._apply_command_definition(
                invalid_def,
                {'arguments': {}}
            )
    
    def test_parameter_parsing_with_no_matches(self):
        """Test parameter parsing when syntax has no parameter patterns."""
        from typing import cast, Dict, Optional
        
        command_def = cast(Dict[str, Optional[str]], {
            'command_name': '\\noparams',
            'syntax': '\\noparams',  # No #1, #2, etc.
            'implementation': 'Just text',
            'default': None
        })
        parsed_args = {
            'command_name': '\\noparams',
            'arguments': {}
        }
        
        result = Command._apply_command_definition(command_def, parsed_args)
        assert result == 'Just text'
    
    def test_parameter_type_detection_edge_cases(self):
        """Test edge cases in parameter type detection (optional vs required)."""
        from typing import cast, Dict, Optional
        
        # Test parameter detection when parameter is at start of syntax
        # Current behavior: parameters at position 0 are not detected due to start_pos > 0 check
        command_def = cast(Dict[str, Optional[str]], {
            'command_name': '\\test',
            'syntax': '#1{content}',  # Parameter at position 0
            'implementation': '#1 and some content',
            'default': None
        })
        parsed_args = {
            'command_name': '\\test',
            'arguments': {}  # No arguments because parameter at position 0 isn't detected
        }
        
        # This tests the current behavior - parameter at position 0 is not detected
        result = Command._apply_command_definition(command_def, parsed_args)
        assert result == '#1 and some content'  # #1 is not replaced because it's not in expected_params
        
        # Test a more typical case where parameter has prefix
        command_def2 = cast(Dict[str, Optional[str]], {
            'command_name': '\\test',
            'syntax': '\\test{#1}',  # Parameter with proper prefix
            'implementation': 'Value: #1',
            'default': None
        })
        parsed_args2 = {
            'command_name': '\\test',
            'arguments': {
                '#1': {'value': 'hello', 'type': 'required'}
            }
        }
        
        result2 = Command._apply_command_definition(command_def2, parsed_args2)
        assert result2 == 'Value: hello'
    
    def test_default_value_usage_edge_cases(self):
        """Test specific edge cases in default value usage."""
        from typing import cast, Dict, Optional
        
        # Test where we have exactly expected_count - 1 arguments with a default
        command_def = cast(Dict[str, Optional[str]], {
            'command_name': '\\test',
            'syntax': '\\test[#1]{#2}',
            'implementation': 'Hello #1, #2',
            'default': 'World'
        })
        parsed_args = {
            'command_name': '\\test',
            'arguments': {
                '#2': {'value': 'there', 'type': 'required'}
            }
        }
        
        result = Command._apply_command_definition(command_def, parsed_args)
        assert result == 'Hello World, there'
    """Integration tests for command definition and application workflow."""
    
    def test_full_workflow_with_real_commands(self):
        """Test the complete workflow from LaTeX content to applied commands."""
        # Define LaTeX content with command definitions
        content = r'''
        \newcommand{\greet}[2][World]{Hello #1, welcome #2}
        \newcommand{\bold}[1]{\textbf{#1}}
        '''
        
        # Get document defined commands
        commands = Command.get_document_defined_commands(content)
        assert len(commands) == 2
        
        # Convert to syntax definitions
        greet_def = Command._convert_command_definition_to_syntax(commands[0])
        bold_def = Command._convert_command_definition_to_syntax(commands[1])
        
        # Test applying the greet command with default
        greet_usage = r'\greet{John}'
        greet_syntax = greet_def['syntax']
        assert greet_syntax is not None
        
        parsed_greet = Command.parse_arguments(
            greet_usage, r'\greet', 0, 6, greet_syntax, False
        )
        assert parsed_greet is not None
        
        result_greet = Command._apply_command_definition(greet_def, parsed_greet)
        assert result_greet == 'Hello World, welcome John'
        
        # Test applying the bold command
        bold_usage = r'\bold{important text}'
        bold_syntax = bold_def['syntax']
        assert bold_syntax is not None
        
        parsed_bold = Command.parse_arguments(
            bold_usage, r'\bold', 0, 5, bold_syntax, False
        )
        assert parsed_bold is not None
        
        result_bold = Command._apply_command_definition(bold_def, parsed_bold)
        assert result_bold == r'\textbf{important text}'