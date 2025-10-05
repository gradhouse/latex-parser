# File: document_analysis_test_cases.py
# Description: Test cases for document analysis methods (get_document_defined_commands and get_document_defined_environments)
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

"""
Test cases for LaTeX document analysis functionality including command and environment definitions.
"""

# Test cases for get_document_defined_commands method
DOCUMENT_DEFINED_COMMANDS_TESTS = [
    {
        'description': 'Empty content returns empty list',
        'content': '',
        'expected': []
    },
    {
        'description': 'No definitions returns empty list',
        'content': r'\textbf{hello} \section{title} \begin{document} text \end{document}',
        'expected': []
    },
    {
        'description': 'Single newcommand without arguments',
        'content': r'\newcommand{\mycommand}{Hello World}',
        'expected': [
            {
                'command_name': r'\mycommand',
                'definition_type': 'newcommand',
                'position': (0, 34),
                'arguments': {
                    'cmd': r'\mycommand',
                    'definition': 'Hello World'
                }
            }
        ]
    },
    {
        'description': 'Newcommand with arguments',
        'content': r'\newcommand{\mycommand}[2]{#1 and #2}',
        'expected': [
            {
                'command_name': r'\mycommand',
                'definition_type': 'newcommand',
                'position': (0, 35),
                'arguments': {
                    'cmd': r'\mycommand',
                    'nargs': '2',
                    'definition': '#1 and #2'
                }
            }
        ]
    },
    {
        'description': 'Newcommand with default argument',
        'content': r'\newcommand{\mycommand}[2][default]{#1 and #2}',
        'expected': [
            {
                'command_name': r'\mycommand',
                'definition_type': 'newcommand',
                'position': (0, 46),
                'arguments': {
                    'cmd': r'\mycommand',
                    'nargs': '2',
                    'default': 'default',
                    'definition': '#1 and #2'
                }
            }
        ]
    },
    {
        'description': 'All command definition types',
        'content': r'''
\newcommand{\cmdone}{first}
\renewcommand{\cmdtwo}{second}
\providecommand{\cmdthree}{third}
\DeclareRobustCommand{\cmdfour}{fourth}
\newcommand*{\cmdfive}{fifth}
\renewcommand*{\cmdsix}{sixth}
''',
        'expected': [
            {
                'command_name': r'\cmdone',
                'definition_type': 'newcommand',
                'position': (1, 28),
                'arguments': {'cmd': r'\cmdone', 'definition': 'first'}
            },
            {
                'command_name': r'\cmdtwo',
                'definition_type': 'renewcommand',
                'position': (29, 58),
                'arguments': {'cmd': r'\cmdtwo', 'definition': 'second'}
            },
            {
                'command_name': r'\cmdthree',
                'definition_type': 'providecommand',
                'position': (59, 90),
                'arguments': {'cmd': r'\cmdthree', 'definition': 'third'}
            },
            {
                'command_name': r'\cmdfour',
                'definition_type': 'DeclareRobustCommand',
                'position': (91, 128),
                'arguments': {'cmd': r'\cmdfour', 'definition': 'fourth'}
            },
            {
                'command_name': r'\cmdfive',
                'definition_type': 'newcommand*',
                'position': (129, 157),
                'arguments': {'cmd': r'\cmdfive', 'definition': 'fifth'}
            },
            {
                'command_name': r'\cmdsix',
                'definition_type': 'renewcommand*',
                'position': (158, 188),
                'arguments': {'cmd': r'\cmdsix', 'definition': 'sixth'}
            }
        ]
    },
    {
        'description': 'Commands sorted by position',
        'content': r'''
Some text before
\renewcommand{\late}{later}
More text
\newcommand{\early}{earlier}
Final text
''',
        'expected': [
            {
                'command_name': r'\late',
                'definition_type': 'renewcommand',
                'position': (18, 46),
                'arguments': {'cmd': r'\late', 'definition': 'later'}
            },
            {
                'command_name': r'\early',
                'definition_type': 'newcommand',
                'position': (57, 84),
                'arguments': {'cmd': r'\early', 'definition': 'earlier'}
            }
        ]
    },
    {
        'description': 'Complex nested definitions',
        'content': r'''
\newcommand{\complex}[3][def]{
    \textbf{#1}: \emph{#2} and \underline{#3}
    \newcommand{\inner}{nested}
}
\providecommand{\another}{simple}
''',
        'expected': [
            {
                'command_name': r'\complex',
                'definition_type': 'newcommand',
                'position': (1, 85),
                'arguments': {
                    'cmd': r'\complex',
                    'nargs': '3',
                    'default': 'def',
                    'definition': '\n    \\textbf{#1}: \\emph{#2} and \\underline{#3}\n    \\newcommand{\\inner}{nested}\n'
                }
            },
            {
                'command_name': r'\inner',
                'definition_type': 'newcommand',
                'position': (50, 76),
                'arguments': {'cmd': r'\inner', 'definition': 'nested'}
            },
            {
                'command_name': r'\another',
                'definition_type': 'providecommand',
                'position': (86, 118),
                'arguments': {'cmd': r'\another', 'definition': 'simple'}
            }
        ]
    },
    {
        'description': 'Mixed content with definitions',
        'content': r'''
\documentclass{article}
\usepackage{amsmath}

\newcommand{\mysum}[2]{\sum_{#1}^{#2}}

\begin{document}
\title{Test Document}
\author{Test Author}

\renewcommand{\thesection}{\Roman{section}}

Some text with \textbf{formatting}.

\newcommand{\myref}[1]{\ref{#1}}

\end{document}
''',
        'expected': [
            {
                'command_name': r'\mysum',
                'definition_type': 'newcommand',
                'position': (46, 82),
                'arguments': {
                    'cmd': r'\mysum',
                    'nargs': '2',
                    'definition': '\\sum_{#1}^{#2}'
                }
            },
            {
                'command_name': r'\thesection',
                'definition_type': 'renewcommand',
                'position': (140, 181),
                'arguments': {
                    'cmd': r'\thesection',
                    'definition': '\\Roman{section}'
                }
            },
            {
                'command_name': r'\myref',
                'definition_type': 'newcommand',
                'position': (229, 259),
                'arguments': {
                    'cmd': r'\myref',
                    'nargs': '1',
                    'definition': '\\ref{#1}'
                }
            }
        ]
    }
]

# Test cases for get_document_defined_environments method
DOCUMENT_DEFINED_ENVIRONMENTS_TESTS = [
    {
        'description': 'Empty content returns empty list',
        'content': '',
        'expected': []
    },
    {
        'description': 'No environment definitions returns empty list', 
        'content': r'\newcommand{\test}{hello} \begin{document} text \end{document}',
        'expected': []
    },
    {
        'description': 'Single newenvironment without arguments',
        'content': r'\newenvironment{myenv}{start}{end}',
        'expected': [
            {
                'environment_name': 'myenv',
                'definition_type': 'newenvironment',
                'position': (0, 34),
                'arguments': {
                    'name': 'myenv',
                    'begin': 'start',
                    'end': 'end'
                }
            }
        ]
    },
    {
        'description': 'Newenvironment with arguments',
        'content': r'\newenvironment{myenv}[2]{start #1 #2}{end}',
        'expected': [
            {
                'environment_name': 'myenv',
                'definition_type': 'newenvironment',
                'position': (0, 43),
                'arguments': {
                    'name': 'myenv',
                    'nargs': '2',
                    'begin': 'start #1 #2',
                    'end': 'end'
                }
            }
        ]
    },
    {
        'description': 'Newenvironment with default argument',
        'content': r'\newenvironment{myenv}[2][default]{start #1 #2}{end}',
        'expected': [
            {
                'environment_name': 'myenv',
                'definition_type': 'newenvironment',
                'position': (0, 52),
                'arguments': {
                    'name': 'myenv',
                    'nargs': '2', 
                    'default': 'default',
                    'begin': 'start #1 #2',
                    'end': 'end'
                }
            }
        ]
    },
    {
        'description': 'Both newenvironment and renewenvironment',
        'content': r'''
\newenvironment{envone}{begin1}{end1}
\renewenvironment{envtwo}{begin2}{end2}
''',
        'expected': [
            {
                'environment_name': 'envone',
                'definition_type': 'newenvironment',
                'position': (1, 38),
                'arguments': {
                    'name': 'envone',
                    'begin': 'begin1',
                    'end': 'end1'
                }
            },
            {
                'environment_name': 'envtwo',
                'definition_type': 'renewenvironment',
                'position': (39, 78),
                'arguments': {
                    'name': 'envtwo',
                    'begin': 'begin2',
                    'end': 'end2'
                }
            }
        ]
    },
    {
        'description': 'Mixed environment and command definitions',
        'content': r'''
\newcommand{\mycmd}{command}
\newenvironment{myenv}{start}{end}
\renewcommand{\anothercmd}{another}
\renewenvironment{anotherenv}{begin}{end}
''',
        'expected': [
            {
                'environment_name': 'myenv',
                'definition_type': 'newenvironment',
                'position': (30, 64),
                'arguments': {
                    'name': 'myenv',
                    'begin': 'start',
                    'end': 'end'
                }
            },
            {
                'environment_name': 'anotherenv',
                'definition_type': 'renewenvironment',
                'position': (98, 138),
                'arguments': {
                    'name': 'anotherenv',
                    'begin': 'begin',
                    'end': 'end'
                }
            }
        ]
    }
]