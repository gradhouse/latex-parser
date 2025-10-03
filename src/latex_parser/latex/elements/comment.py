# File: comment.py
# Description: LaTeX comment detection and removal methods for LaTeX/TeX parsing
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import re
from typing import Dict, Tuple, List, Optional, Any, NamedTuple


class CommentSpan(NamedTuple):
    """Represents a comment span in the text."""
    start: int
    end: int
    comment_type: str  # 'inline', 'line_continuation', 'comment_only_line'
    content: str  # The actual comment content (without the %)


class Comment:
    """
    LaTeX comment detection and removal methods.
    
    Handles the core rules of LaTeX comments including:
    - Inline comments (% rest of line removed, newline becomes space)
    - Line continuation (% at end swallows newline, no space)
    - Escaped percent (\\% is not a comment)
    
    Note: This class assumes verbatim regions have been preprocessed.
    For verbatim handling, use a separate verbatim detection method first.
    """
    
    @staticmethod
    def detect_comments(text: str) -> List[CommentSpan]:
        """
        Detect all comment spans in the text.
        
        Args:
            text: The input text to analyze (should have verbatim regions preprocessed)
            
        Returns:
            List of CommentSpan objects indicating comment locations
        """
        comments = []
        lines = text.split('\n')
        current_pos = 0
        
        for line_idx, line in enumerate(lines):
            line_start = current_pos
            
            # Find % characters in this line
            i = 0
            while i < len(line):
                if line[i] == '%':
                    abs_pos = line_start + i
                    
                    # Skip if escaped
                    if Comment._is_escaped_percent(text, abs_pos):
                        i += 1
                        continue
                    
                    # Found a comment - determine type and span
                    comment_start = abs_pos
                    comment_end = line_start + len(line)  # End of line
                    
                    # Determine comment type
                    comment_type = "inline"
                    
                    # Check for comment-only line
                    line_before_comment = line[:i].strip()
                    if not line_before_comment:  # Only whitespace before %
                        comment_type = "comment_only_line"
                    else:
                        # Check for line continuation
                        line_after_comment = line[i+1:].strip()
                        if not line_after_comment:  # Only whitespace/nothing after %
                            comment_type = "line_continuation"
                    
                    # Get comment content (without the %)
                    comment_content = line[i+1:]
                    
                    comments.append(CommentSpan(
                        start=comment_start,
                        end=comment_end,
                        comment_type=comment_type,
                        content=comment_content
                    ))
                    
                    # Skip rest of line since it's all comment
                    break
                
                i += 1
            
            # Move to next line (including newline character)
            current_pos = line_start + len(line) + 1
        
        return comments
    
    @staticmethod
    def remove_comments(text: str) -> str:
        """
        Remove comments from text according to LaTeX rules.
        
        This handles:
        - Inline comments: % to end of line removed, newline becomes space
        - Line continuation: % at end of line removes newline, no space added
        - Comment-only lines: entire line removed including newline
        - Escaped %: \\% is preserved as literal
        
        Args:
            text: Input text with comments (should have verbatim regions preprocessed)
            
        Returns:
            Text with comments removed and spacing handled correctly
        """
        if not text:
            return text
            
        comments = Comment.detect_comments(text)
        
        if not comments:
            return text
        
        # Process comments in reverse order to maintain positions
        result = text
        
        for comment in reversed(comments):
            before = result[:comment.start]
            after_comment = result[comment.end:]
            
            if comment.comment_type == "line_continuation":
                # For line continuation, % removes itself and swallows newline
                # Also removes trailing space before % if present
                if comment.end < len(result) and result[comment.end] == '\n':
                    after_comment = result[comment.end + 1:]
                
                # Remove trailing space before % for line continuation
                if before.endswith(' '):
                    before = before.rstrip(' ')
                
                result = before + after_comment
                
            elif comment.comment_type == "comment_only_line":
                # Remove entire line including newline after the comment (if any)
                if comment.end < len(result) and result[comment.end] == '\n':
                    after_comment = result[comment.end + 1:]
                else:
                    # No newline after comment (EOF case)
                    after_comment = result[comment.end:]
                
                # If there's no content after this comment-only line,
                # also remove the preceding newline (EOF case)
                if not after_comment.strip():
                    if before.endswith('\n'):
                        before = before[:-1]
                
                result = before + after_comment
                
            else:  # inline comment
                # Remove comment, newline becomes space (if followed by content)
                if comment.end < len(result) and result[comment.end] == '\n':
                    # Check if there's non-whitespace content after the newline
                    remaining = result[comment.end + 1:]
                    if remaining and remaining.strip():  # There's non-whitespace content
                        # Insert single space unless before char is already whitespace
                        # Note: before is guaranteed to be non-empty for inline comments
                        if not before[-1].isspace():
                            result = before + ' ' + remaining
                        else:
                            result = before + remaining
                    else:
                        result = before + remaining
                else:
                    # No newline after comment (end of file) - remove trailing space before %
                    if before.endswith(' '):
                        before = before.rstrip(' ')
                    result = before + after_comment
        
        return result
    
    @staticmethod
    def _is_escaped_percent(text: str, pos: int) -> bool:
        """
        Check if the % at position pos is escaped with backslash.
        
        Args:
            text: The text to check
            pos: Position of the % character
            
        Returns:
            True if the % is escaped (\\%), False otherwise
        """
        if pos < 1 or pos >= len(text) or text[pos] != '%':
            return False
        
        # Count consecutive backslashes before the %
        backslash_count = 0
        i = pos - 1
        while i >= 0 and text[i] == '\\':
            backslash_count += 1
            i -= 1
        
        # % is escaped if preceded by odd number of backslashes
        return backslash_count % 2 == 1


