# File: environment.py
# Description: LaTeX environment methods
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import re
from typing import Dict, Tuple, List, Optional, Any

class Environment:
    """
    LaTeX environment methods
    """

    @staticmethod
    def find_all_begin_environments(content: str) -> List[Tuple[str, int, int]]:
        """
        Find all \\begin{environmentname} tags in the content.
        
        :param content: The LaTeX content to search
        :return: List of tuples (name, start, end) with environment name and positions
        """
        if not content or not isinstance(content, str):
            return []
        
        # Pattern to match \begin{environmentname}
        # Allows whitespace and newlines between \begin and {environmentname}
        # Captures the environment name and the full match positions
        pattern = r'\\begin\s*\{\s*([^}\s]+)\s*\}'
        
        matches = []
        for match in re.finditer(pattern, content, re.DOTALL):
            matches.append((
                match.group(1),  # name
                match.start(),   # start
                match.end()      # end
            ))
        
        return matches

    @staticmethod
    def find_all_end_environments(content: str) -> List[Tuple[str, int, int]]:
        """
        Find all \\end{environmentname} tags in the content.
        
        :param content: The LaTeX content to search
        :return: List of tuples (name, start, end) with environment name and positions
        """
        
        # Pattern to match \end{environmentname}
        # Allows whitespace and newlines between \end and {environmentname}
        # Captures the environment name and the full match positions
        pattern = r'\\end\s*\{\s*([^}\s]+)\s*\}'
        
        matches = []
        for match in re.finditer(pattern, content, re.DOTALL):
            matches.append((
                match.group(1),  # name
                match.start(),   # start
                match.end()      # end
            ))
        
        return matches

    @staticmethod
    def find_begin_environment(content: str, environment_name: str) -> List[Tuple[int, int]]:
        """
        Find all \\begin{environmentname} tags for a specific environment.
        
        :param content: The LaTeX content to search
        :param environment_name: The specific environment name to find
        :return: List of tuples (start, end) with positions
        """
        if not content or not isinstance(content, str) or not environment_name:
            return []
        
        # Escape the environment name for regex safety
        escaped_name = re.escape(environment_name)
        
        # Pattern to match \begin{specific_environment}
        # Allows whitespace and newlines between \begin and {environmentname}
        pattern = rf'\\begin\s*\{{\s*{escaped_name}\s*\}}'
        
        matches = []
        for match in re.finditer(pattern, content, re.DOTALL):
            matches.append((
                match.start(),   # start
                match.end()      # end
            ))
        
        return matches

    @staticmethod
    def find_end_environment(content: str, environment_name: str) -> List[Tuple[int, int]]:
        """
        Find all \\end{environmentname} tags for a specific environment.
        
        :param content: The LaTeX content to search
        :param environment_name: The specific environment name to find
        :return: List of tuples (start, end) with positions
        """
        
        # Escape the environment name for regex safety
        escaped_name = re.escape(environment_name)
        
        # Pattern to match \end{specific_environment}
        # Allows whitespace and newlines between \end and {environmentname}
        pattern = rf'\\end\s*\{{\s*{escaped_name}\s*\}}'
        
        matches = []
        for match in re.finditer(pattern, content, re.DOTALL):
            matches.append((
                match.start(),   # start
                match.end()      # end
            ))
        
        return matches

    @staticmethod
    def parse_environment_arguments(
        content: str, 
        environment_name: str, 
        begin_start: int, 
        begin_end: int, 
        syntax: str
    ) -> Optional[Dict[str, Any]]:
        """
        Parse environment arguments based on syntax definition.
        
        :param content: The LaTeX content buffer
        :param environment_name: Name of the environment
        :param begin_start: Start position of the \\begin{environment}
        :param begin_end: End position of the \\begin{environment}
        :param syntax: Syntax definition string (e.g., "\\begin{array}[pos]{cols}")
        :return: Dictionary with argument values and positions, or None if parsing fails
        """
        if not all([content, environment_name, syntax]) or begin_start < 0 or begin_end <= begin_start:
            return None
        
        # Parse the syntax to identify argument patterns
        syntax_args = Environment._parse_syntax_arguments(syntax, environment_name)
        if not syntax_args:
            return {
                'environment_name': environment_name,
                'complete_start': begin_start,
                'complete_end': begin_end,
                'arguments': {}
            }
        
        # Start parsing from the end of \begin{environment}
        parse_position = begin_end
        parsed_args = {}
        current_complete_end = begin_end
        
        # Parse each argument according to syntax
        for arg_info in syntax_args:
            arg_type = arg_info['type']  # 'optional' or 'required'
            arg_name = arg_info['name']
            
            # Skip whitespace
            while parse_position < len(content) and content[parse_position].isspace():
                parse_position += 1
            
            if parse_position >= len(content):
                break
                
            if arg_type == 'optional':
                # Look for optional argument [arg]
                if content[parse_position] == '[':
                    arg_result = Environment._parse_bracket_argument(content, parse_position)
                    if arg_result:
                        parsed_args[arg_name] = {
                            'value': arg_result['value'],
                            'start': arg_result['start'],
                            'end': arg_result['end'],
                            'type': 'optional'
                        }
                        parse_position = arg_result['end']
                        current_complete_end = arg_result['end']
                # Optional arguments can be skipped, so continue to next argument
                
            elif arg_type == 'required':
                # Look for required argument {arg}
                if content[parse_position] == '{':
                    arg_result = Environment._parse_brace_argument(content, parse_position)
                    if arg_result:
                        parsed_args[arg_name] = {
                            'value': arg_result['value'],
                            'start': arg_result['start'],
                            'end': arg_result['end'],
                            'type': 'required'
                        }
                        parse_position = arg_result['end']
                        current_complete_end = arg_result['end']
                    else:
                        # Required argument not found - parsing failed
                        break
                else:
                    # Required argument not found - parsing failed
                    break
            else:
                raise ValueError(f'{arg_type} is not required or optional')
        
        return {
            'environment_name': environment_name,
            'complete_start': begin_start,
            'complete_end': current_complete_end,
            'arguments': parsed_args
        }

    @staticmethod
    def _parse_syntax_arguments(syntax: str, environment_name: str) -> List[Dict[str, str]]:
        """
        Parse the syntax string to identify argument patterns.
        
        :param syntax: Syntax definition (e.g., "\\begin{array}[pos]{cols}")
        :param environment_name: Name of the environment
        :return: List of argument info dictionaries
        """
        
        # Remove the \begin{environment_name} part to focus on arguments
        escaped_name = re.escape(environment_name)
        pattern = rf'\\begin\{{\s*{escaped_name}\s*\}}'
        remaining_syntax = re.sub(pattern, '', syntax)
        
        arguments = []
        
        # Find optional arguments [arg_name]
        optional_pattern = r'\[([^\]]+)\]'
        for match in re.finditer(optional_pattern, remaining_syntax):
            arguments.append({
                'type': 'optional',
                'name': match.group(1),
                'position': match.start()
            })
        
        # Find required arguments {arg_name}
        required_pattern = r'\{([^}]+)\}'
        for match in re.finditer(required_pattern, remaining_syntax):
            arguments.append({
                'type': 'required',
                'name': match.group(1),
                'position': match.start()
            })
        
        # Sort by position to maintain order
        arguments.sort(key=lambda x: x['position'])
        
        return arguments

    @staticmethod
    def _parse_bracket_argument(content: str, start_pos: int) -> Optional[Dict[str, Any]]:
        """
        Parse an optional argument starting with '['.
        
        :param content: The content buffer
        :param start_pos: Position of the opening '['
        :return: Dictionary with value and positions, or None if parsing fails
        """
        if start_pos >= len(content) or content[start_pos] != '[':
            return None
        
        bracket_count = 0
        pos = start_pos
        
        while pos < len(content):
            char = content[pos]
            if char == '[':
                bracket_count += 1
            elif char == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    # Found matching closing bracket
                    value = content[start_pos + 1:pos]
                    return {
                        'value': value,
                        'start': start_pos,
                        'end': pos + 1
                    }
            pos += 1
        
        # No matching closing bracket found
        return None

    @staticmethod
    def _parse_brace_argument(content: str, start_pos: int) -> Optional[Dict[str, Any]]:
        """
        Parse a required argument starting with '{'.
        
        :param content: The content buffer
        :param start_pos: Position of the opening '{'
        :return: Dictionary with value and positions, or None if parsing fails
        """
        if start_pos >= len(content) or content[start_pos] != '{':
            return None
        
        brace_count = 0
        pos = start_pos
        
        while pos < len(content):
            char = content[pos]
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    # Found matching closing brace
                    value = content[start_pos + 1:pos]
                    return {
                        'value': value,
                        'start': start_pos,
                        'end': pos + 1
                    }
            pos += 1
        
        # No matching closing brace found
        return None
