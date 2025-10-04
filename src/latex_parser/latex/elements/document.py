# File: document.py
# Description: LaTeX document structure methods
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LI        return backslash_count % 2 == 1details.

import re

from typing import Dict, List, Any
from .command import Command


class Document:
    """
    LaTeX document structure methods
    """

    @staticmethod
    def modernize_input_commands(content: str) -> str:
        r"""
        Modernize \input commands from \input filename to \input{filename}.
        
        Preserves correctly formatted commands:
        - \input{filename} (already correct)
        - \input   {filename} (already correct with whitespace)
        
        Modernizes only:
        - \input filename (no braces)
        - \input   filename (with whitespace before filename)
        
        :param content: LaTeX content to modernize
        :return: Content with modernized \input commands
        """
        if not content:
            return content
            
        # Find all \input commands in the content
        input_commands = Document._find_input_commands(content)
        
        # Build replacement map for commands that need modernization
        replacements = Document._build_input_replacements(input_commands)
        
        # Apply replacements in reverse order to maintain position accuracy
        return Command.apply_string_replacements(content, replacements)
    
    @staticmethod
    def _find_input_commands(content: str) -> List[Dict[str, Any]]:
        r"""
        Find all \input commands in content and determine if they need modernization.
        
        :param content: LaTeX content to search
        :return: List of input command info dictionaries
        """
        input_commands = []
        
        # Use Command.find_all_commands to find all commands
        all_commands = Command.find_all_commands(content)
        
        # Filter for \input commands only
        all_input_commands = [entry for entry in all_commands if entry[0] == '\\input']
        
        # Process each \input command and exclude those in comments or escaped
        for command_name, start, end in all_input_commands:
            # Check if this command is in a comment line
            if Document._is_in_comment(content, start):
                continue
                
            # Check if this command is escaped (preceded by odd number of backslashes)
            if Document._is_escaped_command(content, start):
                continue
            
            # Look for what follows the \input command
            remaining_content = content[end:]
            
            # Check for optional whitespace followed by argument
            # Match whitespace, then either {content} or non-whitespace/non-brace content
            # Stop at next backslash to handle consecutive commands
            match = re.match(r'(\s*)(\{[^}]*\}|[^\s\{\}\\]+)', remaining_content)
            
            if match:
                whitespace = match.group(1)
                argument = match.group(2)
                
                command_info = {
                    'start': start,
                    'end': end + match.end(),
                    'whitespace': whitespace,
                    'argument': argument,
                    'needs_modernization': not argument.startswith('{')
                }
                
                input_commands.append(command_info)
        
        return input_commands
    
    @staticmethod
    def _is_in_comment(content: str, position: int) -> bool:
        """
        Check if a position is within a comment line.
        
        :param content: The full content string
        :param position: Position to check
        :return: True if position is in a comment line
        """
        # Find the start of the line containing this position
        line_start = content.rfind('\n', 0, position) + 1
        line_content = content[line_start:position]
        
        # Check if there's a % before this position in the same line
        return '%' in line_content
    
    @staticmethod
    def _is_escaped_command(content: str, position: int) -> bool:
        r"""
        Check if a command at position is escaped by counting preceding backslashes.
        
        :param content: The full content string  
        :param position: Position of the command
        :return: True if command is escaped (odd number of preceding backslashes)
        """
        # Count consecutive backslashes before the command
        backslash_count = 0
        i = position - 1
        while i >= 0 and content[i] == '\\':
            backslash_count += 1
            i -= 1
        
        # Command is escaped if preceded by odd number of backslashes
        return backslash_count % 2 == 1
    
    @staticmethod
    def _build_input_replacements(input_commands: List[Dict[str, Any]]) -> Dict[int, tuple]:
        r"""
        Build replacement map for \input commands that need modernization.
        
        :param input_commands: List of input command info from _find_input_commands
        :return: Dictionary mapping position to (replacement_text, original_length)
        """
        replacements = {}
        
        for cmd in input_commands:
            if cmd['needs_modernization']:
                # Build modernized version: \input{filename}
                modernized = f"\\input{{{cmd['argument']}}}"
                original_length = cmd['end'] - cmd['start']
                
                replacements[cmd['start']] = (modernized, original_length)
        
        return replacements