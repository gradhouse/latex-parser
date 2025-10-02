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
            (r'\textbf', 0, 7),
            (r'\alpha', 15, 21),
            (r'\beta', 22, 27)
        ]
    },
    {
        'description': 'non-letter commands',
        'content': r'text \@ \! \# content',
        'expected': [
            (r'\@', 5, 7),
            (r'\!', 8, 10),
            (r'\#', 11, 13)
        ]
    },
    {
        'description': 'mixed commands',
        'content': r'\textbf \@ \alpha \!',
        'expected': [
            (r'\textbf', 0, 7),
            (r'\@', 8, 10),
            (r'\alpha', 11, 17),
            (r'\!', 18, 20)
        ]
    },
    {
        'description': 'commands with star forms',
        'content': r'\section{title} \section*{starred}',
        'expected': [
            (r'\section', 0, 8),
            (r'\section*', 16, 25)
        ]
    }
]

# Test cases for commands with @ symbol
FIND_ALL_COMMANDS_AT_SYMBOL_TESTS = [
    {
        'description': 'commands with @ as initial character',
        'content': r'\@chapter{title} \@section{content}',
        'expected': [
            (r'\@chapter', 0, 9),
            (r'\@section', 17, 26)
        ]
    },
    {
        'description': 'mixed @ usage - standalone and initial',
        'content': r'\@ \@section \alpha \!',
        'expected': [
            (r'\@', 0, 2),
            (r'\@section', 3, 12),
            (r'\alpha', 13, 19),
            (r'\!', 20, 22)
        ]
    }
]

# Test cases for whitespace handling
FIND_ALL_COMMANDS_WHITESPACE_TESTS = [
    {
        'description': 'commands with trailing spaces',
        'content': r'\alpha \beta  \gamma	\delta',
        'expected': [
            (r'\alpha', 0, 6),
            (r'\beta', 7, 12),
            (r'\gamma', 14, 20),
            (r'\delta', 21, 27)
        ]
    },
    {
        'description': 'commands with newlines',
        'content': r'\alpha' + '\n' + r'\beta' + '\n\n' + r'\gamma',
        'expected': [
            (r'\alpha', 0, 6),
            (r'\beta', 7, 12),
            (r'\gamma', 14, 20)
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
            (r'\textbf', 1, 8),  # \textbf (the \\ overlap is handled)
            (r'\textbf', 9, 16), # Second \textbf  
            (r'\\', 17, 19)     # Final \\ (double backslash command)
        ]
    }
]

# Test cases for find_command method
FIND_COMMAND_SPECIFIC_TESTS = [
    {
        'description': 'find specific letter command',
        'command_name': r'\textbf',
        'content': r'\textbf{hello} \textit{world} \textbf{again}',
        'expected': [
            (0, 7),   # First \textbf
            (30, 37)  # Second \textbf
        ]
    },
    {
        'description': 'find non-letter command',
        'command_name': r'\@',
        'content': r'text \@ more \! text \@ again',
        'expected': [
            (5, 7),   # First \@
            (21, 23)  # Second \@
        ]
    },
    {
        'description': 'find starred command',
        'command_name': r'\section*',
        'content': r'\section{title} \section*{starred} \section{normal}',
        'expected': [
            (16, 25)  # \section*
        ]
    },
    {
        'description': 'find regular command (not starred)',
        'command_name': r'\section',
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
        'command_name': r'\@',
        'content': r'\@ \@chapter \@section',
        'expected': [
            (0, 2)  # Only the standalone \@
        ]
    },
    {
        'description': 'find @chapter command',
        'command_name': r'\@chapter',
        'content': r'\@ \@chapter \@section',
        'expected': [
            (3, 12)  # \@chapter
        ]
    },
    {
        'description': 'find @section command',
        'command_name': r'\@section',
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
        'command_name': r'\text',
        'content': r'\text \textbf \textbold \textt',
        'expected': [
            (0, 5)  # Only \text, not \textbf or \textbold
        ]
    },
    {
        'description': 'case sensitivity',
        'command_name': r'\alpha',
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
            r'\documentclass', r'\usepackage', r'\begin', r'\section*', r'\textbf', 
            r'\textit', r'\frac', r'\cite', r'\ref', r'\end'
        ]
    }
]

# Error handling test cases
FIND_COMMANDS_ERROR_TESTS = [
    {
        'description': 'empty command name',
        'command_name': '',
        'content': r'\textbf{hello}',
        'should_raise': 'ValueError'  # Changed: empty command name should raise ValueError
    }
]

# Coverage completion test cases for missing lines
FIND_COMMAND_COVERAGE_TESTS = [
    {
        'description': 'Find single non-letter command $ (line 88 coverage)',
        'command_name': r'\$',
        'content': r'\$ and \& and \%',
        'expected': [(0, 2)]
    },
    {
        'description': 'Find @ command with star (line 96 coverage)',
        'command_name': r'\@name*',
        'content': r'\@name* text',
        'expected': [(0, 7)]
    },
    {
        'description': 'Find & command for non-letter end calculation (line 117 coverage)',
        'command_name': r'\&',
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
            (r'\command', 0, 8),      # \command (@ not part of name when not initial)
            (r'\test', 18, 23),       # \test (_ not part of command name)  
            (r'\name', 31, 36)        # \name (digits not part of command name)
        ]
    },
    {
        'description': 'Commands with Unicode characters (only ASCII letters supported)',
        'content': r'\été \naïve \résumé',
        'expected': [
            (r'\na', 5, 8),           # \na (ï not supported, so parses as \na + ïve)
            (r'\r', 12, 14)           # \r (é not supported, so parses as \r + ésumé)
        ]
    },
    {
        'description': 'Multiple consecutive backslashes',
        'content': r'\\\\text \\\\ \\newline',
        'expected': [
            (r'\\', 0, 2),           # First \\
            (r'\text', 3, 8),         # \text (space after second \\)
            (r'\\', 9, 11),          # Third \\
            (r'\\', 11, 13),         # Fourth \\
            (r'\newline', 15, 23)     # \newline (space after fifth \\)
        ]
    },
    {
        'description': 'Commands at end of content (no trailing space)',
        'content': r'\end{document}\bye',
        'expected': [
            (r'\end', 0, 4),
            (r'\bye', 14, 18)
        ]
    },
    {
        'description': 'Commands with immediate braces and brackets',
        'content': r'\textbf{bold}\cite[p.5]{ref}\frac{1}{2}',
        'expected': [
            (r'\textbf', 0, 7),
            (r'\cite', 13, 18),
            (r'\frac', 28, 33)        # Position adjusted for actual parsing
        ]
    }
]

FIND_COMMAND_LATEX_CORNER_CASES = [
    {
        'description': 'Find command followed by digits (should not include digits)',
        'command_name': r'\name',
        'content': r'\name123 text',
        'expected': [(0, 5)]
    },
    {
        'description': 'Find command followed by underscore (should not include underscore)',
        'command_name': r'\test',
        'content': r'\test_helper',
        'expected': [(0, 5)]
    },
    {
        'description': 'Find ASCII command (Unicode not supported in LaTeX commands)',
        'command_name': r'\na',
        'content': r'\été and \naïve',
        'expected': [(9, 12)]       # Only finds \na in \naïve
    },
    {
        'description': 'Find backslash command in multiple consecutive backslashes',
        'command_name': r'\\',
        'content': r'\\\\text',
        'expected': [(0, 2), (2, 4)]
    },
    {
        'description': 'Find command at very end of content',
        'command_name': r'\bye',
        'content': r'\end{document}\bye',
        'expected': [(14, 18)]
    }
]