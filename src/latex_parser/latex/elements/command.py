# File: command.py
# Description: LaTeX command methods
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import re
from typing import Dict, Tuple, List, Optional, Any

class Command:
    """
    LaTeX command methods
    """

    @staticmethod
    def find_all_commands(content: str) -> List[Tuple[str, int, int]]:
        """
        Find all LaTeX commands in the content.
        
        LaTeX commands consist of:
        - \\ followed by a single non-letter (like \\@, \\!)
        - \\ followed by a string of letters (upper or lower case)
        - Optional * form after letter-based command names
        - Spaces and single end-of-line following letter commands are ignored
        
        :param content: The LaTeX content to search
        :return: List of tuples (name, start, end) with command name and positions
        """
        
        matches = []
        
        # Pattern 1: \ followed by letters, optionally followed by *
        # OR \ followed by @ and then letters, optionally followed by *
        # Captures spaces and single newline after the command
        letter_pattern = r'\\((?:@[a-zA-Z]*|[a-zA-Z]+))(\*)?(?:\s|\n(?!\n))?'
        
        for match in re.finditer(letter_pattern, content):
            command_name = '\\' + match.group(1)
            if match.group(2):  # If * is present
                command_name += '*'
            matches.append((
                command_name,    # name
                match.start(),   # start of \
                match.start() + len(match.group(1)) + (1 if match.group(2) else 0) + 1  # end after command name and optional *
            ))
        
        # Pattern 2: \ followed by a single non-letter character
        # But exclude @ when it's followed by letters (since that's handled by pattern 1)
        non_letter_pattern = r'\\([^a-zA-Z\s])(?![a-zA-Z])'
        
        for match in re.finditer(non_letter_pattern, content):
            # Check if this position was already captured by the letter pattern
            position_already_captured = any(
                existing_start <= match.start() < existing_end 
                for _, existing_start, existing_end in matches
            )
            
            if not position_already_captured:
                matches.append((
                    '\\' + match.group(1),  # name (the non-letter character with backslash)
                    match.start(),   # start of \
                    match.end()      # end after the non-letter character
                ))
        
        # Sort by position to maintain document order
        matches.sort(key=lambda x: x[1])
        return matches

    @staticmethod
    def find_command(content: str, command_name: str) -> List[Tuple[int, int]]:
        """
        Find all occurrences of a specific LaTeX command in the content.
        
        :param content: The LaTeX content to search
        :param command_name: The specific command name to find (with the backslash, e.g., '\\textbf')
        :return: List of tuples (start, end) with positions of the command
        """
        
        # Ensure command name starts with backslash
        if not command_name.startswith('\\'):
            raise ValueError(f"Command name must start with backslash, got: '{command_name}'")
        
        # Remove the backslash for processing
        command_name = command_name[1:]
        
        # Escape the command name for regex safety
        escaped_name = re.escape(command_name)
        
        # Check if this is a single non-letter command
        if len(command_name) == 1 and not command_name.isalpha():
            # For standalone @ command, make sure it's not followed by letters
            if command_name == '@':
                pattern = rf'\\{escaped_name}(?![a-zA-Z])'
            else:
                pattern = rf'\\{escaped_name}'
        else:
            # For letter-based commands (including @ commands), ensure word boundary and handle optional *
            if command_name.endswith('*'):
                # Command with * - match exactly (don't match without *)
                base_name = re.escape(command_name[:-1])
                if base_name.startswith('@'):
                    # @ command with star
                    pattern = rf'\\{base_name}\*(?![a-zA-Z])(?:\s|\n(?!\n))?'
                else:
                    # Regular letter command with star
                    pattern = rf'\\{base_name}\*(?![a-zA-Z@])(?:\s|\n(?!\n))?'
            else:
                # Regular command without star
                if command_name.startswith('@'):
                    # @ command - only followed by letters (not @)
                    pattern = rf'\\{escaped_name}(?![a-zA-Z\*])(?:\s|\n(?!\n))?'
                else:
                    # Regular letter command - not followed by letters or @
                    pattern = rf'\\{escaped_name}(?![a-zA-Z@\*])(?:\s|\n(?!\n))?'
        
        matches = []
        for match in re.finditer(pattern, content):
            # Calculate the actual end position (excluding trailing spaces/newlines for letter commands)
            if len(command_name) > 1 or command_name.isalpha() or command_name.startswith('@'):
                # For letter commands, end after the command name (and optional *)
                actual_end = match.start() + 1 + len(command_name)  # 1 for backslash + command length
            else:
                # For non-letter commands, include everything
                actual_end = match.end()
            
            matches.append((
                match.start(),   # start
                actual_end       # end
            ))
        
        return matches

    @staticmethod
    def parse_syntax_arguments(syntax: str, command_name: str, is_environment: bool = False) -> List[Dict[str, str]]:
        """
        Parse the syntax string to identify argument patterns for any LaTeX command/environment.
        
        :param syntax: Syntax definition (e.g., "\\textbf{text}" or "\\begin{array}[pos]{cols}")
        :param command_name: Name of the command or environment
        :param is_environment: True if parsing environment syntax, False for command syntax
        :return: List of argument info dictionaries
        """
        
        # Normalize command name - remove leading backslash if present
        clean_command_name = command_name[1:] if command_name.startswith('\\') else command_name
        
        # Construct expected start pattern
        if is_environment:
            expected_start = f"\\begin{{{clean_command_name}}}"
        else:
            expected_start = f"\\{clean_command_name}"
        
        # Validate syntax matches expected pattern
        if not syntax.startswith(expected_start):
            raise ValueError(f"Syntax '{syntax}' doesn't match expected pattern for {'environment' if is_environment else 'command'} '{command_name}'")
        
        # Extract remaining arguments part
        remaining_syntax = syntax[len(expected_start):]
        
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
    def parse_arguments(
        content: str, 
        command_name: str, 
        start_pos: int, 
        end_pos: int, 
        syntax: str, 
        is_environment: bool = False
    ) -> Optional[Dict[str, Any]]:
        """
        Core argument parsing logic for commands and environments.
        
        :param content: The LaTeX content to parse
        :param command_name: Name of the command or environment
        :param start_pos: Start position of the command/environment
        :param end_pos: End position of the command/environment name
        :param syntax: Syntax definition for the command/environment
        :param is_environment: True if parsing environment, False for command
        :return: Dictionary with parsed arguments and position info, or None if empty args
        """
        
        # Parse the syntax to identify argument patterns
        syntax_args = Command.parse_syntax_arguments(syntax, command_name, is_environment)
        if not syntax_args:
            return {
                f"{'environment' if is_environment else 'command'}_name": command_name,
                'complete_start': start_pos,
                'complete_end': end_pos,
                'arguments': {}
            }
        
        # Start parsing from the end of command/environment name
        parse_position = end_pos
        parsed_args = {}
        current_complete_end = end_pos
        
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
                    arg_result = Command._parse_bracket_argument(content, parse_position)
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
                    arg_result = Command._parse_brace_argument(content, parse_position)
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
            f"{'environment' if is_environment else 'command'}_name": command_name,
            'complete_start': start_pos,
            'complete_end': current_complete_end,
            'arguments': parsed_args
        }

    @staticmethod
    def parse_command_arguments(
        content: str, 
        command_name: str, 
        command_start: int, 
        command_end: int, 
        syntax: str
    ) -> Optional[Dict[str, Any]]:
        """
        Parse arguments for a specific LaTeX command.
        
        :param content: The LaTeX content to parse
        :param command_name: Name of the command (without backslash)
        :param command_start: Start position of the command (including backslash)
        :param command_end: End position of the command name
        :param syntax: Syntax definition for the command (e.g., "\\textbf{text}")
        :return: Dictionary with parsed arguments and position info, or None if empty args
        """
        return Command.parse_arguments(content, command_name, command_start, command_end, syntax, is_environment=False)

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
