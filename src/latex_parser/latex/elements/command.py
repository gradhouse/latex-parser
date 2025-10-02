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
            command_name = match.group(1)
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
                    match.group(1),  # name (the non-letter character)
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
        :param command_name: The specific command name to find (without the backslash)
        :return: List of tuples (start, end) with positions of the command
        """
        
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
