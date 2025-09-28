# File: generate_command_dictionary.py
# Description: Generate the LaTeX command dictionary
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

from typing import Dict, Any

def generate_223_command_dictionary() -> Dict[str, Any]:
    """
    Generate the LaTeX command dictionary for section 2.2.3 and C.4.1 of [lamport_1994].

    :return: Dict[str, Any], the LaTeX command dictionary
    """

    common_references = [
        {
            'ref_id': 'lamport_1994',
            'sections': '2.2.3, C.4.1',
            'pages': '21-22, 174'
        }
    ]

    sectioning_dictionary = {
        '\\part': {
            'syntax': '\\part[toc_entry]{heading}',
            'command_type': 'sectioning',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': 'starts a major sectional division at the part level; typically used in book classes; optionally adds an entry to the table of contents',
            'references': common_references
        },
        '\\part*': {
            'syntax': '\\part*{heading}',
            'command_type': 'sectioning',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': 'starts a major sectional division at the part level without adding an entry to the table of contents',
            'references': common_references
        },
        '\\chapter': {
            'syntax': '\\chapter[toc_entry]{heading}',
            'command_type': 'sectioning',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': 'starts a major sectional division at the chapter level; typically used in book and report classes; optionally adds an entry to the table of contents',
            'references': common_references
        },
        '\\chapter*': {
            'syntax': '\\chapter*{heading}',
            'command_type': 'sectioning',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': 'starts a major sectional division at the chapter level without adding an entry to the table of contents',
            'references': common_references
        },
        '\\section': {
            'syntax': '\\section[toc_entry]{heading}',
            'command_type': 'sectioning',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': 'starts a major sectional division at the section level; typically used in articles, books, and reports; optionally adds an entry to the table of contents',
            'references': common_references
        },
        '\\section*': {
            'syntax': '\\section*{heading}',
            'command_type': 'sectioning',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': 'starts a major sectional division at the section level without adding an entry to the table of contents',
            'references': common_references
        },
        '\\subsection': {
            'syntax': '\\subsection[toc_entry]{heading}',
            'command_type': 'sectioning',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': 'starts a sectional division at the subsection level; optionally adds an entry to the table of contents',
            'references': common_references
        },
        '\\subsection*': {
            'syntax': '\\subsection*{heading}',
            'command_type': 'sectioning',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': 'starts a sectional division at the subsection level without adding an entry to the table of contents',
            'references': common_references
        },
        '\\subsubsection': {
            'syntax': '\\subsubsection[toc_entry]{heading}',
            'command_type': 'sectioning',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': 'starts a sectional division at the subsubsection level; optionally adds an entry to the table of contents',
            'references': common_references
        },
        '\\subsubsection*': {
            'syntax': '\\subsubsection*{heading}',
            'command_type': 'sectioning',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': 'starts a sectional division at the subsubsection level without adding an entry to the table of contents',
            'references': common_references
        },
        '\\paragraph': {
            'syntax': '\\paragraph[toc_entry]{heading}',
            'command_type': 'sectioning',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': 'starts a sectional division at the paragraph level; optionally adds an entry to the table of contents',
            'references': common_references
        },
        '\\paragraph*': {
            'syntax': '\\paragraph*{heading}',
            'command_type': 'sectioning',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': 'starts a sectional division at the paragraph level without adding an entry to the table of contents',
            'references': common_references
        },
        '\\subparagraph': {
            'syntax': '\\subparagraph[toc_entry]{heading}',
            'command_type': 'sectioning',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': 'starts a sectional division at the subparagraph level; optionally adds an entry to the table of contents',
            'references': common_references
        },
        '\\subparagraph*': {
            'syntax': '\\subparagraph*{heading}',
            'command_type': 'sectioning',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': 'starts a sectional division at the subparagraph level without adding an entry to the table of contents',
            'references': common_references
        }
    }

    return sectioning_dictionary

def generate_332_command_dictionary() -> Dict[str, Any]:
    """
    Generate the LaTeX command dictionary for section 3.3.2 and C.7.3 of [lamport_1994].

    :return: Dict[str, Any], the LaTeX command dictionary
    """

    common_references = [
        {
            'ref_id': 'lamport_1994',
            'sections': '3.3.2, C.7.3',
            'pages': '41-45, 189-190'
        }
    ]

    greek_letter_dictionary = {
        '\\alpha': {
            'syntax': '\\alpha',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter alpha',
            'references': common_references
        },
        '\\beta': {
            'syntax': '\\beta',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter beta',
            'references': common_references
        },
        '\\gamma': {
            'syntax': '\\gamma',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter gamma',
            'references': common_references
        },
        '\\delta': {
            'syntax': '\\delta',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter delta',
            'references': common_references
        },
        '\\epsilon': {
            'syntax': '\\epsilon',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter epsilon',
            'references': common_references
        },
        '\\varepsilon': {
            'syntax': '\\varepsilon',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'variant Greek letter epsilon',
            'references': common_references
        },
        '\\zeta': {
            'syntax': '\\zeta',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter zeta',
            'references': common_references
        },
        '\\eta': {
            'syntax': '\\eta',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter eta',
            'references': common_references
        },
        '\\theta': {
            'syntax': '\\theta',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter theta',
            'references': common_references
        },
        '\\vartheta': {
            'syntax': '\\vartheta',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'variant Greek letter theta',
            'references': common_references
        },
        '\\iota': {
            'syntax': '\\iota',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter iota',
            'references': common_references
        },
        '\\kappa': {
            'syntax': '\\kappa',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter kappa',
            'references': common_references
        },
        '\\lambda': {
            'syntax': '\\lambda',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter lambda',
            'references': common_references
        },
        '\\mu': {
            'syntax': '\\mu',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter mu',
            'references': common_references
        },
        '\\nu': {
            'syntax': '\\nu',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter nu',
            'references': common_references
        },
        '\\xi': {
            'syntax': '\\xi',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter xi',
            'references': common_references
        },
        '\\pi': {
            'syntax': '\\pi',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter pi',
            'references': common_references
        },
        '\\varpi': {
            'syntax': '\\varpi',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'variant Greek letter pi',
            'references': common_references
        },
        '\\rho': {
            'syntax': '\\rho',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter rho',
            'references': common_references
        },
        '\\varrho': {
            'syntax': '\\varrho',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'variant Greek letter rho',
            'references': common_references
        },
        '\\sigma': {
            'syntax': '\\sigma',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter sigma',
            'references': common_references
        },
        '\\varsigma': {
            'syntax': '\\varsigma',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'variant Greek letter sigma',
            'references': common_references
        },
        '\\tau': {
            'syntax': '\\tau',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter tau',
            'references': common_references
        },
        '\\upsilon': {
            'syntax': '\\upsilon',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter upsilon',
            'references': common_references
        },
        '\\phi': {
            'syntax': '\\phi',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter phi',
            'references': common_references
        },
        '\\varphi': {
            'syntax': '\\varphi',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'variant Greek letter phi',
            'references': common_references
        },
        '\\chi': {
            'syntax': '\\chi',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter chi',
            'references': common_references
        },
        '\\psi': {
            'syntax': '\\psi',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter psi',
            'references': common_references
        },
        '\\omega': {
            'syntax': '\\omega',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Greek letter omega',
            'references': common_references
        },
        '\\Gamma': {
            'syntax': '\\Gamma',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'uppercase Greek letter Gamma',
            'references': common_references
        },
        '\\Delta': {
            'syntax': '\\Delta',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'uppercase Greek letter Delta',
            'references': common_references
        },
        '\\Theta': {
            'syntax': '\\Theta',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'uppercase Greek letter Theta',
            'references': common_references
        },
        '\\Lambda': {
            'syntax': '\\Lambda',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'uppercase Greek letter Lambda',
            'references': common_references
        },
        '\\Xi': {
            'syntax': '\\Xi',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'uppercase Greek letter Xi',
            'references': common_references
        },
        '\\Pi': {
            'syntax': '\\Pi',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'uppercase Greek letter Pi',
            'references': common_references
        },
        '\\Sigma': {
            'syntax': '\\Sigma',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'uppercase Greek letter Sigma',
            'references': common_references
        },
        '\\Upsilon': {
            'syntax': '\\Upsilon',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'uppercase Greek letter Upsilon',
            'references': common_references
        },
        '\\Phi': {
            'syntax': '\\Phi',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'uppercase Greek letter Phi',
            'references': common_references
        },
        '\\Psi': {
            'syntax': '\\Psi',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'uppercase Greek letter Psi',
            'references': common_references
        },
        '\\Omega': {
            'syntax': '\\Omega',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'uppercase Greek letter Omega',
            'references': common_references
        },
    }

    binary_operations_dictionary = {
        '\\pm': {
            'syntax': '\\pm',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'plus-minus sign',
            'references': common_references
        },
        '\\mp': {
            'syntax': '\\mp',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'minus-plus sign',
            'references': common_references
        },
        '\\times': {
            'syntax': '\\times',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'multiplication sign',
            'references': common_references
        },
        '\\div': {
            'syntax': '\\div',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'division sign',
            'references': common_references
        },
        '\\ast': {
            'syntax': '\\ast',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'asterisk operator',
            'references': common_references
        },
        '\\star': {
            'syntax': '\\star',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'star operator',
            'references': common_references
        },
        '\\circ': {
            'syntax': '\\circ',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'circle operator',
            'references': common_references
        },
        '\\bullet': {
            'syntax': '\\bullet',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'bullet operator',
            'references': common_references
        },
        '\\cdot': {
            'syntax': '\\cdot',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'centered dot operator',
            'references': common_references
        },
        '\\cap': {
            'syntax': '\\cap',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'intersection operator',
            'references': common_references
        },
        '\\cup': {
            'syntax': '\\cup',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'union operator',
            'references': common_references
        },
        '\\uplus': {
            'syntax': '\\uplus',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'disjoint union operator',
            'references': common_references
        },
        '\\sqcap': {
            'syntax': '\\sqcap',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'square intersection operator',
            'references': common_references
        },
        '\\sqcup': {
            'syntax': '\\sqcup',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'square union operator',
            'references': common_references
        },
        '\\vee': {
            'syntax': '\\vee',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'logical or operator',
            'references': common_references
        },
        '\\wedge': {
            'syntax': '\\wedge',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'logical and operator',
            'references': common_references
        },
        '\\setminus': {
            'syntax': '\\setminus',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'set difference operator',
            'references': common_references
        },
        '\\wr': {
            'syntax': '\\wr',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'wreath product operator',
            'references': common_references
        },
        '\\diamond': {
            'syntax': '\\diamond',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'diamond operator',
            'references': common_references
        },
        '\\bigtriangleup': {
            'syntax': '\\bigtriangleup',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'big triangle up operator',
            'references': common_references
        },
        '\\bigtriangledown': {
            'syntax': '\\bigtriangledown',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'big triangle down operator',
            'references': common_references
        },
        '\\triangleleft': {
            'syntax': '\\triangleleft',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'triangle left operator',
            'references': common_references
        },
        '\\triangleright': {
            'syntax': '\\triangleright',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'triangle right operator',
            'references': common_references
        },
        '\\lhd': {
            'syntax': '\\lhd',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'left harpoon down operator',
            'references': common_references
        },
        '\\rhd': {
            'syntax': '\\rhd',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'right harpoon down operator',
            'references': common_references
        },
        '\\unlhd': {
            'syntax': '\\unlhd',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'underlined left harpoon down operator',
            'references': common_references
        },
        '\\unrhd': {
            'syntax': '\\unrhd',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'underlined right harpoon down operator',
            'references': common_references
        },
        '\\oplus': {
            'syntax': '\\oplus',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'circled plus operator',
            'references': common_references
        },
        '\\ominus': {
            'syntax': '\\ominus',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'circled minus operator',
            'references': common_references
        },
        '\\otimes': {
            'syntax': '\\otimes',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'circled times operator',
            'references': common_references
        },
        '\\oslash': {
            'syntax': '\\oslash',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'circled slash operator',
            'references': common_references
        },
        '\\odot': {
            'syntax': '\\odot',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'circled dot operator',
            'references': common_references
        },
        '\\bigcirc': {
            'syntax': '\\bigcirc',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'big circle operator',
            'references': common_references
        },
        '\\dagger': {
            'syntax': '\\dagger',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'dagger operator',
            'references': common_references
        },
        '\\ddagger': {
            'syntax': '\\ddagger',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'double dagger operator',
            'references': common_references
        },
        '\\amalg': {
            'syntax': '\\amalg',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'amalgamation operator',
            'references': common_references
        },
    }

    relation_symbols_dictionary = {
        '\\leq': {
            'syntax': '\\leq',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'less than or equal to sign',
            'references': common_references
        },
        '\\prec': {
            'syntax': '\\prec',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'precedes',
            'references': common_references
        },
        '\\preceq': {
            'syntax': '\\preceq',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'precedes or equals',
            'references': common_references
        },
        '\\ll': {
            'syntax': '\\ll',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'much less than',
            'references': common_references
        },
        '\\subset': {
            'syntax': '\\subset',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'subset of',
            'references': common_references
        },
        '\\subseteq': {
            'syntax': '\\subseteq',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'subset of or equal to',
            'references': common_references
        },
        '\\sqsubset': {
            'syntax': '\\sqsubset',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'square subset of',
            'references': common_references
        },
        '\\sqsubseteq': {
            'syntax': '\\sqsubseteq',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'square subset of or equal to',
            'references': common_references
        },
        '\\in': {
            'syntax': '\\in',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'element of',
            'references': common_references
        },
        '\\vdash': {
            'syntax': '\\vdash',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'entails (turnstile)',
            'references': common_references
        },
        '\\geq': {
            'syntax': '\\geq',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'greater than or equal to',
            'references': common_references
        },
        '\\succ': {
            'syntax': '\\succ',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'succeeds',
            'references': common_references
        },
        '\\succeq': {
            'syntax': '\\succeq',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'succeeds or equals',
            'references': common_references
        },
        '\\gg': {
            'syntax': '\\gg',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'much greater than',
            'references': common_references
        },
        '\\sqsupset': {
            'syntax': '\\sqsupset',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'square superset of',
            'references': common_references
        },
        '\\sqsupseteq': {
            'syntax': '\\sqsupseteq',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'square superset of or equal to',
            'references': common_references
        },
        '\\ni': {
            'syntax': '\\ni',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'contains as member',
            'references': common_references
        },
        '\\dashv': {
            'syntax': '\\dashv',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'dash with vertical bar',
            'references': common_references
        },
        '\\equiv': {
            'syntax': '\\equiv',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'identically equal to',
            'references': common_references
        },
        '\\sim': {
            'syntax': '\\sim',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'similar to',
            'references': common_references
        },
        '\\simeq': {
            'syntax': '\\simeq',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'asymptotically equal to',
            'references': common_references
        },
        '\\asymp': {
            'syntax': '\\asymp',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'asymptotically equal to',
            'references': common_references
        },
        '\\approx': {
            'syntax': '\\approx',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'approximately equal to',
            'references': common_references
        },
        '\\cong': {
            'syntax': '\\cong',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'congruent to',
            'references': common_references
        },
        '\\neq': {
            'syntax': '\\neq',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'not equal to',
            'references': common_references
        },
        '\\doteq': {
            'syntax': '\\doteq',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'approaches the value',
            'references': common_references
        },
        '\\notin': {
            'syntax': '\\notin',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'not an element of',
            'references': common_references
        },
        '\\models': {
            'syntax': '\\models',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'models (double turnstile)',
            'references': common_references
        },
        '\\perp': {
            'syntax': '\\perp',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'perpendicular to',
            'references': common_references
        },
        '\\mid': {
            'syntax': '\\mid',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'such that (vertical bar)',
            'references': common_references
        },
        '\\parallel': {
            'syntax': '\\parallel',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'parallel to',
            'references': common_references
        },
        '\\bowtie': {
            'syntax': '\\bowtie',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'bowtie relation',
            'references': common_references
        },
        '\\Join': {
            'syntax': '\\Join',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'join relation',
            'references': common_references
        },
        '\\smile': {
            'syntax': '\\smile',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'smile relation',
            'references': common_references
        },
        '\\frown': {
            'syntax': '\\frown',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'frown relation',
            'references': common_references
        },
        '\\propto': {
            'syntax': '\\propto',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'proportional to',
            'references': common_references
        },
    }

    arrow_symbols_dictionary = {
        '\\leftarrow': {
            'syntax': '\\leftarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'left arrow',
            'references': common_references
        },
        '\\Leftarrow': {
            'syntax': '\\Leftarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'double left arrow',
            'references': common_references
        },
        '\\rightarrow': {
            'syntax': '\\rightarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'right arrow',
            'references': common_references
        },
        '\\Rightarrow': {
            'syntax': '\\Rightarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'double right arrow',
            'references': common_references
        },
        '\\leftrightarrow': {
            'syntax': '\\leftrightarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'left-right arrow',
            'references': common_references
        },
        '\\Leftrightarrow': {
            'syntax': '\\Leftrightarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'double left-right arrow',
            'references': common_references
        },
        '\\mapsto': {
            'syntax': '\\mapsto',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'mapsto arrow',
            'references': common_references
        },
        '\\hookleftarrow': {
            'syntax': '\\hookleftarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'hook left arrow',
            'references': common_references
        },
        '\\leftharpoonup': {
            'syntax': '\\leftharpoonup',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'left harpoon up',
            'references': common_references
        },
        '\\leftharpoondown': {
            'syntax': '\\leftharpoondown',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'left harpoon down',
            'references': common_references
        },
        '\\rightleftharpoons': {
            'syntax': '\\rightleftharpoons',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'right and left harpoons',
            'references': common_references
        },
        '\\longleftarrow': {
            'syntax': '\\longleftarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'long left arrow',
            'references': common_references
        },
        '\\Longleftarrow': {
            'syntax': '\\Longleftarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'long double left arrow',
            'references': common_references
        },
        '\\longrightarrow': {
            'syntax': '\\longrightarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'long right arrow',
            'references': common_references
        },
        '\\Longrightarrow': {
            'syntax': '\\Longrightarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'long double right arrow',
            'references': common_references
        },
        '\\longleftrightarrow': {
            'syntax': '\\longleftrightarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'long left-right arrow',
            'references': common_references
        },
        '\\Longleftrightarrow': {
            'syntax': '\\Longleftrightarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'long double left-right arrow',
            'references': common_references
        },
        '\\longmapsto': {
            'syntax': '\\longmapsto',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'long mapsto arrow',
            'references': common_references
        },
        '\\hookrightarrow': {
            'syntax': '\\hookrightarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'hook right arrow',
            'references': common_references
        },
        '\\rightharpoonup': {
            'syntax': '\\rightharpoonup',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'right harpoon up',
            'references': common_references
        },
        '\\rightharpoondown': {
            'syntax': '\\rightharpoondown',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'right harpoon down',
            'references': common_references
        },
        '\\leadsto': {
            'syntax': '\\leadsto',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'leads to arrow',
            'references': common_references
        },
        '\\uparrow': {
            'syntax': '\\uparrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'up arrow',
            'references': common_references
        },
        '\\Uparrow': {
            'syntax': '\\Uparrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'double up arrow',
            'references': common_references
        },
        '\\downarrow': {
            'syntax': '\\downarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'down arrow',
            'references': common_references
        },
        '\\Downarrow': {
            'syntax': '\\Downarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'double down arrow',
            'references': common_references
        },
        '\\updownarrow': {
            'syntax': '\\updownarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'up-down arrow',
            'references': common_references
        },
        '\\Updownarrow': {
            'syntax': '\\Updownarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'double up-down arrow',
            'references': common_references
        },
        '\\nearrow': {
            'syntax': '\\nearrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'north-east arrow',
            'references': common_references
        },
        '\\searrow': {
            'syntax': '\\searrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'south-east arrow',
            'references': common_references
        },
        '\\swarrow': {
            'syntax': '\\swarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'south-west arrow',
            'references': common_references
        },
        '\\nwarrow': {
            'syntax': '\\nwarrow',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'north-west arrow',
            'references': common_references
        },
    }

    misc_symbols_dictionary = {
        '\\aleph': {
            'syntax': '\\aleph',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'aleph symbol',
            'references': common_references
        },
        '\\hbar': {
            'syntax': '\\hbar',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'h-bar (Planck constant over 2π)',
            'references': common_references
        },
        '\\imath': {
            'syntax': '\\imath',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'dotless i',
            'references': common_references
        },
        '\\jmath': {
            'syntax': '\\jmath',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'dotless j',
            'references': common_references
        },
        '\\ell': {
            'syntax': '\\ell',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'script letter l',
            'references': common_references
        },
        '\\wp': {
            'syntax': '\\wp',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'Weierstrass p',
            'references': common_references
        },
        '\\Re': {
            'syntax': '\\Re',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'real part',
            'references': common_references
        },
        '\\Im': {
            'syntax': '\\Im',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'imaginary part',
            'references': common_references
        },
        '\\mho': {
            'syntax': '\\mho',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'mho (conductance)',
            'references': common_references
        },
        '\\prime': {
            'syntax': '\\prime',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'prime symbol',
            'references': common_references
        },
        '\\emptyset': {
            'syntax': '\\emptyset',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'empty set',
            'references': common_references
        },
        '\\nabla': {
            'syntax': '\\nabla',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'nabla (del operator)',
            'references': common_references
        },
        '\\surd': {
            'syntax': '\\surd',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'square root sign',
            'references': common_references
        },
        '\\top': {
            'syntax': '\\top',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'top (truth)',
            'references': common_references
        },
        '\\bot': {
            'syntax': '\\bot',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'bottom (falsity)',
            'references': common_references
        },
        '\\|': {
            'syntax': '\\|',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'vertical double bar',
            'references': common_references
        },
        '\\angle': {
            'syntax': '\\angle',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'angle symbol',
            'references': common_references
        },
        '\\forall': {
            'syntax': '\\forall',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'for all',
            'references': common_references
        },
        '\\exists': {
            'syntax': '\\exists',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'there exists',
            'references': common_references
        },
        '\\neg': {
            'syntax': '\\neg',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'negation',
            'references': common_references
        },
        '\\flat': {
            'syntax': '\\flat',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'flat (music)',
            'references': common_references
        },
        '\\natural': {
            'syntax': '\\natural',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'natural (music)',
            'references': common_references
        },
        '\\sharp': {
            'syntax': '\\sharp',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'sharp (music)',
            'references': common_references
        },
        '\\backslash': {
            'syntax': '\\backslash',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'backslash',
            'references': common_references
        },
        '\\partial': {
            'syntax': '\\partial',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'partial derivative symbol',
            'references': common_references
        },
        '\\infty': {
            'syntax': '\\infty',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'infinity symbol',
            'references': common_references
        },
        '\\Box': {
            'syntax': '\\Box',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'box symbol',
            'references': common_references
        },
        '\\Diamond': {
            'syntax': '\\Diamond',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'diamond symbol',
            'references': common_references
        },
        '\\triangle': {
            'syntax': '\\triangle',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'triangle symbol',
            'references': common_references
        },
        '\\clubsuit': {
            'syntax': '\\clubsuit',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'club suit',
            'references': common_references
        },
        '\\diamondsuit': {
            'syntax': '\\diamondsuit',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'diamond suit',
            'references': common_references
        },
        '\\heartsuit': {
            'syntax': '\\heartsuit',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'heart suit',
            'references': common_references
        },
        '\\spadesuit': {
            'syntax': '\\spadesuit',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'spade suit',
            'references': common_references
        },
    }

    variable_sized_symbols_dictionary = {
        '\\sum': {
            'syntax': '\\sum',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'summation symbol',
            'references': common_references
        },
        '\\prod': {
            'syntax': '\\prod',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'product symbol',
            'references': common_references
        },
        '\\coprod': {
            'syntax': '\\coprod',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'coproduct symbol',
            'references': common_references
        },
        '\\int': {
            'syntax': '\\int',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'integral symbol',
            'references': common_references
        },
        '\\oint': {
            'syntax': '\\oint',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'contour integral symbol',
            'references': common_references
        },
        '\\bigcap': {
            'syntax': '\\bigcap',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'big intersection symbol',
            'references': common_references
        },
        '\\bigcup': {
            'syntax': '\\bigcup',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'big union symbol',
            'references': common_references
        },
        '\\bigvee': {
            'syntax': '\\bigvee',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'big logical or symbol',
            'references': common_references
        },
        '\\bigwedge': {
            'syntax': '\\bigwedge',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'big logical and symbol',
            'references': common_references
        },
        '\\bigodot': {
            'syntax': '\\bigodot',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'big circled dot symbol',
            'references': common_references
        },
        '\\bigotimes': {
            'syntax': '\\bigotimes',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'big circled times symbol',
            'references': common_references
        },
        '\\bigoplus': {
            'syntax': '\\bigoplus',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'big circled plus symbol',
            'references': common_references
        },
        '\\biguplus': {
            'syntax': '\\biguplus',
            'command_type': 'math symbol',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'big disjoint union symbol',
            'references': common_references
        },
    }

    log_like_function_dictionary = {
        '\\arccos': {
            'syntax': '\\arccos',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'inverse cosine function',
            'references': common_references
        },
        '\\arcsin': {
            'syntax': '\\arcsin',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'inverse sine function',
            'references': common_references
        },
        '\\arctan': {
            'syntax': '\\arctan',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'inverse tangent function',
            'references': common_references
        },
        '\\arg': {
            'syntax': '\\arg',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'argument of a complex number',
            'references': common_references
        },
        '\\cos': {
            'syntax': '\\cos',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'cosine function',
            'references': common_references
        },
        '\\cosh': {
            'syntax': '\\cosh',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'hyperbolic cosine function',
            'references': common_references
        },
        '\\cot': {
            'syntax': '\\cot{text}',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'cotangent function',
            'references': common_references
        },
        '\\coth': {
            'syntax': '\\coth',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'hyperbolic cotangent function',
            'references': common_references
        },
        '\\csc': {
            'syntax': '\\csc',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'cosecant function',
            'references': common_references
        },
        '\\deg': {
            'syntax': '\\deg{text}',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'degree of a polynomial or vertex',
            'references': common_references
        },
        '\\det': {
            'syntax': '\\det',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'determinant',
            'references': common_references
        },
        '\\dim': {
            'syntax': '\\dim',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'dimension',
            'references': common_references
        },
        '\\exp': {
            'syntax': '\\exp',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'exponential function',
            'references': common_references
        },
        '\\gcd': {
            'syntax': '\\gcd',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'greatest common divisor',
            'references': common_references
        },
        '\\hom': {
            'syntax': '\\hom',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'homomorphism set',
            'references': common_references
        },
        '\\inf': {
            'syntax': '\\inf',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'infimum',
            'references': common_references
        },
        '\\ker': {
            'syntax': '\\ker',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'kernel',
            'references': common_references
        },
        '\\lg': {
            'syntax': '\\lg',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'base-10 logarithm',
            'references': common_references
        },
        '\\lim': {
            'syntax': '\\lim',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'limit',
            'references': common_references
        },
        '\\liminf': {
            'syntax': '\\liminf',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'limit inferior',
            'references': common_references
        },
        '\\limsup': {
            'syntax': '\\limsup',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'limit superior',
            'references': common_references
        },
        '\\ln': {
            'syntax': '\\ln',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'natural logarithm',
            'references': common_references
        },
        '\\log': {
            'syntax': '\\log',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'logarithm',
            'references': common_references
        },
        '\\max': {
            'syntax': '\\max',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'maximum',
            'references': common_references
        },
        '\\min': {
            'syntax': '\\min',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'minimum',
            'references': common_references
        },
        '\\Pr': {
            'syntax': '\\Pr',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'probability',
            'references': common_references
        },
        '\\sec': {
            'syntax': '\\sec',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'secant function',
            'references': common_references
        },
        '\\sin': {
            'syntax': '\\sin',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'sine function',
            'references': common_references
        },
        '\\sinh': {
            'syntax': '\\sinh',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'hyperbolic sine function',
            'references': common_references
        },
        '\\sup': {
            'syntax': '\\sup',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'supremum',
            'references': common_references
        },
        '\\tan': {
            'syntax': '\\tan',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'tangent function',
            'references': common_references
        },
        '\\tanh': {
            'syntax': '\\tanh',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'hyperbolic tangent function',
            'references': common_references
        },
        '\\bmod': {
            'syntax': '\\bmod',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'modulus operation',
            'references': common_references
        },   
        '\\pmod': {
            'syntax': '\\pmod{n}',
            'command_type': 'math function',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'typesets the modulus in congruence relations, displaying (mod n) in math mode',
            'references': common_references
        },
    }

    # \mathcal is mentioned in 3.3.2 in [lamport_1994] but not generate here.
    # this is instead defined in sections 3.3.8 and C.7.8
    
    math_dictionary = dict()
    math_dictionary.update(greek_letter_dictionary)
    math_dictionary.update(binary_operations_dictionary)
    math_dictionary.update(relation_symbols_dictionary)
    math_dictionary.update(arrow_symbols_dictionary)
    math_dictionary.update(misc_symbols_dictionary)
    math_dictionary.update(variable_sized_symbols_dictionary)
    math_dictionary.update(log_like_function_dictionary)

    return math_dictionary

def generate_336_command_dictionary() -> Dict[str, Any]:
    """
    Generate the LaTeX command dictionary for section 3.3.6 and C.7.6 of [lamport_1994].
    
    :return: Dict[str, Any], the LaTeX command dictionary
    """

    common_references = [
        {
            'ref_id': 'lamport_1994',
            'sections': '3.3.6, C.7.6',
            'pages': '49-50, 190-191'
        }
    ]

    math_accent_dictionary = {
        '\\hat': {
            'syntax': '\\hat{text}',
            'command_type': 'math accent',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'draw hat over text',
            'references': common_references
        },
        '\\check': {
            'syntax': '\\check{text}',
            'command_type': 'math accent',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'draw check accent over text',
            'references': common_references
        },
        '\\breve': {
            'syntax': '\\breve{text}',
            'command_type': 'math accent',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'draw breve accent over text',
            'references': common_references
        },
        '\\acute': {
            'syntax': '\\acute{text}',
            'command_type': 'math accent',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'draw acute accent over text',
            'references': common_references
        },
        '\\grave': {
            'syntax': '\\grave{text}',
            'command_type': 'math accent',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'draw grave accent over text',
            'references': common_references
        },
        '\\tilde': {
            'syntax': '\\tilde{text}',
            'command_type': 'math accent',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'draw tilde over text',
            'references': common_references
        },
        '\\bar': {
            'syntax': '\\bar{text}',
            'command_type': 'math accent',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'draw bar over text',
            'references': common_references
        },
        '\\vec': {
            'syntax': '\\vec{text}',
            'command_type': 'math accent',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'draw vector arrow over text',
            'references': common_references
        },
        '\\dot': {
            'syntax': '\\dot{text}',
            'command_type': 'math accent',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'draw single dot over text',
            'references': common_references
        },
        '\\ddot': {
            'syntax': '\\ddot{text}',
            'command_type': 'math accent',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'draw double dot over text',
            'references': common_references
        },
        '\\widehat': {
            'syntax': '\\widehat{text}',
            'command_type': 'math accent',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'draw wide hat over text',
            'references': common_references
        },
        '\\widetilde': {
            'syntax': '\\widetilde{text}',
            'command_type': 'math accent',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'draw wide tilde over text',
            'references': common_references
        }        
    }

    math_enclosure_dictionary = {
        '\\overline': {
            'syntax': '\\overline{text}',
            'command_type': 'enclosure',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'draw horizontal line over text',
            'references': common_references
        },
        '\\underline': {
            'syntax': '\\underline{text}',
            'command_type': 'enclosure',
            'robustness': 'fragile',
            'modes': ['math', 'paragraph', 'LR'],
            'description': 'draw horizontal line under text',
            'references': common_references
        },
        '\\overbrace': {
            'syntax': '\\overbrace{text}',
            'command_type': 'enclosure',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'draw horizontal brace over text',
            'references': common_references
        },
        '\\underbrace': {
            'syntax': '\\underbrace{text}',
            'command_type': 'enclosure',
            'robustness': 'robust',
            'modes': ['math'],
            'description': 'draw horizontal brace under text',
            'references': common_references
        }
    }

    # imath and jmath are mentioned in 3.3.6 and C.7.6 but not generated in this method
    # as they are defined in section 3.3.2 in [lamport_1994].

    math_relation_modifier_dictionary = {
        '\\stackrel': {
            'syntax': '\\stackrel{top}{bottom}', 
            'command_type': 'math relation modifier',            
            'robustness': 'fragile', 
            'modes': ['math'], 
            'description': 'draw one symbol or text above another with the first argument in small type',
            'references': common_references
        }
    }

    math_dictionary = dict()
    math_dictionary.update(math_accent_dictionary)
    math_dictionary.update(math_enclosure_dictionary)  
    math_dictionary.update(math_relation_modifier_dictionary)

    return math_dictionary


def generate_337_command_dictionary() -> Dict[str, Any]:
    """
    Generate the LaTeX command dictionary for section 3.3.7 and C.7.7 of [lamport_1994].

    :return: Dict[str, Any], the LaTeX command dictionary
    """

    common_references = [
        {
            'ref_id': 'lamport_1994',
            'sections': '3.3.7, C.7.7',
            'pages': '50-51, 191'
        }
    ]

    spacing_dictionary = {
        '\\,': {
            'syntax': '\\,',
            'command_type': 'spacing',
            'robustness': 'robust',
            'modes': ['math', 'paragraph', 'LR'],
            'description': 'thin space',
            'references': common_references
        },
        '\\!': {
            'syntax': '\\!',
            'command_type': 'spacing',
            'robustness': 'robust',
            'modes': ['math', 'paragraph', 'LR'],
            'description': 'negative thin space',
            'references': common_references
        },
        '\\:': {
            'syntax': '\\:',
            'command_type': 'spacing',
            'robustness': 'robust',
            'modes': ['math', 'paragraph', 'LR'],
            'description': 'medium space',
            'references': common_references
        },
        '\\;': {
            'syntax': '\\;',
            'command_type': 'spacing',
            'robustness': 'robust',
            'modes': ['math', 'paragraph', 'LR'],
            'description': 'thick space',
            'references': common_references
        },
        '\\ ': {
            'syntax': '\\ ',
            'command_type': 'spacing',
            'robustness': 'robust',
            'modes': ['math', 'paragraph', 'LR'],
            'description': 'interword space',
            'references': common_references
        }
    }

    return spacing_dictionary

def generate_command_dictionary() -> Dict[str, Any]:
    """
    Generate the LaTeX command dictionary.

    :return: Dict[str, Any], the LaTeX command dictionary
    """

    command_dictionary = dict()
    command_dictionary.update(generate_223_command_dictionary())  # section 2.2.3 and C.4.1
    command_dictionary.update(generate_332_command_dictionary())  # section 3.3.2 and C.7.3
    command_dictionary.update(generate_336_command_dictionary())  # section 3.3.6 and C.7.6
    command_dictionary.update(generate_337_command_dictionary())  # section 3.3.7 and C.7.7

    return command_dictionary
