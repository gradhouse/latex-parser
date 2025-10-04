# File: test_document.py
# Description: Test cases for document input command modernization using fixtures
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import pytest

from latex_parser.latex.elements.document import Document
from tests.latex.fixtures.document_test_cases import (
    DOCUMENT_INPUT_BASIC_TESTS,
    DOCUMENT_INPUT_MULTIPLE_TESTS,
    DOCUMENT_INPUT_COMPLEX_TESTS,
    DOCUMENT_INPUT_EDGE_TESTS
)


class TestDocumentModernizeInputCommands:
    """Test the modernize_input_commands functionality using fixtures."""
    
    @pytest.mark.parametrize("test_case", DOCUMENT_INPUT_BASIC_TESTS)
    def test_basic_input_modernization(self, test_case):
        """Test basic input command modernization."""
        content = test_case["input"]
        expected = test_case["expected"]
        result = Document.modernize_input_commands(content)
        assert result == expected, f"Failed for test case: {test_case['id']} - {test_case['description']}"
    
    @pytest.mark.parametrize("test_case", DOCUMENT_INPUT_MULTIPLE_TESTS)
    def test_multiple_input_commands(self, test_case):
        """Test multiple input command modernization."""
        content = test_case["input"]
        expected = test_case["expected"]
        result = Document.modernize_input_commands(content)
        assert result == expected, f"Failed for test case: {test_case['id']} - {test_case['description']}"
    
    @pytest.mark.parametrize("test_case", DOCUMENT_INPUT_COMPLEX_TESTS)
    def test_complex_content(self, test_case):
        """Test complex content with various scenarios."""
        content = test_case["input"]
        expected = test_case["expected"]
        result = Document.modernize_input_commands(content)
        assert result == expected, f"Failed for test case: {test_case['id']} - {test_case['description']}"
    
    @pytest.mark.parametrize("test_case", DOCUMENT_INPUT_EDGE_TESTS)
    def test_edge_cases(self, test_case):
        """Test edge cases and boundary conditions."""
        content = test_case["input"]
        expected = test_case["expected"]
        result = Document.modernize_input_commands(content)
        assert result == expected, f"Failed for test case: {test_case['id']} - {test_case['description']}"


class TestDocumentInputCommandDetection:
    """Test the internal input command detection methods."""
    
    def test_find_input_commands_basic(self):
        """Test basic input command detection."""
        content = "\\input myfile.tex"
        commands = Document._find_input_commands(content)
        
        assert len(commands) == 1
        assert commands[0]['start'] == 0
        assert commands[0]['argument'] == 'myfile.tex'
        assert commands[0]['needs_modernization'] == True
    
    def test_find_input_commands_with_braces(self):
        """Test input command detection with braces."""
        content = "\\input{myfile.tex}"
        commands = Document._find_input_commands(content)
        
        assert len(commands) == 1
        assert commands[0]['argument'] == '{myfile.tex}'
        assert commands[0]['needs_modernization'] == False
    
    def test_find_input_commands_with_whitespace(self):
        """Test input command detection with whitespace."""
        content = "\\input   myfile.tex"
        commands = Document._find_input_commands(content)
        
        assert len(commands) == 1
        assert commands[0]['whitespace'] == '   '
        assert commands[0]['argument'] == 'myfile.tex'
        assert commands[0]['needs_modernization'] == True
    
    def test_build_input_replacements(self):
        """Test building replacement map."""
        commands = [
            {
                'start': 0,
                'end': 15,
                'argument': 'myfile.tex',
                'needs_modernization': True
            },
            {
                'start': 20,
                'end': 37,
                'argument': '{otherfile.tex}',
                'needs_modernization': False
            }
        ]
        
        replacements = Document._build_input_replacements(commands)
        
        assert len(replacements) == 1
        assert 0 in replacements
        assert replacements[0] == ('\\input{myfile.tex}', 15)
        assert 20 not in replacements
    
    def test_escaped_command_detection(self):
        """Test escaped command detection."""
        # Test escaped command
        content = "\\\\input test.tex"
        commands = Document._find_input_commands(content)
        assert len(commands) == 0  # Should find no commands because it's escaped
        
        # Test non-escaped command
        content = "\\input test.tex"
        commands = Document._find_input_commands(content) 
        assert len(commands) == 1  # Should find the command