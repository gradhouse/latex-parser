# File: register_command_definitions.py
# Description: Register LaTeX command definitions
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

from typing import List
from latex_parser.latex.definitions.command_definition import CommandDefinition, CommandType, CommandRobustness, CommandMode
from latex_parser.latex.definitions.command_definition_registry import CommandDefinitionRegistry

def register_document_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register LaTeX document commands in the command definition registry.

    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for document commands
    references = [{'ref_id': 'lamport_1994', 'sections': '2.2.2, C.5.1, C.5.2, C.5.4', 'pages': '19-21, 176-179, 181-183'}]
    
    def add_doc_cmd(name: str, syntax: str, description: str) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.DOCUMENT,
            robustness=CommandRobustness.ROBUST, modes=[CommandMode.PREAMBLE],
            description=description, references=references
        ))
    
    # Register document commands
    add_doc_cmd('\\documentclass', '\\documentclass[options]{class}', 
                'Specifies the overall layout of the document by selecting a document class and optional parameters')
    add_doc_cmd('\\documentstyle', '\\documentstyle[options]{style}',
                'Specifies the overall layout of the document by selecting a document style and optional parameters. This command is for LaTeX 2.09 and deprecated in favor of \\documentclass.')
    add_doc_cmd('\\usepackage', '\\usepackage[options]{packages}',
                'Loads a LaTeX package with optional parameters')
    add_doc_cmd('\\maketitle', '\\maketitle',
                'Generates the title block using information from \\title, \\author, \\date, and \\thanks')
    add_doc_cmd('\\title', '\\title{title}',
                'Defines the document title to be typeset by \\maketitle')
    add_doc_cmd('\\author', '\\author{authors}',
                'Defines the document author(s) to be typeset by \\maketitle')
    add_doc_cmd('\\date', '\\date{date}',
                'Defines the document date to be typeset by \\maketitle')
    add_doc_cmd('\\thanks', '\\thanks{text}',
                'Provides a footnote for the title, author, or date in the title block')


def register_sectioning_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register LaTeX sectioning commands in the command definition registry.
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for sectioning commands
    references = [{'ref_id': 'lamport_1994', 'sections': '2.2.3, C.4.1', 'pages': '21-22, 174'}]
    
    def add_sect_cmd(name: str, syntax: str, description: str) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.SECTIONING,
            robustness=CommandRobustness.ROBUST, modes=[CommandMode.PARAGRAPH],
            description=description, references=references
        ))
    
    # Register sectioning commands
    add_sect_cmd('\\part', '\\part[toc_entry]{heading}',
                 'Starts a major sectional division at the part level; typically used in book classes; optionally adds an entry to the table of contents')
    add_sect_cmd('\\part*', '\\part*{heading}',
                 'Starts a major sectional division at the part level without adding an entry to the table of contents')
    add_sect_cmd('\\chapter', '\\chapter[toc_entry]{heading}',
                 'Starts a major sectional division at the chapter level; typically used in book and report classes; optionally adds an entry to the table of contents')
    add_sect_cmd('\\chapter*', '\\chapter*{heading}',
                 'Starts a major sectional division at the chapter level without adding an entry to the table of contents')
    add_sect_cmd('\\section', '\\section[toc_entry]{heading}',
                 'Starts a major sectional division at the section level; typically used in articles, books, and reports; optionally adds an entry to the table of contents')
    add_sect_cmd('\\section*', '\\section*{heading}',
                 'Starts a major sectional division at the section level without adding an entry to the table of contents')
    add_sect_cmd('\\subsection', '\\subsection[toc_entry]{heading}',
                 'Starts a sectional division at the subsection level; optionally adds an entry to the table of contents')
    add_sect_cmd('\\subsection*', '\\subsection*{heading}',
                 'Starts a sectional division at the subsection level without adding an entry to the table of contents')
    add_sect_cmd('\\subsubsection', '\\subsubsection[toc_entry]{heading}',
                 'Starts a sectional division at the subsubsection level; optionally adds an entry to the table of contents')
    add_sect_cmd('\\subsubsection*', '\\subsubsection*{heading}',
                 'Starts a sectional division at the subsubsection level without adding an entry to the table of contents')
    add_sect_cmd('\\paragraph', '\\paragraph[toc_entry]{heading}',
                 'Starts a sectional division at the paragraph level; optionally adds an entry to the table of contents')
    add_sect_cmd('\\paragraph*', '\\paragraph*{heading}',
                 'Starts a sectional division at the paragraph level without adding an entry to the table of contents')
    add_sect_cmd('\\subparagraph', '\\subparagraph[toc_entry]{heading}',
                 'Starts a sectional division at the subparagraph level; optionally adds an entry to the table of contents')
    add_sect_cmd('\\subparagraph*', '\\subparagraph*{heading}',
                 'Starts a sectional division at the subparagraph level without adding an entry to the table of contents')


def register_greek_letter_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register Greek letter math symbol commands in the command definition registry.
    
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for Greek letter commands
    references = [{'ref_id': 'lamport_1994', 'sections': '3.3.2, C.7.3', 'pages': '41-45, 189-190'}]
    
    def add_greek_cmd(name: str, syntax: str, description: str) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.MATH_SYMBOL_GREEK_LETTER,
            robustness=CommandRobustness.ROBUST, modes=[CommandMode.MATH],
            description=description, references=references
        ))
    
    # Register Greek letter commands
    add_greek_cmd('\\alpha', '\\alpha', 'Greek letter alpha')
    add_greek_cmd('\\beta', '\\beta', 'Greek letter beta')
    add_greek_cmd('\\gamma', '\\gamma', 'Greek letter gamma')
    add_greek_cmd('\\delta', '\\delta', 'Greek letter delta')
    add_greek_cmd('\\epsilon', '\\epsilon', 'Greek letter epsilon')
    add_greek_cmd('\\varepsilon', '\\varepsilon', 'variant Greek letter epsilon')
    add_greek_cmd('\\zeta', '\\zeta', 'Greek letter zeta')
    add_greek_cmd('\\eta', '\\eta', 'Greek letter eta')
    add_greek_cmd('\\theta', '\\theta', 'Greek letter theta')
    add_greek_cmd('\\vartheta', '\\vartheta', 'variant Greek letter theta')
    add_greek_cmd('\\iota', '\\iota', 'Greek letter iota')
    add_greek_cmd('\\kappa', '\\kappa', 'Greek letter kappa')
    add_greek_cmd('\\lambda', '\\lambda', 'Greek letter lambda')
    add_greek_cmd('\\mu', '\\mu', 'Greek letter mu')
    add_greek_cmd('\\nu', '\\nu', 'Greek letter nu')
    add_greek_cmd('\\xi', '\\xi', 'Greek letter xi')
    add_greek_cmd('\\pi', '\\pi', 'Greek letter pi')
    add_greek_cmd('\\varpi', '\\varpi', 'variant Greek letter pi')
    add_greek_cmd('\\rho', '\\rho', 'Greek letter rho')
    add_greek_cmd('\\varrho', '\\varrho', 'variant Greek letter rho')
    add_greek_cmd('\\sigma', '\\sigma', 'Greek letter sigma')
    add_greek_cmd('\\varsigma', '\\varsigma', 'variant Greek letter sigma')
    add_greek_cmd('\\tau', '\\tau', 'Greek letter tau')
    add_greek_cmd('\\upsilon', '\\upsilon', 'Greek letter upsilon')
    add_greek_cmd('\\phi', '\\phi', 'Greek letter phi')
    add_greek_cmd('\\varphi', '\\varphi', 'variant Greek letter phi')
    add_greek_cmd('\\chi', '\\chi', 'Greek letter chi')
    add_greek_cmd('\\psi', '\\psi', 'Greek letter psi')
    add_greek_cmd('\\omega', '\\omega', 'Greek letter omega')
    add_greek_cmd('\\Gamma', '\\Gamma', 'uppercase Greek letter Gamma')
    add_greek_cmd('\\Delta', '\\Delta', 'uppercase Greek letter Delta')
    add_greek_cmd('\\Theta', '\\Theta', 'uppercase Greek letter Theta')
    add_greek_cmd('\\Lambda', '\\Lambda', 'uppercase Greek letter Lambda')
    add_greek_cmd('\\Xi', '\\Xi', 'uppercase Greek letter Xi')
    add_greek_cmd('\\Pi', '\\Pi', 'uppercase Greek letter Pi')
    add_greek_cmd('\\Sigma', '\\Sigma', 'uppercase Greek letter Sigma')
    add_greek_cmd('\\Upsilon', '\\Upsilon', 'uppercase Greek letter Upsilon')
    add_greek_cmd('\\Phi', '\\Phi', 'uppercase Greek letter Phi')
    add_greek_cmd('\\Psi', '\\Psi', 'uppercase Greek letter Psi')
    add_greek_cmd('\\Omega', '\\Omega', 'uppercase Greek letter Omega')


def register_binary_operation_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register binary operation math symbol commands in the command definition registry.
    
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for binary operation commands
    references = [{'ref_id': 'lamport_1994', 'sections': '3.3.2, C.7.3', 'pages': '41-45, 189-190'}]
    
    def add_binop_cmd(name: str, syntax: str, description: str) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.MATH_SYMBOL_BINARY_OP,
            robustness=CommandRobustness.ROBUST, modes=[CommandMode.MATH],
            description=description, references=references
        ))
    
    # Register binary operation commands
    add_binop_cmd('\\pm', '\\pm', 'plus-minus sign')
    add_binop_cmd('\\mp', '\\mp', 'minus-plus sign')
    add_binop_cmd('\\times', '\\times', 'multiplication sign')
    add_binop_cmd('\\div', '\\div', 'division sign')
    add_binop_cmd('\\ast', '\\ast', 'asterisk operator')
    add_binop_cmd('\\star', '\\star', 'star operator')
    add_binop_cmd('\\circ', '\\circ', 'circle operator')
    add_binop_cmd('\\bullet', '\\bullet', 'bullet operator')
    add_binop_cmd('\\cdot', '\\cdot', 'centered dot operator')
    add_binop_cmd('\\cap', '\\cap', 'intersection operator')
    add_binop_cmd('\\cup', '\\cup', 'union operator')
    add_binop_cmd('\\uplus', '\\uplus', 'disjoint union operator')
    add_binop_cmd('\\sqcap', '\\sqcap', 'square intersection operator')
    add_binop_cmd('\\sqcup', '\\sqcup', 'square union operator')
    add_binop_cmd('\\vee', '\\vee', 'logical or operator')
    add_binop_cmd('\\wedge', '\\wedge', 'logical and operator')
    add_binop_cmd('\\setminus', '\\setminus', 'set difference operator')
    add_binop_cmd('\\wr', '\\wr', 'wreath product operator')
    add_binop_cmd('\\diamond', '\\diamond', 'diamond operator')
    add_binop_cmd('\\bigtriangleup', '\\bigtriangleup', 'big triangle up operator')
    add_binop_cmd('\\bigtriangledown', '\\bigtriangledown', 'big triangle down operator')
    add_binop_cmd('\\triangleleft', '\\triangleleft', 'triangle left operator')
    add_binop_cmd('\\triangleright', '\\triangleright', 'triangle right operator')
    add_binop_cmd('\\lhd', '\\lhd', 'left harpoon down operator')
    add_binop_cmd('\\rhd', '\\rhd', 'right harpoon down operator')
    add_binop_cmd('\\unlhd', '\\unlhd', 'underlined left harpoon down operator')
    add_binop_cmd('\\unrhd', '\\unrhd', 'underlined right harpoon down operator')
    add_binop_cmd('\\oplus', '\\oplus', 'circled plus operator')
    add_binop_cmd('\\ominus', '\\ominus', 'circled minus operator')
    add_binop_cmd('\\otimes', '\\otimes', 'circled times operator')
    add_binop_cmd('\\oslash', '\\oslash', 'circled slash operator')
    add_binop_cmd('\\odot', '\\odot', 'circled dot operator')
    add_binop_cmd('\\bigcirc', '\\bigcirc', 'big circle operator')
    add_binop_cmd('\\dagger', '\\dagger', 'dagger operator')
    add_binop_cmd('\\ddagger', '\\ddagger', 'double dagger operator')
    add_binop_cmd('\\amalg', '\\amalg', 'amalgamation operator')


def register_relation_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register relation math symbol commands in the command definition registry.
    
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for relation commands
    references = [{'ref_id': 'lamport_1994', 'sections': '3.3.2, C.7.3', 'pages': '41-45, 189-190'}]
    
    def add_rel_cmd(name: str, syntax: str, description: str) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.MATH_SYMBOL_RELATION,
            robustness=CommandRobustness.ROBUST, modes=[CommandMode.MATH],
            description=description, references=references
        ))
    
    # Register relation commands
    add_rel_cmd('\\leq', '\\leq', 'less than or equal to sign')
    add_rel_cmd('\\prec', '\\prec', 'precedes')
    add_rel_cmd('\\preceq', '\\preceq', 'precedes or equals')
    add_rel_cmd('\\ll', '\\ll', 'much less than')
    add_rel_cmd('\\subset', '\\subset', 'subset of')
    add_rel_cmd('\\subseteq', '\\subseteq', 'subset of or equal to')
    add_rel_cmd('\\sqsubset', '\\sqsubset', 'square subset of')
    add_rel_cmd('\\sqsubseteq', '\\sqsubseteq', 'square subset of or equal to')
    add_rel_cmd('\\in', '\\in', 'element of')
    add_rel_cmd('\\vdash', '\\vdash', 'entails (turnstile)')
    add_rel_cmd('\\geq', '\\geq', 'greater than or equal to')
    add_rel_cmd('\\succ', '\\succ', 'succeeds')
    add_rel_cmd('\\succeq', '\\succeq', 'succeeds or equals')
    add_rel_cmd('\\gg', '\\gg', 'much greater than')
    add_rel_cmd('\\sqsupset', '\\sqsupset', 'square superset of')
    add_rel_cmd('\\sqsupseteq', '\\sqsupseteq', 'square superset of or equal to')
    add_rel_cmd('\\ni', '\\ni', 'contains as member')
    add_rel_cmd('\\dashv', '\\dashv', 'dash with vertical bar')
    add_rel_cmd('\\equiv', '\\equiv', 'identically equal to')
    add_rel_cmd('\\sim', '\\sim', 'similar to')
    add_rel_cmd('\\simeq', '\\simeq', 'asymptotically equal to')
    add_rel_cmd('\\asymp', '\\asymp', 'asymptotically equal to')
    add_rel_cmd('\\approx', '\\approx', 'approximately equal to')
    add_rel_cmd('\\cong', '\\cong', 'congruent to')
    add_rel_cmd('\\neq', '\\neq', 'not equal to')
    add_rel_cmd('\\doteq', '\\doteq', 'approaches the value')
    add_rel_cmd('\\notin', '\\notin', 'not an element of')
    add_rel_cmd('\\models', '\\models', 'models (double turnstile)')
    add_rel_cmd('\\perp', '\\perp', 'perpendicular to')
    add_rel_cmd('\\mid', '\\mid', 'such that (vertical bar)')
    add_rel_cmd('\\parallel', '\\parallel', 'parallel to')
    add_rel_cmd('\\bowtie', '\\bowtie', 'bowtie relation')
    add_rel_cmd('\\Join', '\\Join', 'join relation')
    add_rel_cmd('\\smile', '\\smile', 'smile relation')
    add_rel_cmd('\\frown', '\\frown', 'frown relation')
    add_rel_cmd('\\propto', '\\propto', 'proportional to')


def register_arrow_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register arrow math symbol commands in the command definition registry.
    
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for arrow commands
    references = [{'ref_id': 'lamport_1994', 'sections': '3.3.2, C.7.3', 'pages': '41-45, 189-190'}]
    
    def add_arrow_cmd(name: str, syntax: str, description: str) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.MATH_SYMBOL_ARROW,
            robustness=CommandRobustness.ROBUST, modes=[CommandMode.MATH],
            description=description, references=references
        ))
    
    # Register arrow commands
    add_arrow_cmd('\\leftarrow', '\\leftarrow', 'left arrow')
    add_arrow_cmd('\\Leftarrow', '\\Leftarrow', 'double left arrow')
    add_arrow_cmd('\\rightarrow', '\\rightarrow', 'right arrow')
    add_arrow_cmd('\\Rightarrow', '\\Rightarrow', 'double right arrow')
    add_arrow_cmd('\\leftrightarrow', '\\leftrightarrow', 'left-right arrow')
    add_arrow_cmd('\\Leftrightarrow', '\\Leftrightarrow', 'double left-right arrow')
    add_arrow_cmd('\\mapsto', '\\mapsto', 'mapsto arrow')
    add_arrow_cmd('\\hookleftarrow', '\\hookleftarrow', 'hook left arrow')
    add_arrow_cmd('\\leftharpoonup', '\\leftharpoonup', 'left harpoon up')
    add_arrow_cmd('\\leftharpoondown', '\\leftharpoondown', 'left harpoon down')
    add_arrow_cmd('\\rightleftharpoons', '\\rightleftharpoons', 'right and left harpoons')
    add_arrow_cmd('\\longleftarrow', '\\longleftarrow', 'long left arrow')
    add_arrow_cmd('\\Longleftarrow', '\\Longleftarrow', 'long double left arrow')
    add_arrow_cmd('\\longrightarrow', '\\longrightarrow', 'long right arrow')
    add_arrow_cmd('\\Longrightarrow', '\\Longrightarrow', 'long double right arrow')
    add_arrow_cmd('\\longleftrightarrow', '\\longleftrightarrow', 'long left-right arrow')
    add_arrow_cmd('\\Longleftrightarrow', '\\Longleftrightarrow', 'long double left-right arrow')
    add_arrow_cmd('\\longmapsto', '\\longmapsto', 'long mapsto arrow')
    add_arrow_cmd('\\hookrightarrow', '\\hookrightarrow', 'hook right arrow')
    add_arrow_cmd('\\rightharpoonup', '\\rightharpoonup', 'right harpoon up')
    add_arrow_cmd('\\rightharpoondown', '\\rightharpoondown', 'right harpoon down')
    add_arrow_cmd('\\leadsto', '\\leadsto', 'leads to arrow')
    add_arrow_cmd('\\nearrow', '\\nearrow', 'north-east arrow')
    add_arrow_cmd('\\searrow', '\\searrow', 'south-east arrow')
    add_arrow_cmd('\\swarrow', '\\swarrow', 'south-west arrow')
    add_arrow_cmd('\\nwarrow', '\\nwarrow', 'north-west arrow')


def register_misc_symbol_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register miscellaneous math symbol commands in the command definition registry.
    
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for miscellaneous symbol commands
    references = [{'ref_id': 'lamport_1994', 'sections': '3.3.2, C.7.3', 'pages': '41-45, 189-190'}]
    
    def add_misc_cmd(name: str, syntax: str, description: str) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.MATH_SYMBOL_MISC,
            robustness=CommandRobustness.ROBUST, modes=[CommandMode.MATH],
            description=description, references=references
        ))
    
    # Register miscellaneous symbol commands
    add_misc_cmd('\\aleph', '\\aleph', 'aleph symbol')
    add_misc_cmd('\\hbar', '\\hbar', 'h-bar (Planck constant over 2π)')
    add_misc_cmd('\\imath', '\\imath', 'dotless i')
    add_misc_cmd('\\jmath', '\\jmath', 'dotless j')
    add_misc_cmd('\\ell', '\\ell', 'script letter l')
    add_misc_cmd('\\wp', '\\wp', 'Weierstrass p')
    add_misc_cmd('\\Re', '\\Re', 'real part')
    add_misc_cmd('\\Im', '\\Im', 'imaginary part')
    add_misc_cmd('\\mho', '\\mho', 'mho (conductance)')
    add_misc_cmd('\\prime', '\\prime', 'prime symbol')
    add_misc_cmd('\\emptyset', '\\emptyset', 'empty set')
    add_misc_cmd('\\nabla', '\\nabla', 'nabla (del operator)')
    add_misc_cmd('\\surd', '\\surd', 'square root sign')
    add_misc_cmd('\\top', '\\top', 'top (truth)')
    add_misc_cmd('\\bot', '\\bot', 'bottom (falsity)')
    add_misc_cmd('\\angle', '\\angle', 'angle symbol')
    add_misc_cmd('\\forall', '\\forall', 'for all')
    add_misc_cmd('\\exists', '\\exists', 'there exists')
    add_misc_cmd('\\neg', '\\neg', 'negation')
    add_misc_cmd('\\flat', '\\flat', 'flat (music)')
    add_misc_cmd('\\natural', '\\natural', 'natural (music)')
    add_misc_cmd('\\sharp', '\\sharp', 'sharp (music)')
    add_misc_cmd('\\partial', '\\partial', 'partial derivative symbol')
    add_misc_cmd('\\infty', '\\infty', 'infinity symbol')
    add_misc_cmd('\\Box', '\\Box', 'box symbol')
    add_misc_cmd('\\Diamond', '\\Diamond', 'diamond symbol')
    add_misc_cmd('\\triangle', '\\triangle', 'triangle symbol')
    add_misc_cmd('\\clubsuit', '\\clubsuit', 'club suit')
    add_misc_cmd('\\diamondsuit', '\\diamondsuit', 'diamond suit')
    add_misc_cmd('\\heartsuit', '\\heartsuit', 'heart suit')
    add_misc_cmd('\\spadesuit', '\\spadesuit', 'spade suit')


def register_variable_sized_symbol_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register variable-sized math symbol commands in the command definition registry.
    
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for variable-sized symbol commands
    references = [{'ref_id': 'lamport_1994', 'sections': '3.3.2, C.7.3', 'pages': '41-45, 189-190'}]
    
    def add_varsized_cmd(name: str, syntax: str, description: str) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.MATH_SYMBOL_VARIABLE_SIZED,
            robustness=CommandRobustness.ROBUST, modes=[CommandMode.MATH],
            description=description, references=references
        ))
    
    # Register variable-sized symbol commands
    add_varsized_cmd('\\sum', '\\sum', 'summation symbol')
    add_varsized_cmd('\\prod', '\\prod', 'product symbol')
    add_varsized_cmd('\\coprod', '\\coprod', 'coproduct symbol')
    add_varsized_cmd('\\int', '\\int', 'integral symbol')
    add_varsized_cmd('\\oint', '\\oint', 'contour integral symbol')
    add_varsized_cmd('\\bigcap', '\\bigcap', 'big intersection symbol')
    add_varsized_cmd('\\bigcup', '\\bigcup', 'big union symbol')
    add_varsized_cmd('\\bigvee', '\\bigvee', 'big logical or symbol')
    add_varsized_cmd('\\bigwedge', '\\bigwedge', 'big logical and symbol')
    add_varsized_cmd('\\bigodot', '\\bigodot', 'big circled dot symbol')
    add_varsized_cmd('\\bigotimes', '\\bigotimes', 'big circled times symbol')
    add_varsized_cmd('\\bigoplus', '\\bigoplus', 'big circled plus symbol')
    add_varsized_cmd('\\biguplus', '\\biguplus', 'big disjoint union symbol')


def register_log_like_function_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register log-like math function commands in the command definition registry.
    
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for log-like function commands
    references = [{'ref_id': 'lamport_1994', 'sections': '3.3.2, C.7.3', 'pages': '41-45, 189-190'}]
    
    def add_loglike_cmd(name: str, syntax: str, description: str) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.MATH_FUNCTION_LOG_LIKE,
            robustness=CommandRobustness.ROBUST, modes=[CommandMode.MATH],
            description=description, references=references
        ))
    
    # Register log-like function commands
    add_loglike_cmd('\\arccos', '\\arccos', 'inverse cosine function')
    add_loglike_cmd('\\arcsin', '\\arcsin', 'inverse sine function')
    add_loglike_cmd('\\arctan', '\\arctan', 'inverse tangent function')
    add_loglike_cmd('\\arg', '\\arg', 'argument of a complex number')
    add_loglike_cmd('\\cos', '\\cos', 'cosine function')
    add_loglike_cmd('\\cosh', '\\cosh', 'hyperbolic cosine function')
    add_loglike_cmd('\\cot', '\\cot', 'cotangent function')
    add_loglike_cmd('\\coth', '\\coth', 'hyperbolic cotangent function')
    add_loglike_cmd('\\csc', '\\csc', 'cosecant function')
    add_loglike_cmd('\\deg', '\\deg', 'degree of a polynomial or vertex')
    add_loglike_cmd('\\det', '\\det', 'determinant')
    add_loglike_cmd('\\dim', '\\dim', 'dimension')
    add_loglike_cmd('\\exp', '\\exp', 'exponential function')
    add_loglike_cmd('\\gcd', '\\gcd', 'greatest common divisor')
    add_loglike_cmd('\\hom', '\\hom', 'homomorphism set')
    add_loglike_cmd('\\inf', '\\inf', 'infimum')
    add_loglike_cmd('\\ker', '\\ker', 'kernel')
    add_loglike_cmd('\\lg', '\\lg', 'base-10 logarithm')
    add_loglike_cmd('\\lim', '\\lim', 'limit')
    add_loglike_cmd('\\liminf', '\\liminf', 'limit inferior')
    add_loglike_cmd('\\limsup', '\\limsup', 'limit superior')
    add_loglike_cmd('\\ln', '\\ln', 'natural logarithm')
    add_loglike_cmd('\\log', '\\log', 'logarithm')
    add_loglike_cmd('\\max', '\\max', 'maximum')
    add_loglike_cmd('\\min', '\\min', 'minimum')
    add_loglike_cmd('\\Pr', '\\Pr', 'probability')
    add_loglike_cmd('\\sec', '\\sec', 'secant function')
    add_loglike_cmd('\\sin', '\\sin', 'sine function')
    add_loglike_cmd('\\sinh', '\\sinh', 'hyperbolic sine function')
    add_loglike_cmd('\\sup', '\\sup', 'supremum')
    add_loglike_cmd('\\tan', '\\tan', 'tangent function')
    add_loglike_cmd('\\tanh', '\\tanh', 'hyperbolic tangent function')
    add_loglike_cmd('\\bmod', '\\bmod', 'modulus operation')
    add_loglike_cmd('\\pmod', '\\pmod{n}', 'typesets the modulus in congruence relations, displaying (mod n) in math mode')


def register_math_accent_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register math accent commands in the command definition registry.
    
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for math accent commands
    references = [{'ref_id': 'lamport_1994', 'sections': '3.3.6, C.7.6', 'pages': '49-50, 190-191'}]
    
    def add_accent_cmd(name: str, syntax: str, description: str) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.MATH_ACCENT,
            robustness=CommandRobustness.ROBUST, modes=[CommandMode.MATH],
            description=description, references=references
        ))
    
    # Register math accent commands
    add_accent_cmd('\\hat', '\\hat{text}', 'draw hat over text')
    add_accent_cmd('\\check', '\\check{text}', 'draw check accent over text')
    add_accent_cmd('\\breve', '\\breve{text}', 'draw breve accent over text')
    add_accent_cmd('\\acute', '\\acute{text}', 'draw acute accent over text')
    add_accent_cmd('\\grave', '\\grave{text}', 'draw grave accent over text')
    add_accent_cmd('\\tilde', '\\tilde{text}', 'draw tilde over text')
    add_accent_cmd('\\bar', '\\bar{text}', 'draw bar over text')
    add_accent_cmd('\\vec', '\\vec{text}', 'draw vector arrow over text')
    add_accent_cmd('\\dot', '\\dot{text}', 'draw single dot over text')
    add_accent_cmd('\\ddot', '\\ddot{text}', 'draw double dot over text')
    add_accent_cmd('\\widehat', '\\widehat{text}', 'draw wide hat over text')
    add_accent_cmd('\\widetilde', '\\widetilde{text}', 'draw wide tilde over text')


def register_math_enclosure_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register math enclosure commands in the command definition registry.
    
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for math enclosure commands
    references = [{'ref_id': 'lamport_1994', 'sections': '3.3.6, C.7.6', 'pages': '49-50, 190-191'}]
    
    def add_enclosure_cmd(name: str, syntax: str, description: str, robustness: CommandRobustness, modes: List[CommandMode]) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.MATH_ENCLOSURE,
            robustness=robustness, modes=modes,
            description=description, references=references
        ))
    
    # Register math enclosure commands
    add_enclosure_cmd('\\overline', '\\overline{text}', 'draw horizontal line over text', 
                     CommandRobustness.ROBUST, [CommandMode.MATH])
    add_enclosure_cmd('\\underline', '\\underline{text}', 'draw horizontal line under text', 
                     CommandRobustness.FRAGILE, [CommandMode.MATH, CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_enclosure_cmd('\\overbrace', '\\overbrace{text}', 'draw horizontal brace over text', 
                     CommandRobustness.ROBUST, [CommandMode.MATH])
    add_enclosure_cmd('\\underbrace', '\\underbrace{text}', 'draw horizontal brace under text', 
                     CommandRobustness.ROBUST, [CommandMode.MATH])


def register_text_accent_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register text accent commands in the command definition registry.
    
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for text accent commands
    references = [{'ref_id': 'lamport_1994', 'sections': '3.2.1, C.3.4', 'pages': '38, 173'}]
    
    def add_text_accent_cmd(name: str, syntax: str, description: str) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.TEXT_ACCENT,
            robustness=CommandRobustness.ROBUST, modes=[CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT],
            description=description, references=references
        ))
    
    # Register text accent commands
    add_text_accent_cmd("\\'", "\\'{character}", 'acute accent (e.g., é)')
    add_text_accent_cmd('\\`', '\\`{character}', 'grave accent (e.g., è)')
    add_text_accent_cmd('\\^', '\\^{character}', 'circumflex accent (e.g., ê)')
    add_text_accent_cmd('\\"', '\\"{character}', 'diaeresis/umlaut accent (e.g., ë)')
    add_text_accent_cmd('\\~', '\\~{character}', 'tilde accent (e.g., ñ)')
    add_text_accent_cmd('\\=', '\\={character}', 'macron accent (e.g., ō)')
    add_text_accent_cmd('\\.', '\\.{character}', 'dot accent (e.g., ṅ)')
    add_text_accent_cmd('\\u', '\\u{character}', 'breve accent (e.g., ă)')
    add_text_accent_cmd('\\v', '\\v{character}', 'caron/háček accent (e.g., č)')
    add_text_accent_cmd('\\H', '\\H{character}', 'double acute accent (e.g., ő)')
    add_text_accent_cmd('\\t', '\\t{characters}', 'tie accent (connects two characters)')
    add_text_accent_cmd('\\c', '\\c{character}', 'cedilla accent (e.g., ç)')
    add_text_accent_cmd('\\d', '\\d{character}', 'dot-under accent (e.g., ḍ)')
    add_text_accent_cmd('\\b', '\\b{character}', 'bar-under accent (e.g., ṯ)')


def register_text_symbol_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register text symbol commands in the command definition registry.
    
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for text symbol commands
    references = [{'ref_id': 'lamport_1994', 'sections': '3.2.2, C.3.4', 'pages': '38-39, 173'}]
    
    def add_text_symbol_cmd(name: str, syntax: str, description: str, modes: List[CommandMode]) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.TEXT_SYMBOL,
            robustness=CommandRobustness.ROBUST, modes=modes,
            description=description, references=references
        ))
    
    # Register non-English text symbols (paragraph and left-right modes only)
    add_text_symbol_cmd('\\oe', '\\oe', 'lowercase oe ligature (œ)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_text_symbol_cmd('\\OE', '\\OE', 'uppercase OE ligature (Œ)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_text_symbol_cmd('\\ae', '\\ae', 'lowercase ae ligature (æ)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_text_symbol_cmd('\\AE', '\\AE', 'uppercase AE ligature (Æ)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_text_symbol_cmd('\\aa', '\\aa', 'lowercase a with ring (å)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_text_symbol_cmd('\\AA', '\\AA', 'uppercase A with ring (Å)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_text_symbol_cmd('\\o', '\\o', 'lowercase o with slash (ø)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_text_symbol_cmd('\\O', '\\O', 'uppercase O with slash (Ø)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_text_symbol_cmd('\\l', '\\l', 'lowercase l with slash (ł)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_text_symbol_cmd('\\L', '\\L', 'uppercase L with slash (Ł)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_text_symbol_cmd('\\ss', '\\ss', 'German sharp s (ß)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_text_symbol_cmd('?`', '?`', 'inverted question mark (¿)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_text_symbol_cmd('!`', '!`', 'inverted exclamation mark (¡)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    
    # Register special punctuation symbols
    add_text_symbol_cmd('\\dag', '\\dag', 'dagger symbol (†)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    add_text_symbol_cmd('\\ddag', '\\ddag', 'double dagger symbol (‡)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    add_text_symbol_cmd('\\S', '\\S', 'section symbol (§)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    add_text_symbol_cmd('\\P', '\\P', 'paragraph symbol (¶)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    add_text_symbol_cmd('\\copyright', '\\copyright', 'copyright symbol (©)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_text_symbol_cmd('\\pounds', '\\pounds', 'pound sterling symbol (£)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    
    # Register special character escape commands
    add_text_symbol_cmd('\\#', '\\#', 'hash/number sign (#)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    add_text_symbol_cmd('\\$', '\\$', 'dollar sign ($)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    add_text_symbol_cmd('\\%', '\\%', 'percent sign (%)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    add_text_symbol_cmd('\\&', '\\&', 'ampersand (&)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    add_text_symbol_cmd('\\_', '\\_', 'underscore (_)', [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])


def register_text_spacing_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register text spacing commands in the command definition registry.
    
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for text spacing commands
    references = [{'ref_id': 'lamport_1994', 'sections': '3.3.7, C.7.7', 'pages': '50-51, 191'}]
    
    def add_spacing_cmd(name: str, syntax: str, description: str) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.TEXT_SPACING,
            robustness=CommandRobustness.ROBUST, modes=[CommandMode.MATH, CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT],
            description=description, references=references
        ))
    
    # Register text spacing commands
    add_spacing_cmd('\\,', '\\,', 'thin space')
    add_spacing_cmd('\\!', '\\!', 'negative thin space')
    add_spacing_cmd('\\:', '\\:', 'medium space')
    add_spacing_cmd('\\;', '\\;', 'thick space')
    add_spacing_cmd('\\ ', '\\ ', 'interword space')


def register_delimiter_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register delimiter and delimiter sizing commands in the command definition registry.
    Includes all delimiters from Lamport: ( [ \\{ \\lfloor \\lceil \\langle / | 
    ) ] \\} \\rfloor \\rceil \\rangle \\backslash \\| \\uparrow \\downarrow 
    \\updownarrow \\Uparrow \\Downarrow and \\Updownarrow.
    
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for delimiter commands
    references = [{'ref_id': 'lamport_1994', 'sections': '3.3.4, C.7.5', 'pages': '46-47, 190'}]
    
    def add_delimiter_cmd(name: str, syntax: str, description: str, modes: List[CommandMode]) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.DELIMITER,
            robustness=CommandRobustness.ROBUST, modes=modes,
            description=description, references=references
        ))
    
    # Delimiter sizing commands (primarily math mode)
    add_delimiter_cmd('\\bigl', '\\bigl⟨delimiter⟩', 'applies big sizing to left delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\bigr', '\\bigr⟨delimiter⟩', 'applies big sizing to right delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\Bigl', '\\Bigl⟨delimiter⟩', 'applies Big sizing to left delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\Bigr', '\\Bigr⟨delimiter⟩', 'applies Big sizing to right delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\biggl', '\\biggl⟨delimiter⟩', 'applies bigg sizing to left delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\biggr', '\\biggr⟨delimiter⟩', 'applies bigg sizing to right delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\Biggl', '\\Biggl⟨delimiter⟩', 'applies Bigg sizing to left delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\Biggr', '\\Biggr⟨delimiter⟩', 'applies Bigg sizing to right delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\left', '\\left⟨delimiter⟩...\\right⟨delimiter⟩', 'auto-sizes left delimiter (paired with \\right)', [CommandMode.MATH])
    add_delimiter_cmd('\\right', '\\right⟨delimiter⟩', 'auto-sizes right delimiter (paired with \\left)', [CommandMode.MATH])
    
    # Basic delimiter symbols (parentheses, brackets, and vertical bars work in all modes)
    add_delimiter_cmd('(', '(', 'left parenthesis delimiter', [CommandMode.MATH, CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_delimiter_cmd(')', ')', 'right parenthesis delimiter', [CommandMode.MATH, CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_delimiter_cmd('[', '[', 'left square bracket delimiter', [CommandMode.MATH, CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_delimiter_cmd(']', ']', 'right square bracket delimiter', [CommandMode.MATH, CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_delimiter_cmd('|', '|', 'vertical bar delimiter', [CommandMode.MATH, CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    
    # Brace delimiters 
    add_delimiter_cmd('\\{', '\\{', 'left brace delimiter', [CommandMode.MATH, CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_delimiter_cmd('\\}', '\\}', 'right brace delimiter', [CommandMode.MATH, CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    
    # Math-only named delimiters
    add_delimiter_cmd('\\langle', '\\langle', 'left angle bracket delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\rangle', '\\rangle', 'right angle bracket delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\lceil', '\\lceil', 'left ceiling delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\rceil', '\\rceil', 'right ceiling delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\lfloor', '\\lfloor', 'left floor delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\rfloor', '\\rfloor', 'right floor delimiter', [CommandMode.MATH])
    
    # Slash and backslash delimiters (math mode)
    add_delimiter_cmd('/', '/', 'forward slash delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\backslash', '\\backslash', 'backslash delimiter', [CommandMode.MATH])
    
    # Double vertical bar (math mode)
    add_delimiter_cmd('\\|', '\\|', 'double vertical bar delimiter', [CommandMode.MATH])
    
    # Arrow delimiters (math mode only)
    add_delimiter_cmd('\\uparrow', '\\uparrow', 'up arrow delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\downarrow', '\\downarrow', 'down arrow delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\updownarrow', '\\updownarrow', 'up-down arrow delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\Uparrow', '\\Uparrow', 'double up arrow delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\Downarrow', '\\Downarrow', 'double down arrow delimiter', [CommandMode.MATH])
    add_delimiter_cmd('\\Updownarrow', '\\Updownarrow', 'double up-down arrow delimiter', [CommandMode.MATH])


def register_bibliography_citation_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register bibliography and citation commands in the command definition registry.
    
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for bibliography and citation commands
    references = [{'ref_id': 'lamport_1994', 'sections': '4.3, C.11.3', 'pages': '69-72, 209-210'}]
    
    def add_bibcite_cmd(name: str, syntax: str, description: str, robustness: CommandRobustness, modes: List[CommandMode]) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.BIBLIOGRAPHY,
            robustness=robustness, modes=modes,
            description=description, references=references
        ))
    
    # Register bibliography and citation commands
    add_bibcite_cmd('\\bibliography', '\\bibliography{bibliography_files}', 
                   'specifies the bibliography database files to use', 
                   CommandRobustness.ROBUST, [CommandMode.PARAGRAPH])
    add_bibcite_cmd('\\bibliographystyle', '\\bibliographystyle{bib_style}', 
                   'specifies the bibliography style to use', 
                   CommandRobustness.ROBUST, [CommandMode.PARAGRAPH])
    add_bibcite_cmd('\\bibitem', '\\bibitem[label]{cite_key}', 
                   'creates a bibliography entry with optional label', 
                   CommandRobustness.ROBUST, [CommandMode.PARAGRAPH])
    add_bibcite_cmd('\\cite', '\\cite[text]{key_list}', 
                   'cites one or more bibliography entries with optional prefix text', 
                   CommandRobustness.FRAGILE, [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_bibcite_cmd('\\nocite', '\\nocite{key_list}', 
                   'includes bibliography entries in the bibliography without citing them in text', 
                   CommandRobustness.FRAGILE, [CommandMode.PARAGRAPH])


def register_font_declaration_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register font declaration commands and font commands with arguments in the command definition registry.
    
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for font declaration commands
    references = [{'ref_id': 'lamport_1994', 'sections': '3.1, C.15', 'pages': '36-37, 225-226'}]
    
    def add_font_decl_cmd(name: str, syntax: str, description: str, modes: List[CommandMode]) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.FONT_DECLARATION,
            robustness=CommandRobustness.ROBUST, modes=modes,
            description=description, references=references
        ))
    
    # Register font weight declarations (paragraph and left-right modes only)
    add_font_decl_cmd('\\mdseries', '\\mdseries', 'sets font weight to medium (normal)', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_decl_cmd('\\bfseries', '\\bfseries', 'sets font weight to bold', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    
    # Register font family declarations (paragraph and left-right modes only)
    add_font_decl_cmd('\\rmfamily', '\\rmfamily', 'sets font family to roman (serif)', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_decl_cmd('\\sffamily', '\\sffamily', 'sets font family to sans serif', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_decl_cmd('\\ttfamily', '\\ttfamily', 'sets font family to typewriter (monospace)', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    
    # Register font shape declarations (paragraph and left-right modes only)
    add_font_decl_cmd('\\upshape', '\\upshape', 'sets font shape to upright', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_decl_cmd('\\itshape', '\\itshape', 'sets font shape to italic', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_decl_cmd('\\slshape', '\\slshape', 'sets font shape to slanted', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_decl_cmd('\\scshape', '\\scshape', 'sets font shape to small caps', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    
    # Register font reset declaration (paragraph and left-right modes only)
    add_font_decl_cmd('\\normalfont', '\\normalfont', 'resets font to document default', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    
    # Register font weight commands (can be used in math mode also)
    add_font_decl_cmd('\\textmd', '\\textmd{text}', 'typesets text in medium (normal) weight font', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    add_font_decl_cmd('\\textbf', '\\textbf{text}', 'typesets text in bold weight font', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    
    # Register font family commands (can be used in math mode also)
    add_font_decl_cmd('\\textrm', '\\textrm{text}', 'typesets text in roman (serif) font family', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    add_font_decl_cmd('\\textsf', '\\textsf{text}', 'typesets text in sans serif font family', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    add_font_decl_cmd('\\texttt', '\\texttt{text}', 'typesets text in typewriter (monospace) font family', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    
    # Register font shape commands (can be used in math mode also)
    add_font_decl_cmd('\\textup', '\\textup{text}', 'typesets text in upright font shape', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    add_font_decl_cmd('\\textit', '\\textit{text}', 'typesets text in italic font shape', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    add_font_decl_cmd('\\textsl', '\\textsl{text}', 'typesets text in slanted font shape', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    add_font_decl_cmd('\\textsc', '\\textsc{text}', 'typesets text in small caps font shape', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    
    # Register font reset command (can be used in math mode also)
    add_font_decl_cmd('\\textnormal', '\\textnormal{text}', 'typesets text in document default font', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT, CommandMode.MATH])
    
    # Register legacy 2-letter font commands (LaTeX 2.09 compatibility, deprecated)
    add_font_decl_cmd('\\rm', '\\rm', 'legacy: sets font family to roman (deprecated, use \\rmfamily)', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_decl_cmd('\\sf', '\\sf', 'legacy: sets font family to sans serif (deprecated, use \\sffamily)', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_decl_cmd('\\tt', '\\tt', 'legacy: sets font family to typewriter (deprecated, use \\ttfamily)', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_decl_cmd('\\bf', '\\bf', 'legacy: sets font series to bold (deprecated, use \\bfseries)', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_decl_cmd('\\it', '\\it', 'legacy: sets font shape to italic (deprecated, use \\itshape)', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_decl_cmd('\\sl', '\\sl', 'legacy: sets font shape to slanted (deprecated, use \\slshape)', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_decl_cmd('\\sc', '\\sc', 'legacy: sets font shape to small caps (deprecated, use \\scshape)', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_decl_cmd('\\em', '\\em', 'legacy: emphasis font (contextual italic/upright, deprecated, use \\emph{text})', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_decl_cmd('\\cal', '\\cal', 'legacy: calligraphic font for math mode (deprecated, use \\mathcal{text})', 
                     [CommandMode.MATH])
    add_font_decl_cmd('\\mit', '\\mit', 'legacy: math italic font for math mode (deprecated, use \\mathit{text})', 
                     [CommandMode.MATH])

    # Font size commands (fragile, cannot be used in math mode)
    def add_font_size_cmd(name: str, syntax: str, description: str, modes: List[CommandMode]) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.FONT_DECLARATION,
            robustness=CommandRobustness.FRAGILE, modes=modes,
            description=description, references=references
        ))
    
    add_font_size_cmd('\\tiny', '\\tiny', 'sets font size to tiny', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_size_cmd('\\scriptsize', '\\scriptsize', 'sets font size to script size', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_size_cmd('\\footnotesize', '\\footnotesize', 'sets font size to footnote size', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_size_cmd('\\small', '\\small', 'sets font size to small', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_size_cmd('\\normalsize', '\\normalsize', 'sets font size to normal size', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_size_cmd('\\large', '\\large', 'sets font size to large', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_size_cmd('\\Large', '\\Large', 'sets font size to Large', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_size_cmd('\\LARGE', '\\LARGE', 'sets font size to LARGE', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_size_cmd('\\huge', '\\huge', 'sets font size to huge', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])
    add_font_size_cmd('\\Huge', '\\Huge', 'sets font size to Huge', 
                     [CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT])

        
def register_latex_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register LaTeX commands in the command definition registry.

    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    register_document_commands(registry)
    register_sectioning_commands(registry)
    register_greek_letter_commands(registry)
    register_binary_operation_commands(registry)
    register_relation_commands(registry)
    register_arrow_commands(registry)
    register_misc_symbol_commands(registry)
    register_variable_sized_symbol_commands(registry)
    register_log_like_function_commands(registry)
    register_math_accent_commands(registry)
    register_math_enclosure_commands(registry)
    register_text_accent_commands(registry)
    register_text_symbol_commands(registry)
    register_text_spacing_commands(registry)
    register_delimiter_commands(registry)
    register_bibliography_citation_commands(registry)
    register_font_declaration_commands(registry)
