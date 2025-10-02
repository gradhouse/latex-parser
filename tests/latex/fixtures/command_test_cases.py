# File: command_test_cases.py
# Description: Test case fixtures for LaTeX command methods
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

# Test cases for find_all_commands basic functionality
FIND_ALL_COMMANDS_BASIC_TESTS = [
    {
        'description': 'simple letter commands',
        'content': r'\textbf{hello} \alpha \beta',
        'expected': [
            ('textbf', 0, 7),
            ('alpha', 15, 21),
            ('beta', 22, 27)
        ]
    },
    {
        'description': 'non-letter commands',
        'content': r'text \@ \! \# content',
        'expected': [
            ('@', 5, 7),
            ('!', 8, 10),
            ('#', 11, 13)
        ]
    },
    {
        'description': 'mixed commands',
        'content': r'\textbf \@ \alpha \!',
        'expected': [
            ('textbf', 0, 7),
            ('@', 8, 10),
            ('alpha', 11, 17),
            ('!', 18, 20)
        ]
    },
    {
        'description': 'commands with star forms',
        'content': r'\section{title} \section*{starred}',
        'expected': [
            ('section', 0, 8),
            ('section*', 16, 25)
        ]
    }
]

# Test cases for commands with @ symbol
FIND_ALL_COMMANDS_AT_SYMBOL_TESTS = [
    {
        'description': 'commands with @ as initial character',
        'content': r'\@chapter{title} \@section{content}',
        'expected': [
            ('@chapter', 0, 9),
            ('@section', 17, 26)
        ]
    },
    {
        'description': 'mixed @ usage - standalone and initial',
        'content': r'\@ \@section \alpha \!',
        'expected': [
            ('@', 0, 2),
            ('@section', 3, 12),
            ('alpha', 13, 19),
            ('!', 20, 22)
        ]
    }
]

# Test cases for whitespace handling
FIND_ALL_COMMANDS_WHITESPACE_TESTS = [
    {
        'description': 'commands with trailing spaces',
        'content': r'\alpha \beta  \gamma	\delta',
        'expected': [
            ('alpha', 0, 6),
            ('beta', 7, 12),
            ('gamma', 14, 20),
            ('delta', 21, 27)
        ]
    },
    {
        'description': 'commands with newlines',
        'content': r'\alpha' + '\n' + r'\beta' + '\n\n' + r'\gamma',
        'expected': [
            ('alpha', 0, 6),
            ('beta', 7, 12),
            ('gamma', 14, 20)
        ]
    }
]

# Test cases for edge cases
FIND_ALL_COMMANDS_EDGE_TESTS = [
    {
        'description': 'empty content',
        'content': '',
        'expected': []
    },
    {
        'description': 'no commands',
        'content': 'This is just regular text with no commands.',
        'expected': []
    },
    {
        'description': 'escaped backslashes',
        'content': r'\\textbf \textbf \\',
        'expected': [
            ('textbf', 1, 8),  # \textbf (the \\ overlap is handled)
            ('textbf', 9, 16), # Second \textbf  
            ('\\', 17, 19)     # Final \\ (no overlap)
        ]
    }
]

# Test cases for find_command method
FIND_COMMAND_SPECIFIC_TESTS = [
    {
        'description': 'find specific letter command',
        'command_name': 'textbf',
        'content': r'\textbf{hello} \textit{world} \textbf{again}',
        'expected': [
            (0, 7),   # First \textbf
            (30, 37)  # Second \textbf
        ]
    },
    {
        'description': 'find non-letter command',
        'command_name': '@',
        'content': r'text \@ more \! text \@ again',
        'expected': [
            (5, 7),   # First \@
            (21, 23)  # Second \@
        ]
    },
    {
        'description': 'find starred command',
        'command_name': 'section*',
        'content': r'\section{title} \section*{starred} \section{normal}',
        'expected': [
            (16, 25)  # \section*
        ]
    },
    {
        'description': 'find regular command (not starred)',
        'command_name': 'section',
        'content': r'\section{title} \section*{starred} \section{normal}',
        'expected': [
            (0, 8),   # First \section
            (35, 43)  # Third \section (not the starred one)
        ]
    }
]

# Test cases for @ symbol commands specifically
FIND_COMMAND_AT_SYMBOL_TESTS = [
    {
        'description': 'find @ as non-letter command',
        'command_name': '@',
        'content': r'\@ \@chapter \@section',
        'expected': [
            (0, 2)  # Only the standalone \@
        ]
    },
    {
        'description': 'find @chapter command',
        'command_name': '@chapter',
        'content': r'\@ \@chapter \@section',
        'expected': [
            (3, 12)  # \@chapter
        ]
    },
    {
        'description': 'find @section command',
        'command_name': '@section',
        'content': r'\@ \@chapter \@section',
        'expected': [
            (13, 22)  # \@section
        ]
    }
]

# Test cases for boundary conditions
FIND_COMMAND_BOUNDARY_TESTS = [
    {
        'description': 'command boundaries',
        'command_name': 'text',
        'content': r'\text \textbf \textbold \textt',
        'expected': [
            (0, 5)  # Only \text, not \textbf or \textbold
        ]
    },
    {
        'description': 'case sensitivity',
        'command_name': 'alpha',
        'content': r'\Alpha \alpha \BETA \beta',
        'expected': [
            (7, 13)  # Only \alpha (lowercase)
        ]
    }
]

# Test cases for complex real-world scenarios
FIND_ALL_COMMANDS_COMPLEX_TESTS = [
    {
        'description': 'complex document structure',
        'content': r'''\documentclass{article}
\usepackage{amsmath}
\begin{document}
\section*{Introduction}
This is \textbf{bold} and \textit{italic} text.
\[ x = \frac{a}{b} \]
\cite{ref1} and \ref{fig:1}
\end{document}''',
        'expected_commands': [
            'documentclass', 'usepackage', 'begin', 'section*', 'textbf', 
            'textit', 'frac', 'cite', 'ref', 'end'
        ]
    }
]

# Error handling test cases
FIND_COMMANDS_ERROR_TESTS = [
    {
        'description': 'empty command name',
        'command_name': '',
        'content': r'\textbf{hello}',
        'expected': []
    }
]

# Coverage completion test cases for missing lines
FIND_COMMAND_COVERAGE_TESTS = [
    {
        'description': 'Find single non-letter command $ (line 88 coverage)',
        'command_name': '$',
        'content': r'\$ and \& and \%',
        'expected': [(0, 2)]
    },
    {
        'description': 'Find @ command with star (line 96 coverage)',
        'command_name': '@name*',
        'content': r'\@name* text',
        'expected': [(0, 7)]
    },
    {
        'description': 'Find & command for non-letter end calculation (line 117 coverage)',
        'command_name': '&',
        'content': r'\& symbol',
        'expected': [(0, 2)]
    }
]

# Additional LaTeX command corner cases
FIND_ALL_COMMANDS_LATEX_CORNER_CASES = [
    {
        'description': 'Commands with digits and underscores (valid in makeatletter)',
        'content': r'\command@internal \test_helper \name123',
        'expected': [
            ('command', 0, 8),      # \command (@ not part of name when not initial)
            ('test', 18, 23),       # \test (_ not part of command name)  
            ('name', 31, 36)        # \name (digits not part of command name)
        ]
    },
    {
        'description': 'Commands with Unicode characters (only ASCII letters supported)',
        'content': r'\été \naïve \résumé',
        'expected': [
            ('na', 5, 8),           # \na (ï not supported, so parses as \na + ïve)
            ('r', 12, 14)           # \r (é not supported, so parses as \r + ésumé)
        ]
    },
    {
        'description': 'Multiple consecutive backslashes',
        'content': r'\\\\text \\\\ \\newline',
        'expected': [
            ('\\', 0, 2),           # First \\
            ('text', 3, 8),         # \text (space after second \\)
            ('\\', 9, 11),          # Third \\
            ('\\', 11, 13),         # Fourth \\
            ('newline', 15, 23)     # \newline (space after fifth \\)
        ]
    },
    {
        'description': 'Commands at end of content (no trailing space)',
        'content': r'\end{document}\bye',
        'expected': [
            ('end', 0, 4),
            ('bye', 14, 18)
        ]
    },
    {
        'description': 'Commands with immediate braces and brackets',
        'content': r'\textbf{bold}\cite[p.5]{ref}\frac{1}{2}',
        'expected': [
            ('textbf', 0, 7),
            ('cite', 13, 18),
            ('frac', 28, 33)        # Position adjusted for actual parsing
        ]
    }
]

FIND_COMMAND_LATEX_CORNER_CASES = [
    {
        'description': 'Find command followed by digits (should not include digits)',
        'command_name': 'name',
        'content': r'\name123 text',
        'expected': [(0, 5)]
    },
    {
        'description': 'Find command followed by underscore (should not include underscore)',
        'command_name': 'test',
        'content': r'\test_helper',
        'expected': [(0, 5)]
    },
    {
        'description': 'Find ASCII command (Unicode not supported in LaTeX commands)',
        'command_name': 'na',
        'content': r'\été and \naïve',
        'expected': [(9, 12)]       # Only finds \na in \naïve
    },
    {
        'description': 'Find backslash command in multiple consecutive backslashes',
        'command_name': '\\',
        'content': r'\\\\text',
        'expected': [(0, 2), (2, 4)]
    },
    {
        'description': 'Find command at very end of content',
        'command_name': 'bye',
        'content': r'\end{document}\bye',
        'expected': [(14, 18)]
    }
]