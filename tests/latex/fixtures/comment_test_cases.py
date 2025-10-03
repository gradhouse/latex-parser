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
        "description": "Simple inline comment — rest of line removed, newline becomes a space (if not swallowed).",
        "input": r"""Hello % this is a comment
world""",
        "expected_output": "Hello world",
        "expected_comments": [
            {
                "start": 6,  # Position of %
                "end": 25,   # End of first line (length of "Hello % this is a comment")
                "comment_type": "inline",
                "content": " this is a comment"
            }
        ],
        "notes": "The comment and the end-of-line are deleted; TeX inserts a space between tokens from different lines unless newline was swallowed by a trailing %."
    },
    {
        "id": "line_continuation_no_space",
        "description": "Line continuation using % at end of line — newline swallowed, no space inserted.",
        "input": r"""Hello %
world""",
        "expected_output": "Helloworld",
        "expected_comments": [
            {
                "start": 6,  # Position of %
                "end": 7,    # End of first line (length of "Hello %")
                "comment_type": "line_continuation",
                "content": ""
            }
        ],
        "notes": "The % removes the remainder of the line and also swallows the newline; no space remains."
    },
    {
        "id": "percent_escaped",
        "description": r"Escaped percent (\%) is not a comment — it becomes a token '\%'.",
        "input": r"""100\% % comment
foo""",
        "expected_output": r"100\% foo",
        "expected_comments": [
            {
                "start": 6,  # Position of second % (the unescaped one)
                "end": 15,   # End of first line (length of "100\% % comment")
                "comment_type": "inline",
                "content": " comment"
            }
        ],
        "notes": r"\% produces a printable percent character; only unescaped % starts a comment."
    },
    {
        "id": "comment_only_line",
        "description": "A whole line that is only a comment is removed (including the linebreak).",
        "input": r"""Hello
% this whole line is comment
world""",
        "expected_output": "Hello\nworld",
        "expected_comments": [
            {
                "start": 6,  # Position of % at start of second line
                "end": 34,   # End of comment line (length of "% this whole line is comment")
                "comment_type": "comment_only_line",
                "content": " this whole line is comment"
            }
        ],
        "notes": "Comment-only lines vanish; adjacent real lines are separated by a single space as usual."
    }
]

# Complex comment scenarios
COMMENT_COMPLEX_TESTS = [
    {
        "id": "in_argument",
        "description": "Comment inside a brace-delimited argument — comment removed before argument parsing completes.",
        "input": r"""\textbf{Hello % comment
world}""",
        "expected_output": r"\textbf{Hello world}",
        "expected_comments": [
            {
                "start": 14,  # Position of %
                "end": 23,    # End of line inside braces (length of "\textbf{Hello % comment")
                "comment_type": "inline",
                "content": " comment"
            }
        ],
        "notes": "Comments vanish before argument parsing, so the argument sees 'Hello world'."
    },
    {
        "id": "after_begin_environment",
        "description": "Use % to prevent spurious space after \\begin{...}.",
        "input": r"""\begin{itemize}%
\item First
\end{itemize}""",
        "expected_output": r"""\begin{itemize}\item First
\end{itemize}""",
        "expected_comments": [
            {
                "start": 15,  # Position of %
                "end": 16,    # End of first line (length of "\begin{itemize}%")
                "comment_type": "line_continuation",
                "content": ""
            }
        ],
        "notes": "The % prevents a newline-space token after \\begin{itemize} which might otherwise produce unwanted glue."
    },
    {
        "id": "macro_name_split",
        "description": "Splitting a control sequence name across a comment/newline.",
        "input": r"""\newcommand{\foo}{X}
\fo%
o""",
        "expected_output": r"""\newcommand{\foo}{X}
\foo""",
        "expected_comments": [
            {
                "start": 24,  # Position of % (21 + 3)
                "end": 25,    # End of second line (length of "\fo%")
                "comment_type": "line_continuation",
                "content": ""
            }
        ],
        "notes": "The % removes the newline; the tokens concatenated form the control sequence \\foo — this is valid."
    },
    {
        "id": "multiple_comments_and_spaces",
        "description": "Multiple comments, some with spaces after %, all removed.",
        "input": r"""A % first
B % second
C""",
        "expected_output": "A B C",
        "expected_comments": [
            {
                "start": 2,   # Position of first %
                "end": 9,     # End of first line (length of "A % first")
                "comment_type": "inline",
                "content": " first"
            },
            {
                "start": 12,  # Position of second % (10 + 2)
                "end": 20,    # End of second line (length of "B % second")
                "comment_type": "inline",
                "content": " second"
            }
        ],
        "notes": "Each comment removes text upto end-of-line; newlines become spaces between the remaining tokens."
    }
]

# Edge cases and special scenarios
COMMENT_EDGE_TESTS = [
    {
        "id": "percent_in_math_mode",
        "description": "Comment works the same in math mode; % removes rest of line, newline swallowed.",
        "input": r"""This is inline math $a % comment
+b$ done""",
        "expected_output": r"This is inline math $a +b$ done",
        "expected_comments": [
            {
                "start": 22,  # Position of %
                "end": 32,    # End of first line
                "comment_type": "inline",
                "content": " comment"
            }
        ],
        "notes": "Comments are removed in math mode just like in text mode; be careful with line breaks in displayed math too."
    },
    {
        "id": "after_command_with_space_token",
        "description": "Trailing spaces from source after control sequence can be suppressed with %.",
        "input": r"""\texttt{X} % comment
Y""",
        "expected_output": r"\texttt{X} Y",
        "expected_comments": [
            {
                "start": 11,  # Position of %
                "end": 21,    # End of first line
                "comment_type": "inline",
                "content": " comment"
            }
        ],
        "notes": "Without the % the linebreak would normally become a space; here % removes comment and subsequent newline becomes a single space."
    },
    {
        "id": "comment_between_args",
        "description": "Comment between brace groups for multi-argument macros; newline removed by % keeps arguments adjacent.",
        "input": r"""\pair{a}% 
{b}""",
        "expected_output": r"\pair{a}{b}",
        "expected_comments": [
            {
                "start": 8,   # Position of %
                "end": 10,    # End of first line (including space after %)
                "comment_type": "line_continuation",
                "content": " "
            }
        ],
        "notes": "Useful to place % to avoid spurious spaces/newlines between macro arguments."
    },
    {
        "id": "comment_followed_by_space_characters",
        "description": "% followed by spaces: they are part of the comment and removed.",
        "input": r"""Start %    spaced comment
End""",
        "expected_output": "Start End",
        "expected_comments": [
            {
                "start": 6,   # Position of %
                "end": 26,    # End of first line
                "comment_type": "inline",
                "content": "    spaced comment"
            }
        ],
        "notes": "All characters after % on the same line (including spaces) are removed."
    },
    {
        "id": "percent_at_eof",
        "description": "Comment at end of file with no newline: still removes until EOF.",
        "input": r"""Hello
% final comment""",
        "expected_output": "Hello",
        "expected_comments": [
            {
                "start": 6,   # Position of %
                "end": 21,    # End of file
                "comment_type": "comment_only_line",
                "content": " final comment"
            }
        ],
        "notes": "A trailing comment without a final newline removes the remainder of the file from that point."
    }
]

# Verbatim and special environment tests
COMMENT_VERBATIM_TESTS = [
    {
        "id": "verbatim_environment",
        "description": "In verbatim-like environments, % is ordinary — not a comment (catcode changed).",
        "input": r"""\begin{verbatim}
% not a comment here
\end{verbatim}""",
        "expected_output": r"""\begin{verbatim}
% not a comment here
\end{verbatim}""",
        "expected_comments": [],  # No comments detected in verbatim
        "notes": "Packages like verbatim/lstlisting change catcodes so % is printed literally. The expected string shows verbatim body preserved (newlines preserved inside verbatim)."
    },
    {
        "id": "verbatim_with_external_comment",
        "description": "Comments outside verbatim are still processed normally.",
        "input": r"""Before % comment
\begin{verbatim}
% not a comment here
\end{verbatim}
After % another comment
""",
        "expected_output": r"""Before \begin{verbatim}
% not a comment here
\end{verbatim}
After """,
        "expected_comments": [
            {
                "start": 7,   # Position of first %
                "end": 16,    # End of first line
                "comment_type": "inline",
                "content": " comment"
            },
            {
                "start": 76,  # Position of % after \end{verbatim}
                "end": 93,    # End of last content line
                "comment_type": "inline",
                "content": " another comment"
            }
        ],
        "notes": "Comments outside verbatim environments are processed normally, only content inside verbatim is protected."
    }
]

# Catcode and advanced tests
COMMENT_ADVANCED_TESTS = [
    {
        "id": "catcode_change_percent_literal",
        "description": "If catcode of % is changed earlier, it may be ordinary char; test for that.",
        "input": r"""\catcode`\%=12 % make % a printable char
% now a comment? no
\%""",
        "expected_output": r"\catcode`\%=12 \% ",
        "expected_comments": [
            {
                "start": 14,  # Position of % in first line
                "end": 42,    # End of first line
                "comment_type": "inline",
                "content": " make % a printable char"
            }
        ],
        "notes": "If you change the catcode of % to 12 (other), later % is not a comment; this is advanced and rare. Ordering matters (catcode must be changed before the % you expect to be literal). Note: This test case assumes we don't implement full catcode parsing."
    },
    {
        "id": "comment_in_optional_arg",
        "description": "Comments inside optional arguments (square brackets) are removed before parsing.",
        "input": r"""\includegraphics[width=3cm %comment
]{foo}""",
        "expected_output": r"\includegraphics[width=3cm]{foo}",
        "expected_comments": [
            {
                "start": 27,  # Position of %
                "end": 36,    # End of first line
                "comment_type": "inline",
                "content": "comment"
            }
        ],
        "notes": "Comments vanish before LaTeX reads the optional argument; watch for swallowed newlines if % is at line end."
    }
]

# Error and malformed input tests
COMMENT_ERROR_TESTS = [
    {
        "id": "empty_string",
        "description": "Empty string should return empty result.",
        "input": "",
        "expected_output": "",
        "expected_comments": [],
        "notes": "Edge case: empty input."
    },
    {
        "id": "only_percent",
        "description": "String with only % character.",
        "input": "%",
        "expected_output": "",
        "expected_comments": [
            {
                "start": 0,
                "end": 1,
                "comment_type": "comment_only_line",
                "content": ""
            }
        ],
        "notes": "Single % removes everything to end of line/file."
    },
    {
        "id": "escaped_percent_only",
        "description": "String with only escaped percent.",
        "input": r"\%",
        "expected_output": r"\%",
        "expected_comments": [],
        "notes": "Escaped % should not be treated as comment."
    },
    {
        "id": "multiple_escapes",
        "description": "Multiple backslashes before percent.",
        "input": r"\\% comment",
        "expected_output": r"\\",
        "expected_comments": [
            {
                "start": 2,
                "end": 11,
                "comment_type": "inline",
                "content": " comment"
            }
        ],
        "notes": "Even number of backslashes means % is not escaped."
    }
]

# Integration tests combining multiple features
COMMENT_INTEGRATION_TESTS = [
    {
        "id": "complex_document_structure",
        "description": "Complex document with multiple comment types and environments.",
        "input": r"""\documentclass{article} % document class
\usepackage{listings}%
\begin{document}
Hello % inline comment
world %
test
\begin{verbatim}
% this is literal
\end{verbatim}
% final comment only line
\end{document}""",
        "expected_output": r"\documentclass{article} \usepackage{listings}\begin{document}\nHello worldtest\n\begin{verbatim}\n% this is literal\n\end{verbatim}\n\end{document}",
        "expected_comments": [
            {"start": 24, "end": 40, "comment_type": "inline", "content": " document class"},
            {"start": 58, "end": 59, "comment_type": "line_continuation", "content": ""},
            {"start": 81, "end": 98, "comment_type": "inline", "content": " inline comment"},
            {"start": 105, "end": 106, "comment_type": "line_continuation", "content": ""},
            {"start": 147, "end": 170, "comment_type": "comment_only_line", "content": " final comment only line"}
        ],
        "notes": "Complex integration test with various comment scenarios in a realistic document structure."
    }
]

# Helper method test cases
COMMENT_ESCAPE_DETECTION_TRUE_TESTS = [
    {
        "id": "basic_escaped",
        "description": "Basic escaped percent",
        "text": r"\%",
        "position": 1,
        "expected": True
    },
    {
        "id": "escaped_in_middle",
        "description": "Escaped percent in middle of text",
        "text": r"text\%more",
        "position": 5,
        "expected": True
    },
    {
        "id": "odd_backslashes_3",
        "description": "Odd number of backslashes (3)",
        "text": r"\\\%",
        "position": 3,
        "expected": True
    },
    {
        "id": "odd_backslashes_5",
        "description": "Odd number of backslashes (5)",
        "text": r"\\\\\%",
        "position": 5,
        "expected": True
    }
]

COMMENT_ESCAPE_DETECTION_FALSE_TESTS = [
    {
        "id": "no_escape",
        "description": "No escape at start",
        "text": r"%",
        "position": 0,
        "expected": False
    },
    {
        "id": "no_escape_end",
        "description": "No escape at end",
        "text": r"text%",
        "position": 4,
        "expected": False
    },
    {
        "id": "even_backslashes_2",
        "description": "Even number of backslashes (2)",
        "text": r"\\%",
        "position": 2,
        "expected": False
    },
    {
        "id": "even_backslashes_4",
        "description": "Even number of backslashes (4)",
        "text": r"\\\\%",
        "position": 4,
        "expected": False
    },
    {
        "id": "even_with_space",
        "description": "Even number with space",
        "text": r"text \\%",
        "position": 6,
        "expected": False
    }
]

COMMENT_LINE_CONTINUATION_TESTS = [
    {
        "id": "basic_continuation",
        "description": "Basic line continuation",
        "input": r"""Hello %
world""",
        "expected": "Hello world"
    },
    {
        "id": "multiple_continuations",
        "description": "Multiple line continuations",
        "input": r"""A%
B%
C""",
        "expected": "ABC"
    }
]

# Additional test cases to achieve 100% coverage
COMMENT_COVERAGE_TESTS = [
    {
        "id": "line_continuation_no_newline",
        "description": "Line continuation comment without following newline",
        "input": "text%",
        "expected": "text"
    },
    {
        "id": "comment_after_whitespace",
        "description": "Comment after whitespace character",
        "input": "text % comment",
        "expected": "text "
    },
    {
        "id": "percent_at_end_of_file",
        "description": "Percent sign at end of file for line continuation",
        "input": "line1\nline2%",
        "expected": "line1\nline2"
    }
]

COMMENT_VERBATIM_REGION_TESTS = [
    {
        "id": "basic_verbatim",
        "description": "Basic verbatim region detection",
        "input": r"""\begin{verbatim}
content here
\end{verbatim}""",
        "expected_regions": 1,
        "expected_content": "content here"
    },
    {
        "id": "multiple_verbatim",
        "description": "Multiple verbatim regions",
        "input": r"""Before
\begin{verbatim}
first
\end{verbatim}
Middle
\begin{lstlisting}
second
\end{lstlisting}
After""",
        "expected_regions": 2
    }
]

# All test collections
ALL_COMMENT_TESTS = (
    COMMENT_BASIC_TESTS +
    COMMENT_COMPLEX_TESTS + 
    COMMENT_EDGE_TESTS +
    COMMENT_VERBATIM_TESTS +
    COMMENT_ADVANCED_TESTS +
    COMMENT_ERROR_TESTS +
    COMMENT_INTEGRATION_TESTS
)