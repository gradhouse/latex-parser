# File: equation.py
# Description: LaTeX equation and math mode methods
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

from typing import Dict, List, Any
from .command import Command


class Equation:
    """
    LaTeX equation and math mode methods
    """

    @staticmethod
    def modernize_math_delimiters(content: str) -> str:
        """
        Convert old TeX math delimiters to modern LaTeX equivalents.
        
        Converts:
        - \\( \\) to \\begin{math} \\end{math}
        - $ $ (matching pairs) to \\begin{math} \\end{math}
        - \\[ \\] to \\begin{displaymath} \\end{displaymath}
        - $$ $$ to \\begin{displaymath} \\end{displaymath}
        
        Only converts properly paired delimiters, leaving unmatched ones unchanged.
        
        :param content: The LaTeX content to modernize
        :return: Content with modernized math delimiters
        """
        delimiters = Command.find_math_delimiters(content)
        math_replacements = Equation._build_math_delimiter_replacements(delimiters)
        return Command.apply_string_replacements(content, math_replacements)

    @staticmethod
    def _build_math_delimiter_replacements(delimiters: List[Dict[str, Any]]) -> Dict[int, tuple]:
        """
        Build a map of math delimiter positions to their LaTeX environment replacements.
        
        Uses proper pairing logic:
        - $ and $$ are paired consecutively
        - \\( and \\) are paired using stack-based matching
        - \\[ and \\] are paired using stack-based matching
        
        :param delimiters: List of delimiter dictionaries from find_math_delimiters
        :return: Dictionary mapping position to (replacement_text, original_length)
        """
        if not delimiters:
            return {}
            
        replacements = {}
        
        # Sort delimiters by position for proper sequence processing
        delimiters_sorted = sorted(delimiters, key=lambda d: d['start'])
        
        # Group $ and $$ delimiters by type (they pair consecutively)
        dollar_delims = [d for d in delimiters_sorted if d['command_name'] == '$']
        double_dollar_delims = [d for d in delimiters_sorted if d['command_name'] == '$$']
        
        # Process $ pairs (consecutive pairs) - only process even count
        pair_count = len(dollar_delims) // 2
        for i in range(pair_count):
            opening = dollar_delims[i * 2]
            closing = dollar_delims[i * 2 + 1]
            replacements[opening['start']] = ('\\begin{math}', opening['end'] - opening['start'])
            replacements[closing['start']] = ('\\end{math}', closing['end'] - closing['start'])
        
        # Process $$ pairs (consecutive pairs) - only process even count
        pair_count = len(double_dollar_delims) // 2
        for i in range(pair_count):
            opening = double_dollar_delims[i * 2]
            closing = double_dollar_delims[i * 2 + 1]
            replacements[opening['start']] = ('\\begin{displaymath}', opening['end'] - opening['start'])
            replacements[closing['start']] = ('\\end{displaymath}', closing['end'] - closing['start'])
        
        # Process \( and \) using stack-based matching
        paren_stack = []
        for delimiter in delimiters_sorted:
            if delimiter['command_name'] == '\\(':
                paren_stack.append(delimiter)
            elif delimiter['command_name'] == '\\)' and paren_stack:
                opening = paren_stack.pop()
                replacements[opening['start']] = ('\\begin{math}', opening['end'] - opening['start'])
                replacements[delimiter['start']] = ('\\end{math}', delimiter['end'] - delimiter['start'])
        
        # Process \[ and \] using stack-based matching  
        bracket_stack = []
        for delimiter in delimiters_sorted:
            if delimiter['command_name'] == '\\[':
                bracket_stack.append(delimiter)
            elif delimiter['command_name'] == '\\]' and bracket_stack:
                opening = bracket_stack.pop()
                replacements[opening['start']] = ('\\begin{displaymath}', opening['end'] - opening['start'])
                replacements[delimiter['start']] = ('\\end{displaymath}', delimiter['end'] - delimiter['start'])
        
        return replacements