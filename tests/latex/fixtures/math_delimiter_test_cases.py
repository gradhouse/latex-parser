# File: math_delimiter_test_cases.py
# Description: Test case fixtures for math delimiter detection
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

# Basic math delimiter tests
MATH_DELIMITER_BASIC_TESTS = [
    {
        "id": "single_dollar_inline",
        "description": "Single dollar signs for inline math",
        "input": "Text $x = 1$ more text",
        "expected": [
            {"command_name": "$", "start": 5, "end": 6},
            {"command_name": "$", "start": 11, "end": 12}
        ]
    },
    {
        "id": "double_dollar_display", 
        "description": "Double dollar signs for display math",
        "input": "Text $$x = 1$$ more text",
        "expected": [
            {"command_name": "$$", "start": 5, "end": 7},
            {"command_name": "$$", "start": 12, "end": 14}
        ]
    },
    {
        "id": "parenthesis_inline",
        "description": "Parenthesis delimiters for inline math",
        "input": "Text \\(x = 1\\) more text",
        "expected": [
            {"command_name": "\\(", "start": 5, "end": 7},
            {"command_name": "\\)", "start": 12, "end": 14}
        ]
    },
    {
        "id": "bracket_display",
        "description": "Bracket delimiters for display math", 
        "input": "Text \\[x = 1\\] more text",
        "expected": [
            {"command_name": "\\[", "start": 5, "end": 7},
            {"command_name": "\\]", "start": 12, "end": 14}
        ]
    },
    {
        "id": "escaped_dollar",
        "description": "Escaped dollar sign should not be matched",
        "input": "Price is \\$5 and $x = 1$",
        "expected": [
            {"command_name": "$", "start": 17, "end": 18},
            {"command_name": "$", "start": 23, "end": 24}
        ]
    }
]

# Complex delimiter tests
MATH_DELIMITER_COMPLEX_TESTS = [
    {
        "id": "mixed_delimiters",
        "description": "Mixed inline and display math delimiters",
        "input": "Inline $a$ and \\(b\\) and display $$c$$ and \\[d\\]",
        "expected": [
            {"command_name": "$", "start": 7, "end": 8},
            {"command_name": "$", "start": 9, "end": 10},
            {"command_name": "\\(", "start": 15, "end": 17},
            {"command_name": "\\)", "start": 18, "end": 20},
            {"command_name": "$$", "start": 33, "end": 35},
            {"command_name": "$$", "start": 36, "end": 38},
            {"command_name": "\\[", "start": 43, "end": 45},
            {"command_name": "\\]", "start": 46, "end": 48}
        ]
    },
    {
        "id": "adjacent_delimiters",
        "description": "Adjacent math delimiters",
        "input": "$$a$$$$b$$",
        "expected": [
            {"command_name": "$$", "start": 0, "end": 2},
            {"command_name": "$$", "start": 3, "end": 5},
            {"command_name": "$$", "start": 5, "end": 7},
            {"command_name": "$$", "start": 8, "end": 10}
        ]
    },
    {
        "id": "dollar_vs_double_dollar",
        "description": "Ensure $$ takes precedence over $ $",
        "input": "$$$x$$$",
        "expected": [
            {"command_name": "$$", "start": 0, "end": 2},
            {"command_name": "$", "start": 2, "end": 3},
            {"command_name": "$$", "start": 4, "end": 6},
            {"command_name": "$", "start": 6, "end": 7}
        ]
    },
    {
        "id": "multiple_escapes",
        "description": "Multiple backslashes with dollar signs - middle dollar is escaped",
        "input": "\\\\$a$ and \\\\\\$b and \\\\\\\\$c$",
        "expected": [
            {"command_name": "$", "start": 2, "end": 3},
            {"command_name": "$", "start": 4, "end": 5},
            {"command_name": "$", "start": 24, "end": 25},
            {"command_name": "$", "start": 26, "end": 27}
        ]
    }
]

# Edge case tests
MATH_DELIMITER_EDGE_TESTS = [
    {
        "id": "empty_string",
        "description": "Empty string should return empty list",
        "input": "",
        "expected": []
    },
    {
        "id": "no_delimiters",
        "description": "Text with no math delimiters",
        "input": "Just regular text with no math",
        "expected": []
    },
    {
        "id": "only_escaped_dollars",
        "description": "Only escaped dollar signs",
        "input": "Price \\$10 and cost \\$20",
        "expected": []
    },
    {
        "id": "at_start_and_end",
        "description": "Delimiters at start and end of string",
        "input": "$$math content$$",
        "expected": [
            {"command_name": "$$", "start": 0, "end": 2},
            {"command_name": "$$", "start": 14, "end": 16}
        ]
    },
    {
        "id": "single_character_delimiters",
        "description": "Single character strings with delimiters",
        "input": "$",
        "expected": [
            {"command_name": "$", "start": 0, "end": 1}
        ]
    }
]

# Tests for specialized methods
DISPLAY_MATH_TESTS = [
    {
        "id": "only_display_delimiters",
        "description": "Should only return display math delimiters",
        "input": "Inline $a$ and \\(b\\) and display $$c$$ and \\[d\\]",
        "expected": [
            {"command_name": "$$", "start": 33, "end": 35},
            {"command_name": "$$", "start": 36, "end": 38},
            {"command_name": "\\[", "start": 43, "end": 45},
            {"command_name": "\\]", "start": 46, "end": 48}
        ]
    }
]

INLINE_MATH_TESTS = [
    {
        "id": "only_inline_delimiters", 
        "description": "Should only return inline math delimiters",
        "input": "Inline $a$ and \\(b\\) and display $$c$$ and \\[d\\]",
        "expected": [
            {"command_name": "$", "start": 7, "end": 8},
            {"command_name": "$", "start": 9, "end": 10},
            {"command_name": "\\(", "start": 15, "end": 17},
            {"command_name": "\\)", "start": 18, "end": 20}
        ]
    }
]