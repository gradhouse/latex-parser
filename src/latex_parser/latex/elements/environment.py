# File: environment.py
# Description: LaTeX environment methods
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import re
from typing import Dict, Tuple, List

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
