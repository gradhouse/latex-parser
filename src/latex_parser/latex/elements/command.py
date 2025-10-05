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
        :return: List of tuples (command_name, start_pos, end_pos) where:
                 - command_name (str): Full command name including backslash (e.g., "\\textbf", "\\section*")
                 - start_pos (int): 0-based index of command start (position of backslash)
                 - end_pos (int): 0-based index after command end (exclusive)
                 
        Example:
            >>> find_all_commands("\\textbf{hello} \\emph{world}")
            [('\\textbf', 0, 7), ('\\emph', 15, 20)]
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
        :return: List of tuples (start_pos, end_pos) where:
                 - start_pos (int): 0-based index of command start (position of backslash)
                 - end_pos (int): 0-based index after command name end (exclusive, before arguments)
                 
        Example:
            >>> find_command("\\textbf{hello} \\textbf{world}", "\\textbf")
            [(0, 7), (15, 22)]
            
        :raises ValueError: If command_name doesn't start with backslash
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
        
        Return structure:
        {
            'arguments': {
                'arg_name1': {
                    'value': str,     # Argument content
                    'start': int,     # Start position of argument (including delimiter)
                    'end': int,       # End position of argument (including delimiter)
                    'type': str       # 'optional' or 'required'
                },
                'arg_name2': { ... },
                ...
            }
        }
        
        Example:
            >>> parse_command_arguments(content, "textbf", 0, 7, "\\textbf{text}")
            {
                'arguments': {
                    'text': {
                        'value': 'hello',
                        'start': 7,
                        'end': 14,
                        'type': 'required'
                    }
                }
            }
        """
        return Command.parse_arguments(content, command_name, command_start, command_end, syntax, is_environment=False)

    @staticmethod
    def _parse_bracket_argument(content: str, start_pos: int) -> Optional[Dict[str, Any]]:
        """
        Parse an optional argument starting with '['.
        
        :param content: The content buffer
        :param start_pos: Position of the opening '['
        :return: Dictionary with value and positions, or None if parsing fails
        
        Return structure:
        {
            'value': str,     # Argument content (without brackets)
            'start': int,     # Start position of '[' 
            'end': int        # End position after ']'
        }
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
        
        Return structure:
        {
            'value': str,     # Argument content (without braces)
            'start': int,     # Start position of '{'
            'end': int        # End position after '}'
        }
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
        
        Return structure:
        {
            'command_name': str,      # Always '\\def'
            'complete_start': int,    # Start position of entire def command
            'complete_end': int,      # End position of entire def command
            'arguments': {
                'pattern': {
                    'value': str,         # Full pattern string (e.g., '\\mycommand#1#2')
                    'start': int,         # Start position of pattern
                    'end': int,           # End position of pattern
                    'type': str,          # Always 'def_pattern'
                    'parameters': [       # List of parameter info
                        {
                            'number': int,    # Parameter number (1, 2, 3, ...)
                            'position': int,  # Position in pattern string
                            'text': str       # Parameter text (e.g., '#1')
                        }, ...
                    ],
                    'delimiters': [       # List of delimiter info
                        {
                            'text': str,           # Delimiter text
                            'before_param': int,   # Parameter number this appears before (or None)
                            'after_last_param': bool  # True if appears after last parameter
                        }, ...
                    ]
                },
                'replacement': {
                    'value': str,         # Replacement text
                    'start': int,         # Start position of replacement
                    'end': int,           # End position of replacement
                    'type': str           # Always 'def_replacement'
                }
            }
        }
        
        Example:
            >>> parse_def_command(r'\\def\\cmd#1{Hello #1}', 0, 4)
            {
                'command_name': '\\def',
                'complete_start': 0,
                'complete_end': 18,
                'arguments': {
                    'pattern': {
                        'value': '\\cmd#1',
                        'parameters': [{'number': 1, 'position': 4, 'text': '#1'}],
                        'delimiters': [{'text': '\\cmd', 'before_param': 1}]
                    },
                    'replacement': {'value': 'Hello #1'}
                }
            }
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
    def get_document_defined_commands(content: str) -> List[Dict[str, Any]]:
        """
        Find all document-defined commands in LaTeX content.
        
        Searches for and parses all LaTeX command definition commands:
        - \\newcommand and \\newcommand*: Define new commands; error if command already exists
        - \\renewcommand and \\renewcommand*: Redefine existing commands; error if command does not exist  
        - \\providecommand and \\providecommand*: Define commands only if not already defined
        
        The starred versions (*) disallow paragraph breaks in the command definition.
        
        References:
        - Lamport, L. (1994). LaTeX: A Document Preparation System. 2nd ed. Addison-Wesley. 
          Sections 3.4, C.12.1. Pages 52-54, 212-213.
        - Mittelbach, F., et al. (2004). The LaTeX Companion. 2nd ed. Addison-Wesley.
          Sections A.1.2. Pages 843-847.
        
        :param content: LaTeX content to search
        :return: List of parsed command definitions
        
        Return structure for each command definition:
        {
            'command_name': str,       # Full command name (e.g., '\\newcommand')
            'complete_start': int,     # Start position of entire definition
            'complete_end': int,       # End position of entire definition
            'arguments': {
                'cmd': {
                    'value': str,          # Defined command name (e.g., '\\mycmd')
                    'start': int,          # Start position
                    'end': int,            # End position
                    'type': str            # 'required'
                },
                'nargs': {             # Optional - number of arguments
                    'value': str,          # Number as string
                    'start': int,
                    'end': int,
                    'type': str            # 'optional'
                },
                'default': {           # Optional - default value for first argument
                    'value': str,          # Default value
                    'start': int,
                    'end': int,
                    'type': str            # 'optional'
                },
                'definition': {
                    'value': str,          # Command definition/replacement text
                    'start': int,
                    'end': int,
                    'type': str            # 'required'
                }
            }
        }
        
        Example:
            >>> get_document_defined_commands(r'\\newcommand{\\foo}[1]{Hello #1}')
            [{'command_name': '\\newcommand', 'arguments': {'cmd': {'value': '\\foo'}, ...}}]
        """
        # Command definitions to search for
        command_definitions = [
            ('\\newcommand', '\\newcommand{cmd}[nargs][default]{definition}'),
            ('\\newcommand*', '\\newcommand*{cmd}[nargs][default]{definition}'),
            ('\\renewcommand', '\\renewcommand{cmd}[nargs][default]{definition}'),
            ('\\renewcommand*', '\\renewcommand*{cmd}[nargs][default]{definition}'),
            ('\\providecommand', '\\providecommand{cmd}[nargs][default]{definition}'),
            ('\\providecommand*', '\\providecommand*{cmd}[nargs][default]{definition}')
        ]
        
        all_definitions = []
        
        for command, syntax in command_definitions:
            # Find all occurrences of this command
            positions = Command.find_command(content, command)
            
            # Parse each occurrence
            for start_position, end_position in positions:
                parsed = Command.parse_arguments(content, command, start_position, end_position, syntax, False)
                
                if parsed:
                    all_definitions.append(parsed)
        
        # Sort by position in document
        all_definitions.sort(key=lambda x: x['complete_start'])
        
        return all_definitions

    @staticmethod
    def get_document_defined_environments(content: str) -> List[Dict[str, Any]]:
        """
        Find all document-defined environments in LaTeX content.
        
        Searches for and parses all LaTeX environment definition commands:
        - \\newenvironment: Define new environments; error if environment already exists
        - \\renewenvironment: Redefine existing environments; error if environment does not exist
        
        References:
        - Lamport, L. (1994). LaTeX: A Document Preparation System. 2nd ed. Addison-Wesley. 
          Sections 3.5, C.12.2. Pages 54-55, 213-214.
        - Mittelbach, F., et al. (2004). The LaTeX Companion. 2nd ed. Addison-Wesley.
          Sections A.1.3. Pages 847-850.
        
        :param content: LaTeX content to search
        :return: List of parsed environment definitions
        
        Return structure for each environment definition:
        {
            'command_name': str,       # Full command name (e.g., '\\newenvironment')
            'complete_start': int,     # Start position of entire definition
            'complete_end': int,       # End position of entire definition
            'arguments': {
                'name': {
                    'value': str,          # Environment name (e.g., 'myenv')
                    'start': int,          # Start position
                    'end': int,            # End position
                    'type': str            # 'required'
                },
                'nargs': {             # Optional - number of arguments
                    'value': str,          # Number as string
                    'start': int,
                    'end': int,
                    'type': str            # 'optional'
                },
                'default': {           # Optional - default value for first argument
                    'value': str,          # Default value
                    'start': int,
                    'end': int,
                    'type': str            # 'optional'
                },
                'begin_definition': {
                    'value': str,          # Begin environment definition
                    'start': int,
                    'end': int,
                    'type': str            # 'required'
                },
                'end_definition': {
                    'value': str,          # End environment definition
                    'start': int,
                    'end': int,
                    'type': str            # 'required'
                }
            }
        }
        
        Example:
            >>> get_document_defined_environments(r'\\newenvironment{myenv}{\\begin{center}}{\\end{center}}')
            [{'command_name': '\\newenvironment', 'arguments': {'name': {'value': 'myenv'}, ...}}]
        """
        # Environment definitions to search for
        environment_definitions = [
            ('\\newenvironment', '\\newenvironment{name}[nargs][default]{begin_definition}{end_definition}'),
            ('\\renewenvironment', '\\renewenvironment{name}[nargs][default]{begin_definition}{end_definition}')
        ]
        
        all_definitions = []
        
        for command, syntax in environment_definitions:
            # Find all occurrences of this command
            positions = Command.find_command(content, command)
            
            # Parse each occurrence
            for start_position, end_position in positions:
                parsed = Command.parse_arguments(content, command, start_position, end_position, syntax, False)
                
                if parsed:
                    all_definitions.append(parsed)
        
        # Sort by position in document
        all_definitions.sort(key=lambda x: x['complete_start'])
        
        return all_definitions

    @staticmethod
    def apply_string_replacements(content: str, replacements: Dict[int, tuple]) -> str:
        """
        Apply string replacements to content at specified positions.
        
        Replacements are applied in reverse position order to maintain 
        position accuracy as the string is modified.
        
        :param content: Original content string
        :param replacements: Map of position to (replacement_text, original_length) tuples
                           - position (int): 0-based index where replacement starts
                           - replacement_text (str): New text to insert
                           - original_length (int): Length of original text to replace
        :return: Content with replacements applied
        
        Example:
            >>> apply_string_replacements("Hello world", {0: ("Hi", 5)})
            "Hi world"
        """
        if not replacements:
            return content
            
        result = content
        for pos in sorted(replacements.keys(), reverse=True):
            replacement_text, original_length = replacements[pos]
            result = result[:pos] + replacement_text + result[pos + original_length:]
        
        return result

    @staticmethod
    def modernize_def_commands(content: str, is_strict: bool = False) -> str:
        """
        Convert \\def commands to \\newcommand where possible.
        
        Converts simple \\def patterns that can be expressed as \\newcommand:
        - \\def\\mycommand{text} → \\newcommand{\\mycommand}{text}
        - \\def\\mycommand#1{text} → \\newcommand{\\mycommand}[1]{text}
        - \\def\\mycommand#1#2{text} → \\newcommand{\\mycommand}[2]{text}
        
        Leaves complex \\def patterns unchanged (delimited parameters, etc.)
        
        :param content: LaTeX content containing \\def commands
        :param is_strict: If True, raises ValueError when a \\def cannot be converted.
                      If False (default), skips unconvertible \\def commands silently.
        :return: Content with \\def commands modernized to \\newcommand where possible
        :raises ValueError: If strict=True and a \\def command cannot be converted
        """
        # Find all \def commands
        def_positions = Command.find_command(content, '\\def')
        
        if not def_positions:
            return content
        
        # Build replacement map
        replacements = {}
        
        for start, end in def_positions:
            # Parse the \def command
            def_result = Command.parse_def_command(content, start, end)
            
            if def_result:
                # Try to convert to \newcommand
                newcommand_text = Command._convert_def_to_newcommand(def_result)
                
                if newcommand_text:
                    # Add to replacements map
                    original_length = def_result['complete_end'] - def_result['complete_start']
                    replacements[def_result['complete_start']] = (newcommand_text, original_length)
                elif is_strict:
                    # In strict mode, raise an exception for unconvertible patterns
                    pattern = def_result['arguments']['pattern']['value']
                    reason = Command._get_conversion_failure_reason(def_result)
                    raise ValueError(f"Cannot convert \\def command to \\newcommand: {pattern}. Reason: {reason}")
            elif is_strict:
                # In strict mode, raise an exception for unparseable \def commands
                def_text = content[start:end]
                raise ValueError(f"Failed to parse \\def command: {def_text}")
        
        # Apply replacements
        return Command.apply_string_replacements(content, replacements)
    
    @staticmethod
    def _convert_def_to_newcommand(def_result: Dict[str, Any]) -> Optional[str]:
        """
        Convert a parsed \\def command to \\newcommand syntax if possible.
        
        :param def_result: Output from parse_def_command (see parse_def_command documentation for structure)
        :return: \\newcommand string if conversion possible, None otherwise
        
        Returns a string in format:
        - No parameters: "\\newcommand{\\cmdname}{replacement}"
        - With parameters: "\\newcommand{\\cmdname}[N]{replacement}"
        
        Example:
            For input representing "\\def\\hello#1{Hi #1}":
            Returns "\\newcommand{\\hello}[1]{Hi #1}"
        """
        pattern_info = def_result['arguments']['pattern']
        replacement_info = def_result['arguments']['replacement']
        
        parameters = pattern_info['parameters']
        delimiters = pattern_info['delimiters']
        
        # Check if conversion is possible
        if not Command._can_convert_def_to_newcommand(parameters, delimiters):
            return None
        
        # Extract command name from pattern
        command_name = Command._extract_command_name_from_pattern(pattern_info['value'], parameters)
        
        if not command_name:
            return None
        
        # Build \newcommand
        replacement_text = replacement_info['value']
        
        if not parameters:
            # No parameters: \newcommand{\commandname}{replacement}
            return f"\\newcommand{{{command_name}}}{{{replacement_text}}}"
        else:
            # With parameters: \newcommand{\commandname}[n]{replacement}
            param_count = len(parameters)
            return f"\\newcommand{{{command_name}}}[{param_count}]{{{replacement_text}}}"
    
    @staticmethod
    def _can_convert_def_to_newcommand(parameters: List[Dict[str, Any]], delimiters: List[Dict[str, Any]]) -> bool:
        """
        Check if a \\def pattern can be converted to \\newcommand.
        
        :param parameters: List of parameter info from def parsing (see parse_def_command docs)
        :param delimiters: List of delimiter info from def parsing (see parse_def_command docs)
        :return: True if conversion is possible, False otherwise
        
        Conversion rules:
        - Parameters must be sequential (1, 2, 3, ...)
        - No delimited parameters allowed (e.g., \\def\\cmd#1 stop{...})
        - Only simple patterns convertible to \\newcommand syntax
        """
        if not parameters:
            # No parameters - always convertible
            return True
        
        # Check for sequential parameter numbering (1, 2, 3, ...)
        expected_numbers = list(range(1, len(parameters) + 1))
        actual_numbers = [p['number'] for p in parameters]
        
        if actual_numbers != expected_numbers:
            # Non-sequential parameters - cannot convert
            return False
        
        # Check for delimited parameters (delimiters between or after parameters)
        for delimiter in delimiters:
            # Allow only the command name delimiter before first parameter
            if 'before_param' in delimiter and delimiter['before_param'] == 1:
                continue  # This is the command name, which is fine
            elif delimiter.get('before_param') is None and len(delimiters) == 1:
                continue  # This is just the command name with no parameters
            else:
                # Any other delimiter indicates delimited parameters - cannot convert
                return False
        
        return True
    
    @staticmethod
    def _get_conversion_failure_reason(def_result: Dict[str, Any]) -> str:
        """
        Get a human-readable reason why a \\def command cannot be converted.
        
        :param def_result: Output from parse_def_command
        :return: String describing why conversion failed
        """
        pattern_info = def_result['arguments']['pattern']
        parameters = pattern_info['parameters']
        delimiters = pattern_info['delimiters']
        
        if not parameters:
            return "Unknown parsing error"
        
        # Check for sequential parameter numbering
        expected_numbers = list(range(1, len(parameters) + 1))
        actual_numbers = [p['number'] for p in parameters]
        
        if actual_numbers != expected_numbers:
            return f"Non-sequential parameters (found: {actual_numbers}, expected: {expected_numbers})"
        
        # Check for delimited parameters
        for delimiter in delimiters:
            if 'before_param' in delimiter and delimiter['before_param'] == 1:
                continue  # Command name delimiter is OK
            elif delimiter.get('before_param') is None and len(delimiters) == 1:
                continue  # Just command name with no parameters
            else:
                return f"Contains delimited parameters (delimiter: '{delimiter.get('text', 'unknown')}')"
        
        return "Unknown conversion restriction"

    @staticmethod
    def _extract_command_name_from_pattern(pattern: str, parameters: List[Dict[str, Any]]) -> Optional[str]:
        """
        Extract the command name from a \\def pattern.
        
        :param pattern: The pattern string (e.g., "\\mycommand#1#2")
        :param parameters: List of parameter info (see parse_def_command docs for structure)
        :return: Command name (e.g., "\\mycommand") or None if extraction fails
        
        Extraction rules:
        - Command name must start with backslash
        - Command name cannot contain spaces
        - For patterns with parameters: extracts text before first parameter
        - For patterns without parameters: uses entire pattern (if valid)
        """
        if not parameters:
            # No parameters - the entire pattern should be the command name
            pattern_clean = pattern.strip()
            if pattern_clean.startswith('\\') and ' ' not in pattern_clean:
                return pattern_clean
            return None
        
        # Find the position of the first parameter
        first_param = min(parameters, key=lambda p: p['position'])
        first_param_pos = first_param['position']
        
        # Command name is everything before the first parameter
        command_name = pattern[:first_param_pos].strip()
        
        if command_name.startswith('\\') and ' ' not in command_name:
            return command_name
        
        return None
