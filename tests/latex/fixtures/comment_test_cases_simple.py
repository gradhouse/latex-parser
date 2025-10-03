# File: comment_test_cases.py
# Description: Test case fixtures for LaTeX comment detection and removal (verbatim-free)
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.
#
# Note: This file contains test cases for core comment functionality only.
# Verbatim environment handling should be done as a separate preprocessing step.

# Basic comment detection and removal test cases
COMMENT_BASIC_TESTS = [
    {
        "id": "simple_inline",
        "description": "Simple inline comment",
        "input": r"""Hello % this is a comment
world""",
        "expected": "Hello world"
    },
    {
        "id": "line_continuation",
        "description": "Line continuation using % at end of line",
        "input": r"""Hello %
world""",
        "expected": "Helloworld"
    },
    {
        "id": "percent_escaped",
        "description": "Escaped percent is not a comment",
        "input": r"""100\% % comment
foo""",
        "expected": r"100\% foo"
    },
    {
        "id": "comment_only_line",
        "description": "Comment-only line is completely removed",
        "input": r"""line1
% this is a comment line
line2""",
        "expected": "line1\nline2"
    },
    {
        "id": "multiple_comments",
        "description": "Multiple comments on same line",
        "input": r"""text % first comment % second comment
more""",
        "expected": "text more"
    }
]

COMMENT_EDGE_TESTS = [
    {
        "id": "percent_at_start",
        "description": "Comment at start of line",
        "input": r"""% comment at start
content""",
        "expected": "content"
    },
    {
        "id": "percent_at_end_no_newline",
        "description": "Comment at end of file with no newline",
        "input": r"""text % comment""",
        "expected": "text"
    },
    {
        "id": "empty_comment",
        "description": "Empty comment (just %)",
        "input": r"""text %
more""",
        "expected": "textmore"
    },
    {
        "id": "whitespace_before_comment",
        "description": "Whitespace before comment",
        "input": r"""text  % comment with spaces before
more""",
        "expected": "text  more"
    },
    {
        "id": "tab_before_comment",
        "description": "Tab before comment",
        "input": r"""text	% comment with tab before
more""",
        "expected": "text	more"
    }
]

COMMENT_ESCAPE_TESTS = [
    {
        "id": "single_backslash_percent",
        "description": "Single backslash before % - escaped",
        "input": r"""text\% not a comment""",
        "expected": r"text\% not a comment"
    },
    {
        "id": "double_backslash_percent",
        "description": "Double backslash before % - not escaped",
        "input": r"""text\\% this is a comment
more""",
        "expected": r"text\\ more"
    },
    {
        "id": "triple_backslash_percent",
        "description": "Triple backslash before % - escaped",
        "input": r"""text\\\% not a comment""",
        "expected": r"text\\\% not a comment"
    }
]

COMMENT_LINE_CONTINUATION_TESTS = [
    {
        "id": "line_continuation_basic",
        "description": "Basic line continuation",
        "input": "A%\nB",
        "expected": "AB"
    },
    {
        "id": "line_continuation_with_space",
        "description": "Line continuation removes trailing space",
        "input": "A %\nB",
        "expected": "AB"
    },
    {
        "id": "line_continuation_multiple",
        "description": "Multiple line continuations",
        "input": "A%\nB%\nC",
        "expected": "ABC"
    }
]

# All test cases combined
ALL_COMMENT_TESTS = (
    COMMENT_BASIC_TESTS +
    COMMENT_EDGE_TESTS +
    COMMENT_ESCAPE_TESTS +
    COMMENT_LINE_CONTINUATION_TESTS
)