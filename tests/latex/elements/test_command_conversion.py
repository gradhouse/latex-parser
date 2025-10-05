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
    ENVIRONMENT_CONVERSION_ERROR_TESTS
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
        assert 'syntax' in result
        assert 'implementation' in result
        assert 'default' in result
        
        # Verify value types
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