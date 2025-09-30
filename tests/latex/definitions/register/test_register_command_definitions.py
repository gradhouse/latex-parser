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
    register_greek_letter_commands,
    register_binary_operation_commands,
    register_relation_commands,
    register_arrow_commands,
    register_misc_symbol_commands,
    register_variable_sized_symbol_commands,
    register_log_like_function_commands,
    register_math_accent_commands,
    register_math_enclosure_commands,
    register_text_accent_commands,
    register_text_symbol_commands,
    register_text_spacing_commands,
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


class TestRegisterGreekLetterCommands:
    """Test register_greek_letter_commands function."""

    def test_registers_expected_greek_letter_commands(self):
        """Test that all expected Greek letter commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_greek_letter_commands(registry)
        
        expected_commands = {
            '\\Delta', '\\Gamma', '\\Lambda', '\\Omega', '\\Phi', '\\Pi', '\\Psi', '\\Sigma', '\\Theta', '\\Upsilon', '\\Xi', 
            '\\alpha', '\\beta', '\\chi', '\\delta', '\\epsilon', '\\eta', '\\gamma', '\\iota', '\\kappa', '\\lambda', 
            '\\mu', '\\nu', '\\omega', '\\phi', '\\pi', '\\psi', '\\rho', '\\sigma', '\\tau', '\\theta', '\\upsilon', 
            '\\varepsilon', '\\varphi', '\\varpi', '\\varrho', '\\varsigma', '\\vartheta', '\\xi', '\\zeta'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"


class TestRegisterBinaryOperationCommands:
    """Test register_binary_operation_commands function."""

    def test_registers_expected_binary_operation_commands(self):
        """Test that all expected binary operation commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_binary_operation_commands(registry)
        
        expected_commands = {
            '\\amalg', '\\ast', '\\bigcirc', '\\bigtriangledown', '\\bigtriangleup', '\\bullet', '\\cap', '\\cdot', 
            '\\circ', '\\cup', '\\dagger', '\\ddagger', '\\diamond', '\\div', '\\lhd', '\\mp', '\\odot', '\\ominus', 
            '\\oplus', '\\oslash', '\\otimes', '\\pm', '\\rhd', '\\setminus', '\\sqcap', '\\sqcup', '\\star', 
            '\\times', '\\triangleleft', '\\triangleright', '\\unlhd', '\\unrhd', '\\uplus', '\\vee', '\\wedge', '\\wr'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"


class TestRegisterRelationCommands:
    """Test register_relation_commands function."""

    def test_registers_expected_relation_commands(self):
        """Test that all expected relation commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_relation_commands(registry)
        
        expected_commands = {
            '\\Join', '\\approx', '\\asymp', '\\bowtie', '\\cong', '\\dashv', '\\doteq', '\\equiv', '\\frown', 
            '\\geq', '\\gg', '\\in', '\\leq', '\\ll', '\\mid', '\\models', '\\neq', '\\ni', '\\notin', 
            '\\parallel', '\\perp', '\\prec', '\\preceq', '\\propto', '\\sim', '\\simeq', '\\smile', 
            '\\sqsubset', '\\sqsubseteq', '\\sqsupset', '\\sqsupseteq', '\\subset', '\\subseteq', '\\succ', 
            '\\succeq', '\\vdash'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"


class TestRegisterArrowCommands:
    """Test register_arrow_commands function."""

    def test_registers_expected_arrow_commands(self):
        """Test that all expected arrow commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_arrow_commands(registry)
        
        expected_commands = {
            '\\Downarrow', '\\Leftarrow', '\\Leftrightarrow', '\\Longleftarrow', '\\Longleftrightarrow', 
            '\\Longrightarrow', '\\Rightarrow', '\\Uparrow', '\\Updownarrow', '\\downarrow', '\\hookleftarrow', 
            '\\hookrightarrow', '\\leadsto', '\\leftarrow', '\\leftharpoondown', '\\leftharpoonup', 
            '\\leftrightarrow', '\\longleftarrow', '\\longleftrightarrow', '\\longmapsto', '\\longrightarrow', 
            '\\mapsto', '\\nearrow', '\\nwarrow', '\\rightarrow', '\\rightharpoondown', '\\rightharpoonup', 
            '\\rightleftharpoons', '\\searrow', '\\swarrow', '\\uparrow', '\\updownarrow'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"


class TestRegisterMiscSymbolCommands:
    """Test register_misc_symbol_commands function."""

    def test_registers_expected_misc_symbol_commands(self):
        """Test that all expected miscellaneous symbol commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_misc_symbol_commands(registry)
        
        expected_commands = {
            '\\Box', '\\Diamond', '\\Im', '\\Re', '\\aleph', '\\angle', '\\backslash', '\\bot', '\\clubsuit', 
            '\\diamondsuit', '\\ell', '\\emptyset', '\\exists', '\\flat', '\\forall', '\\hbar', '\\heartsuit', 
            '\\imath', '\\infty', '\\jmath', '\\mho', '\\nabla', '\\natural', '\\neg', '\\partial', '\\prime', 
            '\\sharp', '\\spadesuit', '\\surd', '\\top', '\\triangle', '\\wp', '\\|'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"


class TestRegisterVariableSizedSymbolCommands:
    """Test register_variable_sized_symbol_commands function."""

    def test_registers_expected_variable_sized_symbol_commands(self):
        """Test that all expected variable-sized symbol commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_variable_sized_symbol_commands(registry)
        
        expected_commands = {
            '\\bigcap', '\\bigcup', '\\bigodot', '\\bigoplus', '\\bigotimes', '\\biguplus', '\\bigvee', 
            '\\bigwedge', '\\coprod', '\\int', '\\oint', '\\prod', '\\sum'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"


class TestRegisterLogLikeFunctionCommands:
    """Test register_log_like_function_commands function."""

    def test_registers_expected_log_like_function_commands(self):
        """Test that all expected log-like function commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_log_like_function_commands(registry)
        
        expected_commands = {
            '\\Pr', '\\arccos', '\\arcsin', '\\arctan', '\\arg', '\\bmod', '\\cos', '\\cosh', '\\cot', '\\coth', 
            '\\csc', '\\deg', '\\det', '\\dim', '\\exp', '\\gcd', '\\hom', '\\inf', '\\ker', '\\lg', '\\lim', 
            '\\liminf', '\\limsup', '\\ln', '\\log', '\\max', '\\min', '\\pmod', '\\sec', '\\sin', '\\sinh', 
            '\\sup', '\\tan', '\\tanh'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"


class TestRegisterMathAccentCommands:
    """Test register_math_accent_commands function."""

    def test_registers_expected_math_accent_commands(self):
        """Test that all expected math accent commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_math_accent_commands(registry)
        
        expected_commands = {
            '\\acute', '\\bar', '\\breve', '\\check', '\\ddot', '\\dot', '\\grave', 
            '\\hat', '\\tilde', '\\vec', '\\widehat', '\\widetilde'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"


class TestRegisterMathEnclosureCommands:
    """Test register_math_enclosure_commands function."""

    def test_registers_expected_math_enclosure_commands(self):
        """Test that all expected math enclosure commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_math_enclosure_commands(registry)
        
        expected_commands = {
            '\\overbrace', '\\overline', '\\underbrace', '\\underline'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"


class TestRegisterTextAccentCommands:
    """Test register_text_accent_commands function."""

    def test_registers_expected_text_accent_commands(self):
        """Test that all expected text accent commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_text_accent_commands(registry)
        
        expected_commands = {
            '\\"', "\\'", '\\.', '\\=', '\\H', '\\^', '\\`', '\\b', '\\c', '\\d', '\\t', '\\u', '\\v', '\\~'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"


class TestRegisterTextSymbolCommands:
    """Test register_text_symbol_commands function."""

    def test_registers_expected_text_symbol_commands(self):
        """Test that all expected text symbol commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_text_symbol_commands(registry)
        
        expected_commands = {
            '!`', '?`', '\\AA', '\\AE', '\\L', '\\O', '\\OE', '\\P', '\\S', '\\aa', '\\ae', 
            '\\copyright', '\\dag', '\\ddag', '\\l', '\\o', '\\oe', '\\pounds', '\\ss',
            '\\#', '\\$', '\\%', '\\&', '\\_', '\\{', '\\}'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"


class TestRegisterTextSpacingCommands:
    """Test register_text_spacing_commands function."""

    def test_registers_expected_text_spacing_commands(self):
        """Test that all expected text spacing commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_text_spacing_commands(registry)
        
        expected_commands = {
            '\\ ', '\\!', '\\,', '\\:', '\\;'
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
        
        # Combined set of all expected commands from all registration functions
        expected_commands = {
            # Document commands
            '\\documentclass', '\\documentstyle', '\\usepackage', '\\maketitle',
            '\\title', '\\author', '\\date', '\\thanks',
            # Sectioning commands
            '\\part', '\\part*', '\\chapter', '\\chapter*',
            '\\section', '\\section*', '\\subsection', '\\subsection*',
            '\\subsubsection', '\\subsubsection*', '\\paragraph', '\\paragraph*',
            '\\subparagraph', '\\subparagraph*',
            # Greek letter commands
            '\\Delta', '\\Gamma', '\\Lambda', '\\Omega', '\\Phi', '\\Pi', '\\Psi', '\\Sigma', '\\Theta', '\\Upsilon', '\\Xi', 
            '\\alpha', '\\beta', '\\chi', '\\delta', '\\epsilon', '\\eta', '\\gamma', '\\iota', '\\kappa', '\\lambda', 
            '\\mu', '\\nu', '\\omega', '\\phi', '\\pi', '\\psi', '\\rho', '\\sigma', '\\tau', '\\theta', '\\upsilon', 
            '\\varepsilon', '\\varphi', '\\varpi', '\\varrho', '\\varsigma', '\\vartheta', '\\xi', '\\zeta',
            # Binary operation commands
            '\\amalg', '\\ast', '\\bigcirc', '\\bigtriangledown', '\\bigtriangleup', '\\bullet', '\\cap', '\\cdot', 
            '\\circ', '\\cup', '\\dagger', '\\ddagger', '\\diamond', '\\div', '\\lhd', '\\mp', '\\odot', '\\ominus', 
            '\\oplus', '\\oslash', '\\otimes', '\\pm', '\\rhd', '\\setminus', '\\sqcap', '\\sqcup', '\\star', 
            '\\times', '\\triangleleft', '\\triangleright', '\\unlhd', '\\unrhd', '\\uplus', '\\vee', '\\wedge', '\\wr',
            # Relation commands
            '\\Join', '\\approx', '\\asymp', '\\bowtie', '\\cong', '\\dashv', '\\doteq', '\\equiv', '\\frown', 
            '\\geq', '\\gg', '\\in', '\\leq', '\\ll', '\\mid', '\\models', '\\neq', '\\ni', '\\notin', 
            '\\parallel', '\\perp', '\\prec', '\\preceq', '\\propto', '\\sim', '\\simeq', '\\smile', 
            '\\sqsubset', '\\sqsubseteq', '\\sqsupset', '\\sqsupseteq', '\\subset', '\\subseteq', '\\succ', 
            '\\succeq', '\\vdash',
            # Arrow commands
            '\\Downarrow', '\\Leftarrow', '\\Leftrightarrow', '\\Longleftarrow', '\\Longleftrightarrow', 
            '\\Longrightarrow', '\\Rightarrow', '\\Uparrow', '\\Updownarrow', '\\downarrow', '\\hookleftarrow', 
            '\\hookrightarrow', '\\leadsto', '\\leftarrow', '\\leftharpoondown', '\\leftharpoonup', 
            '\\leftrightarrow', '\\longleftarrow', '\\longleftrightarrow', '\\longmapsto', '\\longrightarrow', 
            '\\mapsto', '\\nearrow', '\\nwarrow', '\\rightarrow', '\\rightharpoondown', '\\rightharpoonup', 
            '\\rightleftharpoons', '\\searrow', '\\swarrow', '\\uparrow', '\\updownarrow',
            # Miscellaneous symbol commands
            '\\Box', '\\Diamond', '\\Im', '\\Re', '\\aleph', '\\angle', '\\backslash', '\\bot', '\\clubsuit', 
            '\\diamondsuit', '\\ell', '\\emptyset', '\\exists', '\\flat', '\\forall', '\\hbar', '\\heartsuit', 
            '\\imath', '\\infty', '\\jmath', '\\mho', '\\nabla', '\\natural', '\\neg', '\\partial', '\\prime', 
            '\\sharp', '\\spadesuit', '\\surd', '\\top', '\\triangle', '\\wp', '\\|',
            # Variable-sized symbol commands
            '\\bigcap', '\\bigcup', '\\bigodot', '\\bigoplus', '\\bigotimes', '\\biguplus', '\\bigvee', 
            '\\bigwedge', '\\coprod', '\\int', '\\oint', '\\prod', '\\sum',
            # Log-like function commands
            '\\Pr', '\\arccos', '\\arcsin', '\\arctan', '\\arg', '\\bmod', '\\cos', '\\cosh', '\\cot', '\\coth', 
            '\\csc', '\\deg', '\\det', '\\dim', '\\exp', '\\gcd', '\\hom', '\\inf', '\\ker', '\\lg', '\\lim', 
            '\\liminf', '\\limsup', '\\ln', '\\log', '\\max', '\\min', '\\pmod', '\\sec', '\\sin', '\\sinh', 
            '\\sup', '\\tan', '\\tanh',
            # Math accent commands
            '\\acute', '\\bar', '\\breve', '\\check', '\\ddot', '\\dot', '\\grave', 
            '\\hat', '\\tilde', '\\vec', '\\widehat', '\\widetilde',
            # Math enclosure commands
            '\\overbrace', '\\overline', '\\underbrace', '\\underline',
            # Text accent commands
            '\\"', "\\'", '\\.', '\\=', '\\H', '\\^', '\\`', '\\b', '\\c', '\\d', '\\t', '\\u', '\\v', '\\~',
            # Text symbol commands
            '!`', '?`', '\\AA', '\\AE', '\\L', '\\O', '\\OE', '\\P', '\\S', '\\aa', '\\ae', 
            '\\copyright', '\\dag', '\\ddag', '\\l', '\\o', '\\oe', '\\pounds', '\\ss',
            '\\#', '\\$', '\\%', '\\&', '\\_', '\\{', '\\}',
            # Text spacing commands
            '\\ ', '\\!', '\\,', '\\:', '\\;'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {len(expected_commands)} commands, got {len(registered_keys)}. Missing: {expected_commands - registered_keys}, Extra: {registered_keys - expected_commands}"

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
    
    def test_expected_total_command_count(self):
        """Test that the total number of registered commands matches expectations."""
        registry = CommandDefinitionRegistry()
        register_latex_commands(registry)
        
        # Expected counts based on individual function tests:
        # Document: 8, Sectioning: 14, Greek: 40, Binary: 36, Relation: 36, 
        # Arrow: 32, Misc: 33, Variable-sized: 13, Log-like: 34, Math accent: 12, Math enclosure: 4, Text accent: 14, Text symbol: 26, Text spacing: 5
        expected_total = 8 + 14 + 40 + 36 + 36 + 32 + 33 + 13 + 34 + 12 + 4 + 14 + 26 + 5
        actual_total = len(registry.list_keys())
        
        assert actual_total == expected_total, f"Expected {expected_total} total commands, got {actual_total}"