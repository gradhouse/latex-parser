# File: def_modernization_test_cases.py
# Description: Test cases for modernizing \def commands to \newcommand
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

"""
Test cases for \\def command modernization functionality including error cases,
conversion validation, and helper method testing.
"""

# Test cases for strict mode and unparseable content
DEF_MODERNIZATION_ERROR_CASES = [
    {
        'description': 'Strict mode with unparseable content',
        'content': r'\def\cmd',  # Missing replacement
        'strict_mode': False,
        'expected_normal': r'\def\cmd',  # Should remain unchanged in normal mode
        'strict_mode_raises': True  # Should raise ValueError in strict mode
    },
    {
        'description': 'Delimited parameters conversion failure',
        'content': r'\def\cmd#1 stop{text}',
        'expected_reason': 'Delimited parameters not supported'
    },
    {
        'description': 'Non-sequential parameters conversion failure',
        'content': r'\def\cmd#1#3{text}',
        'expected_reason': 'Non-sequential parameter numbers'
    }
]

# Test cases for can_convert_def_to_newcommand method
CAN_CONVERT_DEF_TESTS = [
    {
        'description': 'Simple def without parameters',
        'def_string': r'\def\mycommand{Hello World}',
        'expected': True
    },
    {
        'description': 'Def with sequential parameters',
        'def_string': r'\def\mycommand#1#2{#1 and #2}',
        'expected': True
    },
    {
        'description': 'Def with delimited parameters',
        'def_string': r'\def\mycommand#1 stop{text}',
        'expected': False
    },
    {
        'description': 'Def with non-sequential parameters',
        'def_string': r'\def\mycommand#1#3{text}',
        'expected': False
    },
    {
        'description': 'Unparseable def command',
        'def_string': r'\def\mycommand',
        'expected': False
    },
    {
        'description': 'Def with complex nested braces',
        'def_string': r'\def\mycommand#1#2{{\bf #1} and {\it #2}}',
        'expected': True
    },
    {
        'description': 'Def with math mode content',
        'def_string': r'\def\mycommand#1{$#1^2$}',
        'expected': True
    }
]

# Test cases for get_conversion_failure_reason method
CONVERSION_FAILURE_REASON_TESTS = [
    {
        'description': 'Delimited parameters reason',
        'def_string': r'\def\cmd#1 stop{text}',
        'expected_reason': 'Delimited parameters not supported'
    },
    {
        'description': 'Non-sequential parameters reason',
        'def_string': r'\def\cmd#1#3{text}',
        'expected_reason': 'Non-sequential parameter numbers'
    },
    {
        'description': 'Unknown parsing error',
        'def_string': r'\def\cmd',  # Unparseable
        'expected_reason': 'Unknown parsing error'
    },
    {
        'description': 'Mock unknown conversion restriction',
        'def_string': 'mock_unknown_restriction',  # Special case for testing
        'expected_reason': 'Unknown conversion restriction'
    }
]

# Test cases for extract_command_name_from_pattern method
EXTRACT_COMMAND_NAME_TESTS = [
    {
        'description': 'Simple command pattern',
        'pattern': r'\mycommand',
        'expected': r'\mycommand'
    },
    {
        'description': 'Command pattern with parameters',
        'pattern': r'\mycommand#1',
        'expected': r'\mycommand'
    },
    {
        'description': 'Command pattern with multiple parameters',
        'pattern': r'\mycommand#1#2#3',
        'expected': r'\mycommand'
    },
    {
        'description': 'Command pattern with spaces',
        'pattern': r'\mycommand #1',
        'expected': r'\mycommand'
    }
]

# Test cases for convert_def_to_newcommand method
CONVERT_DEF_TO_NEWCOMMAND_TESTS = [
    {
        'description': 'Simple def without parameters',
        'def_string': r'\def\mycommand{Hello World}',
        'expected': r'\newcommand{\mycommand}{Hello World}'
    },
    {
        'description': 'Def with one parameter',
        'def_string': r'\def\mycommand#1{Hello #1}',
        'expected': r'\newcommand{\mycommand}[1]{Hello #1}'
    },
    {
        'description': 'Def with two parameters',
        'def_string': r'\def\mycommand#1#2{#1 and #2}',
        'expected': r'\newcommand{\mycommand}[2]{#1 and #2}'
    },
    {
        'description': 'Def with complex replacement text',
        'def_string': r'\def\mycommand#1#2{{\bf #1} \textit{#2}}',
        'expected': r'\newcommand{\mycommand}[2]{{\bf #1} \textit{#2}}'
    },
    {
        'description': 'Def with math content',
        'def_string': r'\def\mycommand#1{$\sum_{i=1}^{#1} i$}',
        'expected': r'\newcommand{\mycommand}[1]{$\sum_{i=1}^{#1} i$}'
    }
]

# Test cases for helper method coverage
HELPER_METHOD_COVERAGE_TESTS = [
    {
        'description': 'Extract command name with param info',
        'pattern': r'\mycommand#1',
        'param_info': {'params': [1]},  # Mock parameter info
        'expected': r'\mycommand'
    },
    {
        'description': 'Get failure reason edge cases',
        'test_cases': [
            {
                'def_string': r'\def\cmd',  # Unparseable
                'expected_reason': 'Unknown parsing error'
            }
        ]
    }
]

# Test cases for invalid input handling
INVALID_INPUT_TESTS = [
    {
        'description': 'Find all commands with empty string',
        'method': 'find_all_commands',
        'content': '',
        'expected': []
    },
    {
        'description': 'Find command with empty content',
        'method': 'find_command',
        'content': '',
        'command_name': r'\textbf',
        'expected': []
    },
    {
        'description': 'Find command with invalid command name (no backslash)',
        'method': 'find_command', 
        'content': r'\textbf{hello}',
        'command_name': 'textbf',
        'should_raise': 'ValueError',
        'expected_message': 'Command name must start with backslash'
    }
]

# Test cases for overlap and boundary conditions
BOUNDARY_CONDITION_TESTS = [
    {
        'description': 'Commands with overlapping patterns',
        'content': r'\alpha* \beta@ \gamma!',
        'expected_commands': [r'\alpha', r'\beta', r'\gamma'],
        'note': 'Should find base commands ignoring non-letter suffixes'
    }
]