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
    register_alignment_commands,
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
    register_delimiter_commands,
    register_bibliography_citation_commands,
    register_command_definition_commands,
    register_environment_definition_commands,
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


class TestRegisterAlignmentCommands:
    """Test register_alignment_commands function."""

    def test_registers_expected_alignment_commands(self):
        """Test that all expected alignment commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_alignment_commands(registry)

        expected_commands = {
            '\\centering', '\\raggedright', '\\raggedleft'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"

    def test_alignment_commands_have_correct_type(self):
        """Test that alignment commands have correct command type."""
        registry = CommandDefinitionRegistry()
        register_alignment_commands(registry)

        # Check that the alignment commands have correct command_type
        for command_name in ['\\centering', '\\raggedright', '\\raggedleft']:
            entry = registry.get_entry(command_name)
            data = entry.as_dict()
            assert data['command_type'] == 'alignment', f"Command {command_name} should have alignment type but has {data['command_type']}"
            assert 'paragraph' in data['modes'], f"Command {command_name} should include paragraph mode but has {data['modes']}"
            assert data['robustness'] == 'robust', f"Command {command_name} should be robust but has {data['robustness']}"


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
            '\\Leftarrow', '\\Leftrightarrow', '\\Longleftarrow', '\\Longleftrightarrow',
            '\\Longrightarrow', '\\Rightarrow', '\\hookleftarrow',
            '\\hookrightarrow', '\\leadsto', '\\leftarrow', '\\leftharpoondown', '\\leftharpoonup',
            '\\leftrightarrow', '\\longleftarrow', '\\longleftrightarrow', '\\longmapsto', '\\longrightarrow',
            '\\mapsto', '\\nearrow', '\\nwarrow', '\\rightarrow', '\\rightharpoondown', '\\rightharpoonup',
            '\\rightleftharpoons', '\\searrow', '\\swarrow'
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
            '\\Box', '\\Diamond', '\\Im', '\\Re', '\\aleph', '\\angle', '\\bot', '\\clubsuit',
            '\\diamondsuit', '\\ell', '\\emptyset', '\\exists', '\\flat', '\\forall', '\\hbar', '\\heartsuit',
            '\\imath', '\\infty', '\\jmath', '\\mho', '\\nabla', '\\natural', '\\neg', '\\partial', '\\prime',
            '\\sharp', '\\spadesuit', '\\surd', '\\top', '\\triangle', '\\wp'
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
            '\\#', '\\$', '\\%', '\\&', '\\_'
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
            # Alignment commands
            '\\centering', '\\raggedright', '\\raggedleft',
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
            '\\ ', '\\!', '\\,', '\\:', '\\;',
            # Delimiter commands
            '(', ')', '[', ']', '|', '\\{', '\\}', '\\bigl', '\\bigr', '\\Bigl', '\\Bigr', '\\biggl', '\\biggr', 
            '\\Biggl', '\\Biggr', '\\left', '\\right', '\\langle', '\\rangle', '\\lceil', '\\rceil', 
            '\\lfloor', '\\rfloor', '/', '\\backslash', '\\|',
            '\\uparrow', '\\downarrow', '\\updownarrow', '\\Uparrow', '\\Downarrow', '\\Updownarrow',
            # Bibliography and citation commands
            '\\bibliography', '\\bibliographystyle', '\\bibitem', '\\cite', '\\nocite',
            # Font declaration commands (robust)
            '\\bf', '\\bfseries', '\\cal', '\\em', '\\it', '\\itshape', '\\mdseries', '\\mit', 
            '\\normalfont', '\\rm', '\\rmfamily', '\\sc', '\\scshape', '\\sf', '\\sffamily', 
            '\\sl', '\\slshape', '\\textbf', '\\textit', '\\textmd', '\\textnormal', '\\textrm', 
            '\\textsc', '\\textsf', '\\textsl', '\\texttt', '\\textup', '\\tt', '\\ttfamily', '\\upshape',
            # Font size commands (fragile)
            '\\tiny', '\\scriptsize', '\\footnotesize', '\\small', '\\normalsize', 
            '\\large', '\\Large', '\\LARGE', '\\huge', '\\Huge',
            # Command definition commands
            '\\newcommand', '\\newcommand*', '\\renewcommand', '\\renewcommand*', 
            '\\providecommand', '\\providecommand*', '\\def',
            # Environment definition commands
            '\\newenvironment', '\\renewenvironment'
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
        # Document: 8, Sectioning: 14, Alignment: 3, Greek: 40, Binary: 36, Relation: 36,
        # Arrow: 26 (removed 6 arrows), Misc: 31 (removed 2), Variable-sized: 13, Log-like: 34,
        # Math accent: 12, Math enclosure: 4, Text accent: 14, Text symbol: 24 (removed 2), Text spacing: 5, Delimiter: 32, Bibliography: 5, Font: 40, Command definition: 7, Environment definition: 2
        expected_total = 8 + 14 + 3 + 40 + 36 + 36 + 26 + 31 + 13 + 34 + 12 + 4 + 14 + 24 + 5 + 32 + 5 + 40 + 7 + 2
        actual_total = len(registry.list_keys())
        
        assert actual_total == expected_total, f"Expected {expected_total} total commands, got {actual_total}"


class TestRegisterDelimiterCommands:
    """Test register_delimiter_commands function."""

    def test_registers_expected_delimiter_commands(self):
        """Test that all expected delimiter commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_delimiter_commands(registry)
        
        expected_commands = {
            # Basic delimiters (work in all modes)
            '(', ')', '[', ']', '|', '\\{', '\\}',
            # Sizing commands (math mode only)
            '\\bigl', '\\bigr', '\\Bigl', '\\Bigr', '\\biggl', '\\biggr', 
            '\\Biggl', '\\Biggr', '\\left', '\\right',
            # Named delimiters (math mode only)
            '\\langle', '\\rangle', '\\lceil', '\\rceil', '\\lfloor', '\\rfloor',
            # Slash and backslash delimiters
            '/', '\\backslash',
            # Double vertical bar
            '\\|',
            # Arrow delimiters (math mode only)
            '\\uparrow', '\\downarrow', '\\updownarrow', '\\Uparrow', '\\Downarrow', '\\Updownarrow'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"

    def test_delimiter_command_modes(self):
        """Test that delimiter commands have appropriate mode assignments."""
        registry = CommandDefinitionRegistry()
        register_delimiter_commands(registry)
        
        # Universal delimiters should work in all modes
        universal_delimiters = ['(', ')', '[', ']', '|', '\\{', '\\}']
        for cmd in universal_delimiters:
            entry = registry.get_entry(cmd)
            data = entry.as_dict()
            expected_modes = ['math', 'paragraph', 'left_right']
            assert data['modes'] == expected_modes, f"Command {cmd} should work in all modes but has modes {data['modes']}"
        
        # Math-only sizing commands
        math_only_sizing = ['\\bigl', '\\bigr', '\\Bigl', '\\Bigr', '\\biggl', '\\biggr', 
                           '\\Biggl', '\\Biggr', '\\left', '\\right']
        for cmd in math_only_sizing:
            entry = registry.get_entry(cmd)
            data = entry.as_dict()
            expected_modes = ['math']
            assert data['modes'] == expected_modes, f"Command {cmd} should be math-only but has modes {data['modes']}"
        
        # Math-only named delimiters and symbols
        math_only_named = ['\\langle', '\\rangle', '\\lceil', '\\rceil', '\\lfloor', '\\rfloor',
                          '/', '\\backslash', '\\|',
                          '\\uparrow', '\\downarrow', '\\updownarrow', '\\Uparrow', '\\Downarrow', '\\Updownarrow']
        for cmd in math_only_named:
            entry = registry.get_entry(cmd)
            data = entry.as_dict()
            expected_modes = ['math']
            assert data['modes'] == expected_modes, f"Command {cmd} should be math-only but has modes {data['modes']}"

    def test_delimiter_special_syntax(self):
        """Test that delimiter commands have special syntax notation."""
        registry = CommandDefinitionRegistry()
        register_delimiter_commands(registry)
        
        # Test left/right sizing commands have special syntax
        left_right_commands = ['\\left', '\\right']
        for cmd in left_right_commands:
            entry = registry.get_entry(cmd)
            data = entry.as_dict()
            assert '⟨delimiter⟩' in data['syntax'], f"Command {cmd} should have special delimiter syntax"
        
        # Test sizing commands have sizing syntax
        sizing_commands = ['\\bigl', '\\bigr', '\\Bigl', '\\Bigr']
        for cmd in sizing_commands:
            entry = registry.get_entry(cmd)
            data = entry.as_dict()
            assert '⟨delimiter⟩' in data['syntax'], f"Command {cmd} should have delimiter syntax"


class TestRegisterBibliographyCitationCommands:
    """Test register_bibliography_citation_commands function."""

    def test_registers_expected_bibliography_citation_commands(self):
        """Test that all expected bibliography and citation commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_bibliography_citation_commands(registry)
        
        expected_commands = {
            '\\bibliography', '\\bibliographystyle', '\\bibitem', '\\cite', '\\nocite'
        }
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"

    def test_bibliography_citation_command_robustness(self):
        """Test that bibliography and citation commands have appropriate robustness assignments."""
        registry = CommandDefinitionRegistry()
        register_bibliography_citation_commands(registry)
        
        # Robust commands
        robust_commands = ['\\bibliography', '\\bibliographystyle', '\\bibitem']
        for cmd in robust_commands:
            entry = registry.get_entry(cmd)
            data = entry.as_dict()
            assert data['robustness'] == 'robust', f"Command {cmd} should be robust but is {data['robustness']}"
        
        # Fragile commands
        fragile_commands = ['\\cite', '\\nocite']
        for cmd in fragile_commands:
            entry = registry.get_entry(cmd)
            data = entry.as_dict()
            assert data['robustness'] == 'fragile', f"Command {cmd} should be fragile but is {data['robustness']}"

    def test_bibliography_citation_command_types(self):
        """Test that all bibliography and citation commands have the correct command type."""
        registry = CommandDefinitionRegistry()
        register_bibliography_citation_commands(registry)
        
        all_commands = ['\\bibliography', '\\bibliographystyle', '\\bibitem', '\\cite', '\\nocite']
        for cmd in all_commands:
            entry = registry.get_entry(cmd)
            data = entry.as_dict()
            assert data['command_type'] == 'bibliography', f"Command {cmd} should have bibliography type but has {data['command_type']}"


class TestRegisterCommandDefinitionCommands:
    """Test register_command_definition_commands function."""

    def test_registers_expected_command_definition_commands(self):
        """Test that all expected command definition commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_command_definition_commands(registry)

        expected_commands = {
            '\\newcommand', '\\newcommand*', '\\renewcommand',
            '\\renewcommand*', '\\providecommand', '\\providecommand*',
            '\\def'
        }

        registered_keys = set(registry.list_keys())

        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"
    
    def test_command_definition_commands_have_correct_type(self):
        """Test that command definition commands have correct command type."""
        registry = CommandDefinitionRegistry()
        register_command_definition_commands(registry)

        # Check that all command definition commands have correct command_type
        latex_commands = ['\\newcommand', '\\newcommand*', '\\renewcommand', 
                         '\\renewcommand*', '\\providecommand', '\\providecommand*']
        
        for command_name in latex_commands:
            entry = registry.get_entry(command_name)
            data = entry.as_dict()
            assert data['command_type'] == 'command_definition', f"Command {command_name} should have command_definition type but has {data['command_type']}"
        
        # Check that TeX primitive has correct type
        def_entry = registry.get_entry('\\def')
        def_data = def_entry.as_dict()
        assert def_data['command_type'] == 'tex_command_definition', f"Command \\def should have tex_command_definition type but has {def_data['command_type']}"

    def test_command_definition_commands_have_correct_properties(self):
        """Test that command definition commands have correct robustness and modes."""
        registry = CommandDefinitionRegistry()
        register_command_definition_commands(registry)

        all_commands = ['\\newcommand', '\\newcommand*', '\\renewcommand', 
                       '\\renewcommand*', '\\providecommand', '\\providecommand*']
        
        for command_name in all_commands:
            entry = registry.get_entry(command_name)
            data = entry.as_dict()
            # Check robustness
            assert data['robustness'] == 'fragile', f"Command {command_name} should be fragile but has {data['robustness']}"
            # Check modes
            expected_modes = {'preamble', 'paragraph'}
            actual_modes = set(data['modes'])
            assert actual_modes == expected_modes, f"Command {command_name} should have modes {expected_modes} but has {actual_modes}"

    def test_command_definition_commands_syntax_format(self):
        """Test that command definition commands have correct syntax format."""
        registry = CommandDefinitionRegistry()
        register_command_definition_commands(registry)

        # Expected syntax patterns
        expected_syntax = {
            '\\newcommand': '\\newcommand{cmd}[nargs][default]{definition}',
            '\\newcommand*': '\\newcommand*{cmd}[nargs][default]{definition}',
            '\\renewcommand': '\\renewcommand{cmd}[nargs][default]{definition}',
            '\\renewcommand*': '\\renewcommand*{cmd}[nargs][default]{definition}',
            '\\providecommand': '\\providecommand{cmd}[nargs][default]{definition}',
            '\\providecommand*': '\\providecommand*{cmd}[nargs][default]{definition}',
            '\\def': '\\def⟨pattern⟩{⟨replacement⟩}'
        }
        
        for command_name, expected in expected_syntax.items():
            entry = registry.get_entry(command_name)
            data = entry.as_dict()
            assert data['syntax'] == expected, f"Command {command_name} should have syntax '{expected}' but has '{data['syntax']}'"

    def test_command_definition_commands_have_descriptions(self):
        """Test that command definition commands have non-empty descriptions."""
        registry = CommandDefinitionRegistry()
        register_command_definition_commands(registry)

        all_commands = ['\\newcommand', '\\newcommand*', '\\renewcommand', 
                       '\\renewcommand*', '\\providecommand', '\\providecommand*']
        
        for command_name in all_commands:
            entry = registry.get_entry(command_name)
            data = entry.as_dict()
            assert data['description'], f"Command {command_name} should have a non-empty description"
            assert len(data['description']) > 0, f"Command {command_name} description should not be empty"

    def test_command_definition_commands_have_references(self):
        """Test that command definition commands have references."""
        registry = CommandDefinitionRegistry()
        register_command_definition_commands(registry)

        all_commands = ['\\newcommand', '\\newcommand*', '\\renewcommand', 
                       '\\renewcommand*', '\\providecommand', '\\providecommand*']
        
        for command_name in all_commands:
            entry = registry.get_entry(command_name)
            data = entry.as_dict()
            assert isinstance(data['references'], list), f"Command {command_name} should have references as a list"
            assert len(data['references']) > 0, f"Command {command_name} should have at least one reference"
            # Check that each reference has expected fields
            for ref in data['references']:
                assert 'ref_id' in ref, f"Reference for {command_name} should have 'ref_id' field"
                assert 'sections' in ref, f"Reference for {command_name} should have 'sections' field"
                assert 'pages' in ref, f"Reference for {command_name} should have 'pages' field"


class TestRegisterEnvironmentDefinitionCommands:
    """Test register_environment_definition_commands function."""

    def test_registers_expected_environment_definition_commands(self):
        """Test that all expected environment definition commands are registered and only those."""
        registry = CommandDefinitionRegistry()
        register_environment_definition_commands(registry)

        expected_commands = {
            '\\newenvironment', '\\renewenvironment'
        }

        registered_keys = set(registry.list_keys())

        # Check that exactly the expected commands are present
        assert registered_keys == expected_commands, f"Expected {expected_commands}, got {registered_keys}"
    
    def test_environment_definition_commands_have_correct_type(self):
        """Test that environment definition commands have correct command type."""
        registry = CommandDefinitionRegistry()
        register_environment_definition_commands(registry)

        # Check that all environment definition commands have correct command_type
        env_commands = ['\\newenvironment', '\\renewenvironment']
        
        for command_name in env_commands:
            entry = registry.get_entry(command_name)
            data = entry.as_dict()
            assert data['command_type'] == 'environment_definition', f"Command {command_name} should have environment_definition type but has {data['command_type']}"

    def test_environment_definition_commands_have_correct_properties(self):
        """Test that environment definition commands have correct robustness and modes."""
        registry = CommandDefinitionRegistry()
        register_environment_definition_commands(registry)

        all_commands = ['\\newenvironment', '\\renewenvironment']
        
        for command_name in all_commands:
            entry = registry.get_entry(command_name)
            data = entry.as_dict()
            # Check robustness
            assert data['robustness'] == 'fragile', f"Command {command_name} should be fragile but has {data['robustness']}"
            # Check modes
            expected_modes = {'preamble', 'paragraph'}
            actual_modes = set(data['modes'])
            assert actual_modes == expected_modes, f"Command {command_name} should have modes {expected_modes} but has {actual_modes}"

    def test_environment_definition_commands_syntax_format(self):
        """Test that environment definition commands have correct syntax format."""
        registry = CommandDefinitionRegistry()
        register_environment_definition_commands(registry)

        # Expected syntax patterns
        expected_syntax = {
            '\\newenvironment': '\\newenvironment{name}[nargs][default]{begin_definition}{end_definition}',
            '\\renewenvironment': '\\renewenvironment{name}[nargs][default]{begin_definition}{end_definition}'
        }
        
        for command_name, expected in expected_syntax.items():
            entry = registry.get_entry(command_name)
            data = entry.as_dict()
            assert data['syntax'] == expected, f"Command {command_name} should have syntax '{expected}' but has '{data['syntax']}'"

    def test_environment_definition_commands_have_descriptions(self):
        """Test that environment definition commands have non-empty descriptions."""
        registry = CommandDefinitionRegistry()
        register_environment_definition_commands(registry)

        all_commands = ['\\newenvironment', '\\renewenvironment']
        
        for command_name in all_commands:
            entry = registry.get_entry(command_name)
            data = entry.as_dict()
            assert data['description'], f"Command {command_name} should have a non-empty description"
            assert len(data['description']) > 0, f"Command {command_name} description should not be empty"

    def test_environment_definition_commands_have_references(self):
        """Test that environment definition commands have references."""
        registry = CommandDefinitionRegistry()
        register_environment_definition_commands(registry)

        all_commands = ['\\newenvironment', '\\renewenvironment']
        
        for command_name in all_commands:
            entry = registry.get_entry(command_name)
            data = entry.as_dict()
            assert isinstance(data['references'], list), f"Command {command_name} should have references as a list"
            assert len(data['references']) > 0, f"Command {command_name} should have at least one reference"
            # Check that each reference has expected fields
            for ref in data['references']:
                assert 'ref_id' in ref, f"Reference for {command_name} should have 'ref_id' field"
                assert 'sections' in ref, f"Reference for {command_name} should have 'sections' field"
                assert 'pages' in ref, f"Reference for {command_name} should have 'pages' field"

    def test_environment_definition_commands_reference_content(self):
        """Test that environment definition commands reference LaTeX Companion A.1.3."""
        registry = CommandDefinitionRegistry()
        register_environment_definition_commands(registry)

        all_commands = ['\\newenvironment', '\\renewenvironment']
        
        for command_name in all_commands:
            entry = registry.get_entry(command_name)
            data = entry.as_dict()
            references = data['references']
            assert len(references) == 1, f"Command {command_name} should have exactly one reference"
            
            ref = references[0]
            assert ref['ref_id'] == 'latex_companion_2004', f"Command {command_name} should reference LaTeX Companion 2004"
            assert ref['sections'] == 'A.1.3', f"Command {command_name} should reference section A.1.3"
            assert ref['pages'] == '847-850', f"Command {command_name} should reference pages 847-850"

    def test_environment_definition_commands_descriptions_content(self):
        """Test that environment definition commands have appropriate descriptions."""
        registry = CommandDefinitionRegistry()
        register_environment_definition_commands(registry)

        # Check specific descriptions
        new_entry = registry.get_entry('\\newenvironment')
        new_data = new_entry.as_dict()
        assert 'defines a new environment' in new_data['description']
        assert 'errors if the environment already exists' in new_data['description']

        renew_entry = registry.get_entry('\\renewenvironment')
        renew_data = renew_entry.as_dict()
        assert 'redefines an existing environment' in renew_data['description']
        assert 'errors if the environment does not exist' in renew_data['description']