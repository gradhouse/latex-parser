# File: test_register_command_definitions.py
# Description: Unit tests for register_command_definitions.py
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import pytest
from latex_parser.latex.definitions.command_definition_registry import CommandDefinitionRegistry
from latex_parser.latex.definitions.register.register_command_definitions import (
    register_document_commands,
    register_sectioning_commands,
    register_latex_commands
)


class TestRegisterDocumentCommands:
    """Test register_document_commands function."""

    def test_registers_expected_document_commands(self):
        """Test that all expected document commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_document_commands(registry)
        
        expected_commands = {
            '\\documentclass', '\\documentstyle', '\\usepackage', '\\maketitle',
            '\\title', '\\author', '\\date', '\\thanks'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"


class TestRegisterSectioningCommands:
    """Test register_sectioning_commands function."""

    def test_registers_expected_sectioning_commands(self):
        """Test that all expected sectioning commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_sectioning_commands(registry)
        
        expected_commands = {
            '\\part', '\\part*', '\\chapter', '\\chapter*',
            '\\section', '\\section*', '\\subsection', '\\subsection*',
            '\\subsubsection', '\\subsubsection*', '\\paragraph', '\\paragraph*',
            '\\subparagraph', '\\subparagraph*'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"


class TestRegisterLatexCommands:
    """Test register_latex_commands function."""

    def test_registers_all_expected_commands(self):
        """Test that register_latex_commands registers all expected commands and only those."""
        registry = CommandDefinitionRegistry()
        register_latex_commands(registry)
        
        # Combined set of all expected commands
        expected_commands = {
            # Document commands
            '\\documentclass', '\\documentstyle', '\\usepackage', '\\maketitle',
            '\\title', '\\author', '\\date', '\\thanks',
            # Sectioning commands
            '\\part', '\\part*', '\\chapter', '\\chapter*',
            '\\section', '\\section*', '\\subsection', '\\subsection*',
            '\\subsubsection', '\\subsubsection*', '\\paragraph', '\\paragraph*',
            '\\subparagraph', '\\subparagraph*'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"

    def test_command_consistency_across_runs(self):
        """Test that the same commands are registered consistently across multiple runs."""
        # First run
        registry1 = CommandDefinitionRegistry()
        register_latex_commands(registry1)
        keys1 = set(registry1.list_keys())
        
        # Second run
        registry2 = CommandDefinitionRegistry()
        register_latex_commands(registry2)
        keys2 = set(registry2.list_keys())
        
        # Should be identical
        assert keys1 == keys2, "Command registration is not consistent across runs"