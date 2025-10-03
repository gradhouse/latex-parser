# File: test_comment.py
# Description: Simplified test cases for LaTeX comment detection and removal (no verbatim)
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import pytest
import sys
import os
from latex_parser.latex.elements.comment import Comment, CommentSpan

# Add the tests directory to the path to import fixtures
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from latex.fixtures.comment_test_cases_simple import (
    COMMENT_BASIC_TESTS,
    COMMENT_EDGE_TESTS,
    COMMENT_ESCAPE_TESTS,
    COMMENT_LINE_CONTINUATION_TESTS,
    ALL_COMMENT_TESTS
)


class TestCommentDetection:
    """Test class for comment detection functionality."""

    @pytest.mark.parametrize("test_case", COMMENT_BASIC_TESTS, ids=lambda x: x['id'])
    def test_comment_detection_basic(self, test_case):
        """Test basic comment detection scenarios."""
        input_text = test_case['input']
        comments = Comment.detect_comments(input_text)
        
        # Verify comments are detected
        assert isinstance(comments, list)
        for comment in comments:
            assert isinstance(comment, CommentSpan)
            assert comment.start >= 0
            assert comment.end > comment.start
            assert comment.comment_type in ['inline', 'line_continuation', 'comment_only_line']

    @pytest.mark.parametrize("test_case", COMMENT_EDGE_TESTS, ids=lambda x: x['id'])
    def test_comment_detection_edge_cases(self, test_case):
        """Test edge cases for comment detection."""
        input_text = test_case['input']
        comments = Comment.detect_comments(input_text)
        
        # Verify comments are detected
        assert isinstance(comments, list)


class TestCommentRemoval:
    """Test class for comment removal functionality."""

    @pytest.mark.parametrize("test_case", COMMENT_BASIC_TESTS, ids=lambda x: x['id'])
    def test_comment_removal_basic(self, test_case):
        """Test basic comment removal scenarios."""
        input_text = test_case['input']
        expected = test_case['expected']
        
        result = Comment.remove_comments(input_text)
        assert result == expected, f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", COMMENT_EDGE_TESTS, ids=lambda x: x['id'])
    def test_comment_removal_edge_cases(self, test_case):
        """Test edge cases for comment removal."""
        input_text = test_case['input']
        expected = test_case['expected']
        
        result = Comment.remove_comments(input_text)
        assert result == expected, f"Failed for {test_case['description']}"

    @pytest.mark.parametrize("test_case", COMMENT_LINE_CONTINUATION_TESTS, ids=lambda x: x['id'])
    def test_comment_removal_line_continuation(self, test_case):
        """Test line continuation comment removal."""
        input_text = test_case['input']
        expected = test_case['expected']
        
        result = Comment.remove_comments(input_text)
        assert result == expected, f"Failed for {test_case['description']}"


class TestCommentHelperMethods:
    """Test class for comment helper methods."""

    @pytest.mark.parametrize("test_case", COMMENT_ESCAPE_TESTS, ids=lambda x: x['id'])
    def test_escaped_percent_handling(self, test_case):
        """Test escaped percent handling through comment removal."""
        input_text = test_case['input']
        expected = test_case['expected']
        
        # Test removal - escaped % should remain
        result = Comment.remove_comments(input_text)
        assert result == expected, f"Failed for {test_case['description']}"

    def test_line_continuation_via_remove_comments(self):
        """Test line continuation processing through remove_comments."""
        test_cases = [
            ("A%\nB", "AB"),
            ("A %\nB", "AB"),
            ("A%\nB%\nC", "ABC"),
        ]
        
        for input_text, expected in test_cases:
            result = Comment.remove_comments(input_text)
            assert result == expected


class TestCommentIntegration:
    """Test class for integration scenarios."""

    def test_empty_input(self):
        """Test empty input handling."""
        assert Comment.detect_comments("") == []
        assert Comment.remove_comments("") == ""

    def test_no_comments(self):
        """Test input with no comments."""
        input_text = "Hello world\nNo comments here"
        assert Comment.detect_comments(input_text) == []
        assert Comment.remove_comments(input_text) == input_text

    def test_comment_span_namedtuple(self):
        """Test CommentSpan NamedTuple functionality."""
        span = CommentSpan(start=5, end=10, comment_type="inline", content=" test")
        assert span.start == 5
        assert span.end == 10
        assert span.comment_type == "inline"
        assert span.content == " test"


class TestCommentCoverage:
    """Test class to achieve 100% coverage for edge cases."""

    def test_line_continuation_no_newline_after(self):
        """Test line continuation without newline after comment (EOF case)."""
        input_text = "text%"
        result = Comment.remove_comments(input_text)
        assert result == "text"

    def test_comment_only_line_eof(self):
        """Test comment-only line at end of file."""
        input_text = "text\n% comment only"
        result = Comment.remove_comments(input_text)
        assert result == "text"

    def test_comment_only_line_eof_with_preceding_newline(self):
        """Test comment-only line at EOF that removes preceding newline."""
        input_text = "% only comment"
        result = Comment.remove_comments(input_text)
        assert result == ""

    def test_inline_comment_eof(self):
        """Test inline comment at end of file."""
        input_text = "text% comment"
        result = Comment.remove_comments(input_text)
        assert result == "text"

    def test_inline_comment_before_whitespace_char(self):
        """Test inline comment where character before % is whitespace."""
        input_text = "text % comment\nmore"
        result = Comment.remove_comments(input_text)
        assert result == "text more"

    def test_line_continuation_eof_via_remove_comments(self):
        """Test line continuation at EOF through remove_comments."""
        input_text = "text%"
        result = Comment.remove_comments(input_text)
        assert result == "text"

    def test_empty_before_text_inline_comment(self):
        """Test inline comment where before text becomes empty after strip."""
        input_text = " % comment\nmore"
        result = Comment.remove_comments(input_text)
        assert result == " more"

    def test_line_continuation_with_no_next_line(self):
        """Test line continuation at very end of input."""
        input_text = "A%\nB%"  # Second % has no next line
        result = Comment.remove_comments(input_text)
        assert result == "AB"

    def test_whitespace_only_after_inline_comment(self):
        """Test inline comment followed by newline and only whitespace."""
        input_text = "text% comment\n   \n"
        result = Comment.remove_comments(input_text)
        assert result == "text   \n"


if __name__ == "__main__":
    pytest.main([__file__])