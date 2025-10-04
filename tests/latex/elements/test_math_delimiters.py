# File: test_math_delimiters.py
# Description: Tests for math delimiter detection methods
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import pytest

from latex_parser.latex.elements.command import Command
from tests.latex.fixtures.math_delimiter_test_cases import (
    MATH_DELIMITER_BASIC_TESTS,
    MATH_DELIMITER_COMPLEX_TESTS, 
    MATH_DELIMITER_EDGE_TESTS,
    DISPLAY_MATH_TESTS,
    INLINE_MATH_TESTS
)


class TestMathDelimiters:
    """Test math delimiter detection methods."""
    
    @pytest.mark.parametrize("test_case", MATH_DELIMITER_BASIC_TESTS, ids=lambda x: x['id'])
    def test_find_math_delimiters_basic(self, test_case):
        """Test basic math delimiter detection."""
        result = Command.find_math_delimiters(test_case["input"])
        assert result == test_case["expected"], f"Failed for {test_case['id']}: {test_case['description']}"
    
    @pytest.mark.parametrize("test_case", MATH_DELIMITER_COMPLEX_TESTS, ids=lambda x: x['id'])
    def test_find_math_delimiters_complex(self, test_case):
        """Test complex math delimiter scenarios."""
        result = Command.find_math_delimiters(test_case["input"])
        assert result == test_case["expected"], f"Failed for {test_case['id']}: {test_case['description']}"
    
    @pytest.mark.parametrize("test_case", MATH_DELIMITER_EDGE_TESTS, ids=lambda x: x['id'])
    def test_find_math_delimiters_edge_cases(self, test_case):
        """Test edge cases for math delimiter detection."""
        result = Command.find_math_delimiters(test_case["input"])
        assert result == test_case["expected"], f"Failed for {test_case['id']}: {test_case['description']}"
    
    @pytest.mark.parametrize("test_case", DISPLAY_MATH_TESTS, ids=lambda x: x['id'])
    def test_find_display_math_delimiters(self, test_case):
        """Test display math delimiter filtering."""
        result = Command.find_display_math_delimiters(test_case["input"])
        assert result == test_case["expected"], f"Failed for {test_case['id']}: {test_case['description']}"
    
    @pytest.mark.parametrize("test_case", INLINE_MATH_TESTS, ids=lambda x: x['id'])
    def test_find_inline_math_delimiters(self, test_case):
        """Test inline math delimiter filtering."""
        result = Command.find_inline_math_delimiters(test_case["input"])
        assert result == test_case["expected"], f"Failed for {test_case['id']}: {test_case['description']}"


class TestMathDelimiterEdgeCases:
    """Test specific edge cases and error conditions."""
    
    def test_consecutive_dollars(self):
        """Test handling of consecutive dollar signs."""
        # Should prioritize $$ when possible
        result = Command.find_math_delimiters("$$$")
        expected = [
            {"command_name": "$$", "start": 0, "end": 2},
            {"command_name": "$", "start": 2, "end": 3}
        ]
        assert result == expected
    
    def test_escaped_vs_unescaped_mixed(self):
        """Test mixture of escaped and unescaped delimiters."""
        text = "\\$5 costs $x$ dollars and \\$y is not math"
        result = Command.find_math_delimiters(text)
        expected = [
            {"command_name": "$", "start": 10, "end": 11},
            {"command_name": "$", "start": 12, "end": 13}
        ]
        assert result == expected
    
    def test_backslash_counting(self):
        """Test proper backslash counting for escape detection."""
        # Even number of backslashes means $ is not escaped
        text = "\\\\$math$"
        result = Command.find_math_delimiters(text) 
        expected = [
            {"command_name": "$", "start": 2, "end": 3},
            {"command_name": "$", "start": 7, "end": 8}
        ]
        assert result == expected
        
        # Odd number of backslashes means $ is escaped
        text = "\\\\\\$not math"
        result = Command.find_math_delimiters(text)
        expected = []
        assert result == expected

    def test_performance_with_large_text(self):
        """Test performance with larger text containing many delimiters."""
        # Create a large text with many math delimiters
        large_text = "Text with math: " + "$x$ " * 1000 + "end"
        result = Command.find_math_delimiters(large_text)
        
        # Should find 2000 delimiters (1000 opening, 1000 closing)
        assert len(result) == 2000
        assert all(d["command_name"] == "$" for d in result)
    
    def test_all_delimiter_types_together(self):
        """Test all delimiter types in one string."""
        text = "$a$ \\(b\\) $$c$$ \\[d\\] more $e$ and \\(f\\)"
        result = Command.find_math_delimiters(text)
        
        expected_commands = ["$", "$", "\\(", "\\)", "$$", "$$", "\\[", "\\]", "$", "$", "\\(", "\\)"]
        actual_commands = [d["command_name"] for d in result]
        assert actual_commands == expected_commands
    
    def test_dollar_at_beginning_of_string(self):
        """Test dollar sign at very beginning of string."""
        text = "$x$"
        result = Command.find_math_delimiters(text)
        expected = [
            {"command_name": "$", "start": 0, "end": 1},
            {"command_name": "$", "start": 2, "end": 3}
        ]
        assert result == expected
    
    def test_complex_escape_scenarios(self):
        """Test complex escape scenarios."""
        # Multiple consecutive backslashes
        text = "\\\\\\\\$math$ and \\\\\\\\\\$escaped"
        result = Command.find_math_delimiters(text)
        expected = [
            {"command_name": "$", "start": 4, "end": 5},
            {"command_name": "$", "start": 9, "end": 10}
        ]
        assert result == expected