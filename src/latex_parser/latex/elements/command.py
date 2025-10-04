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
        
        # Special handling for TeX \def commands
        if not is_environment and command_name == '\\def':
            return Command.parse_def_command(content, start_pos, end_pos)
        
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

    @staticmethod
    def parse_def_command(content: str, command_start: int, command_end: int) -> Optional[Dict[str, Any]]:
        """
        Parse TeX \\def command with flexible parameter pattern matching.
        
        \\def syntax: \\def⟨pattern⟩{⟨replacement⟩}
        Examples:
        - \\def\\mycommand{replacement}
        - \\def\\mycommand#1{replacement with #1}
        - \\def\\mycommand#1#2{replacement with #1 and #2}  
        - \\def\\mycommand#1 stop{replacement} (delimited parameter)
        - \\def\\mycommand#1[#2]#3{replacement} (complex pattern)
        
        :param content: The LaTeX content to parse
        :param command_start: Start position of \\def command
        :param command_end: End position of \\def command name
        :return: Dictionary with parsed pattern and replacement, or None if parsing fails
        """
        if command_end >= len(content):
            return None
        
        # Skip whitespace after \\def
        pos = command_end
        while pos < len(content) and content[pos].isspace():
            pos += 1
        
        if pos >= len(content):
            return None
        
        # Parse the pattern part (everything before the replacement braces)
        # In TeX \def, we need to find the first unmatched { which starts the replacement
        pattern_start = pos
        pattern_end = None
        
        # Find the replacement braces - first { that's not part of balanced pairs in pattern
        while pos < len(content):
            char = content[pos]
            
            if char == '{':
                # In standard TeX \def, the first { starts the replacement
                # More complex brace handling could be added here if needed
                pattern_end = pos
                break
                
            pos += 1
        
        if pattern_end is None:
            return None
        
        # Extract pattern
        pattern = content[pattern_start:pattern_end].strip()
        
        # Parse the replacement braces {replacement}
        replacement_result = Command._parse_brace_argument(content, pattern_end)
        if not replacement_result:
            return None
        
        # Parse parameter information from pattern using more robust approach
        parameters = []
        param_pattern = r'#(\d+)'
        
        for match in re.finditer(param_pattern, pattern):
            param_num = int(match.group(1))
            parameters.append({
                'number': param_num,
                'position': match.start(),
                'text': match.group(0)
            })
        
        # Sort parameters by position to ensure correct order
        parameters.sort(key=lambda p: p['position'])
        
        # Find delimited patterns (text between parameters and after last parameter)
        delimiters = []
        if parameters:
            # Check for delimiters between parameters and after last parameter
            last_end = 0
            for param in parameters:
                # Check for delimiter before this parameter
                if param['position'] > last_end:
                    delimiter_text = pattern[last_end:param['position']].strip()
                    if delimiter_text:
                        delimiters.append({
                            'text': delimiter_text,
                            'before_param': param['number']
                        })
                last_end = param['position'] + len(param['text'])
            
            # Check for delimiter after last parameter
            if last_end < len(pattern):
                delimiter_text = pattern[last_end:].strip()
                # Since pattern is already stripped and we have text after last_end,
                # delimiter_text should always be non-empty
                delimiters.append({
                    'text': delimiter_text, 
                    'after_last_param': True
                })
        else:
            # No parameters - the entire pattern is a delimiter  
            if pattern.strip():
                delimiters.append({
                    'text': pattern.strip(),
                    'before_param': None
                })
        
        return {
            'command_name': '\\def',
            'complete_start': command_start,
            'complete_end': replacement_result['end'],
            'arguments': {
                'pattern': {
                    'value': pattern,
                    'start': pattern_start,
                    'end': pattern_end,
                    'type': 'def_pattern',
                    'parameters': parameters,
                    'delimiters': delimiters
                },
                'replacement': {
                    'value': replacement_result['value'],
                    'start': replacement_result['start'],
                    'end': replacement_result['end'],
                    'type': 'def_replacement'
                }
            }
        }

    @staticmethod
    def find_math_delimiters(content: str) -> List[Dict[str, Any]]:
        """
        Find all LaTeX math mode delimiters in the content.
        
        Searches for all math delimiters including:
        - Display math: $$ and \\[ \\]
        - Inline math: $ and \\( \\)
        
        Handles escaped delimiters properly by counting preceding backslashes.
        When $$ is found, it takes precedence over individual $ signs.
        
        :param content: The LaTeX content to search
        :return: List of dictionaries with delimiter info (command_name, start, end)
        """
        delimiters = []
        i = 0
        
        while i < len(content):
            # Check for escaped $ (\$) - skip it
            if content[i] == '$':
                # Count backslashes before the $
                backslash_count = 0
                j = i - 1
                while j >= 0 and content[j] == '\\':
                    backslash_count += 1
                    j -= 1
                
                # If odd number of backslashes, the $ is escaped
                if backslash_count % 2 == 1:
                    i += 1
                    continue
                
                # Check for $$ first (must come before single $)
                if i < len(content) - 1 and content[i+1] == '$':
                    delimiters.append({
                        'command_name': '$$',
                        'start': i,
                        'end': i + 2
                    })
                    i += 2
                    continue
                else:
                    # Single $
                    delimiters.append({
                        'command_name': '$',
                        'start': i,
                        'end': i + 1
                    })
                    i += 1
                    continue
                    
            # Check for \( \[ \) and \]
            elif i < len(content) - 1 and content[i] == '\\':
                if content[i+1] == '(':
                    delimiters.append({
                        'command_name': '\\(',
                        'start': i,
                        'end': i + 2
                    })
                    i += 2
                    continue
                elif content[i+1] == '[':
                    delimiters.append({
                        'command_name': '\\[',
                        'start': i,
                        'end': i + 2
                    })
                    i += 2
                    continue
                elif content[i+1] == ')':
                    delimiters.append({
                        'command_name': '\\)',
                        'start': i,
                        'end': i + 2
                    })
                    i += 2
                    continue
                elif content[i+1] == ']':
                    delimiters.append({
                        'command_name': '\\]',
                        'start': i,
                        'end': i + 2
                    })
                    i += 2
                    continue
            
            i += 1
        
        return delimiters

    @staticmethod
    def find_display_math_delimiters(content: str) -> List[Dict[str, Any]]:
        """
        Find display math delimiters only in the content.
        
        Filters the results of find_math_delimiters to return only display math
        delimiters: $$ and \\[ \\]
        
        :param content: The LaTeX content to search
        :return: List of dictionaries with display math delimiter info
        """
        all_delimiters = Command.find_math_delimiters(content)
        return [d for d in all_delimiters if d['command_name'] in ['$$', '\\[', '\\]']]

    @staticmethod  
    def find_inline_math_delimiters(content: str) -> List[Dict[str, Any]]:
        """
        Find inline math delimiters only in the content.
        
        Filters the results of find_math_delimiters to return only inline math
        delimiters: $ and \\( \\)
        
        :param content: The LaTeX content to search
        :return: List of dictionaries with inline math delimiter info
        """
        all_delimiters = Command.find_math_delimiters(content)
        return [d for d in all_delimiters if d['command_name'] in ['$', '\\(', '\\)']]

    @staticmethod
    def apply_string_replacements(content: str, replacements: Dict[int, tuple]) -> str:
        """
        Apply string replacements to content at specified positions.
        
        Replacements are applied in reverse position order to maintain 
        position accuracy as the string is modified.
        
        :param content: Original content string
        :param replacements: Map of position to (replacement_text, original_length)
        :return: Content with replacements applied
        """
        if not replacements:
            return content
            
        result = content
        for pos in sorted(replacements.keys(), reverse=True):
            replacement_text, original_length = replacements[pos]
            result = result[:pos] + replacement_text + result[pos + original_length:]
        
        return result
