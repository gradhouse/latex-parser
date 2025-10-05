# File: command_edge_cases.py
# Description: Edge case test cases for LaTeX command parsing and analysis
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

"""
Edge case test cases for command.py that test error handling, boundary conditions,
and unusual LaTeX syntax patterns that are difficult to reach through normal usage.
"""

# Test cases for argument parsing edge cases and error conditions
ARGUMENT_PARSING_EDGE_CASES = [
    {
        'description': 'Line 223: parse_arguments else branch when _parse_brace_argument returns None for required argument',
        'method': 'parse_arguments',
        'content': r'\newcommand{\test}{hello',  # Missing closing brace for definition
        'command_name': r'\newcommand',
        'start_pos': 0,
        'end_pos': 11,
        'template': r'\newcommand{cmd}[nargs][default]{definition}',
        'allow_optional': False,
        'expected_has_cmd': True,
        'expected_missing_definition': True
    },
    {
        'description': 'Line 228: parse_arguments else branch when content[parse_position] != "{" for required argument',
        'method': 'parse_arguments',
        'content': r'\newcommand{\test}hello',  # Missing { before hello for definition
        'command_name': r'\newcommand',
        'start_pos': 0,
        'end_pos': 11,
        'template': r'\newcommand{cmd}[nargs][default]{definition}',
        'allow_optional': False,
        'expected_has_cmd': True,
        'expected_missing_definition': True
    },
    {
        'description': 'Line 341: @ command startswith check in find_command for non-letter commands',
        'method': 'find_command',
        'content': r'\@123',  # @ followed by numbers
        'command_name': r'\@',
        'expected': [(0, 2)]
    },
    {
        'description': 'Line 256->241: parse_position >= len(content) branch in parse_arguments',
        'method': 'parse_arguments',
        'content': r'\textbf{',  # Starts required arg but content ends
        'command_name': r'\textbf',
        'start_pos': 0,
        'end_pos': 7,
        'template': r'\textbf{text}',
        'allow_optional': False,
        'expected_graceful_termination': True
    }
]

# Test cases for math delimiter parsing edge cases
MATH_DELIMITER_EDGE_CASES = [
    {
        'description': 'Line 557->562: Find math delimiters with escaped backslash pattern',
        'method': 'find_math_delimiters',
        'content': r'text \\\$ more',  # Three backslashes before $ = escaped
        'expected_dollar_count': 0  # Should be escaped
    }
]

# Test cases for document analysis error handling
DOCUMENT_ANALYSIS_ERROR_CASES = [
    {
        'description': 'Lines 705-706: get_document_defined_commands with None filtering',
        'method': 'get_document_defined_commands',
        'content': r'\newcommand',  # Incomplete - should result in None from parse_arguments
        'expected_handles_none': True
    },
    {
        'description': 'Lines 719-720: get_document_defined_environments with None filtering',
        'method': 'get_document_defined_environments', 
        'content': r'\newenvironment',  # Incomplete - should result in None from parse_arguments
        'expected_handles_none': True
    }
]

# Combined test cases for easy import
ALL_COMMAND_EDGE_CASES = {
    'argument_parsing': ARGUMENT_PARSING_EDGE_CASES,
    'math_delimiters': MATH_DELIMITER_EDGE_CASES,
    'document_analysis': DOCUMENT_ANALYSIS_ERROR_CASES
}