# File: environment_test_cases.py
# Description: Test case data for Environment class methods
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

# Test cases for find_all_begin_environments
FIND_ALL_BEGIN_ENVIRONMENTS_BASIC_TESTS = [
    {
        'description': 'single environment',
        'content': r'\begin{equation}',
        'expected': [('equation', 0, 16)]
    },
    {
        'description': 'multiple different environments',
        'content': r'''\begin{equation}
E = mc^2
\end{equation}

\begin{align}
x &= y \\
z &= w
\end{align}

\begin{figure}
\caption{Test}
\end{figure}''',
        'expected': [('equation', 0, 16), ('align', 42, 55), ('figure', 86, 100)]
    },
    {
        'description': 'same environment multiple times',
        'content': r'''\begin{equation}
E = mc^2
\end{equation}

\begin{equation}
F = ma
\end{equation}''',
        'expected': [('equation', 0, 16), ('equation', 42, 58)]
    },
    {
        'description': 'environment with special characters',
        'content': r'''\begin{equation*}
\begin{align*}
\begin{figure_test}''',
        'expected': [('equation*', 0, 17), ('align*', 18, 32), ('figure_test', 33, 52)]
    }
]

FIND_ALL_BEGIN_ENVIRONMENTS_WHITESPACE_TESTS = [
    {
        'description': 'various whitespace patterns',
        'content': r'''\begin{equation}
\begin  {align}
\begin	{figure}
\begin
{table}
\begin { matrix }''',
        'expected': [('equation', 0, 16), ('align', 17, 32), ('figure', 33, 48), ('table', 49, 63), ('matrix', 64, 81)]
    }
]

FIND_ALL_BEGIN_ENVIRONMENTS_EDGE_CASE_TESTS = [
    {
        'description': 'empty content',
        'content': '',
        'expected': []
    },
    {
        'description': 'whitespace only content',
        'content': '   \n\n  ',
        'expected': []
    },
    {
        'description': 'no environments',
        'content': r'''This is just text with no environments.
Some math: $x = y$
And a command: \textbf{bold text}''',
        'expected': []
    },
    {
        'description': 'nested environments',
        'content': r'''\begin{figure}
  \begin{equation}
    E = mc^2
  \end{equation}
\end{figure}''',
        'expected': [('figure', 0, 14), ('equation', 17, 33)]
    }
]

# Test cases for find_all_end_environments
FIND_ALL_END_ENVIRONMENTS_BASIC_TESTS = [
    {
        'description': 'single end environment',
        'content': r'\end{equation}',
        'expected': [('equation', 0, 14)]
    },
    {
        'description': 'multiple different end environments',
        'content': r'''\end{equation}
\end{align}
\end{figure}''',
        'expected': [('equation', 0, 14), ('align', 15, 26), ('figure', 27, 39)]
    },
    {
        'description': 'various whitespace patterns in end environments',
        'content': r'''\end{equation}
\end  {align}
\end	{figure}
\end
{table}
\end { matrix }''',
        'expected': [('equation', 0, 14), ('align', 15, 28), ('figure', 29, 42), ('table', 43, 55), ('matrix', 56, 71)]
    }
]

# Test cases for find_begin_environment
FIND_BEGIN_ENVIRONMENT_BASIC_TESTS = [
    {
        'description': 'single match',
        'content': r'\begin{equation}',
        'environment_name': 'equation',
        'expected': [(0, 16)]
    },
    {
        'description': 'multiple matches same environment',
        'content': r'''\begin{equation}
E = mc^2
\end{equation}

\begin{equation}
F = ma
\end{equation}''',
        'environment_name': 'equation',
        'expected': [(0, 16), (42, 58)]
    },
    {
        'description': 'no matches',
        'content': r'''\begin{align}
x &= y
\end{align}''',
        'environment_name': 'equation',
        'expected': []
    },
    {
        'description': 'partial name no match',
        'content': r'\begin{equation*}',
        'environment_name': 'equation',
        'expected': []
    },
    {
        'description': 'special characters in name',
        'content': r'\begin{equation*}',
        'environment_name': 'equation*',
        'expected': [(0, 17)]
    }
]

FIND_BEGIN_ENVIRONMENT_WHITESPACE_TESTS = [
    {
        'description': 'whitespace variations',
        'content': r'''\begin{equation}
\begin  {equation}
\begin	{equation}
\begin
{equation}''',
        'environment_name': 'equation',
        'expected': [(0, 16), (17, 35), (36, 53), (54, 71)]
    }
]

FIND_BEGIN_ENVIRONMENT_EDGE_CASE_TESTS = [
    {
        'description': 'empty content',
        'content': '',
        'environment_name': 'equation',
        'expected': []
    },
    {
        'description': 'mixed environments find specific',
        'content': r'''\begin{figure}
\begin{equation}
\begin{align}
\begin{equation}
\begin{table}''',
        'environment_name': 'equation',
        'expected': [(15, 31), (46, 62)]
    }
]

# Test cases for find_end_environment
FIND_END_ENVIRONMENT_BASIC_TESTS = [
    {
        'description': 'single match',
        'content': r'\end{equation}',
        'environment_name': 'equation',
        'expected': [(0, 14)]
    },
    {
        'description': 'multiple matches same environment',
        'content': r'''\end{equation}
\end{equation}''',
        'environment_name': 'equation',
        'expected': [(0, 14), (15, 29)]
    },
    {
        'description': 'no matches',
        'content': r'\end{align}',
        'environment_name': 'equation',
        'expected': []
    },
    {
        'description': 'special characters in name',
        'content': r'\end{equation*}',
        'environment_name': 'equation*',
        'expected': [(0, 15)]
    }
]

FIND_END_ENVIRONMENT_WHITESPACE_TESTS = [
    {
        'description': 'whitespace variations',
        'content': r'''\end{equation}
\end  {equation}
\end	{equation}
\end
{equation}''',
        'environment_name': 'equation',
        'expected': [(0, 14), (15, 31), (32, 47), (48, 63)]
    }
]

# Integration test cases
INTEGRATION_TESTS = [
    {
        'description': 'complete environment matching',
        'content': r'''\begin{equation}
E = mc^2
\end{equation}

\begin{align}
x &= y \\
z &= w
\end{align}''',
        'expected_begins': [('equation', 0, 16), ('align', 42, 55)],
        'expected_ends': [('equation', 26, 40), ('align', 73, 84)]
    },
    {
        'description': 'mismatched environments',
        'content': r'''\begin{equation}
E = mc^2
\end{align}''',
        'expected_begins': [('equation', 0, 16)],
        'expected_ends': [('align', 26, 37)]
    },
    {
        'description': 'realistic latex document',
        'content': r'''\documentclass{article}
\usepackage{amsmath}

\begin{document}

\section{Introduction}
This is some text.

\begin{equation}
E = mc^2
\end{equation}

More text here.

\begin{align}
x &= a + b \\
y &= c + d
\end{align}

\begin{figure}
\centering
\caption{A figure}
\label{fig:test}
\end{figure}

\end{document}''',
        'expected_begins': [('document', 46, 62), ('equation', 107, 123), ('align', 166, 179), ('figure', 218, 232)],
        'expected_ends': [('equation', 133, 147), ('align', 205, 216), ('figure', 280, 292), ('document', 294, 308)]
    }
]

# Invalid input test cases
INVALID_INPUT_TESTS = [
    {
        'description': 'none content find_all_begin',
        'content': None,
        'expected': []
    },
    {
        'description': 'non-string content find_all_begin',
        'content': 123,
        'expected': []
    },
    {
        'description': 'list content find_all_begin',
        'content': [],
        'expected': []
    }
]

# Test cases for star environments
FIND_ALL_BEGIN_ENVIRONMENTS_STAR_TESTS = [
    {
        'description': 'star environments',
        'content': r'''\begin{equation*}
\begin{align*}
\begin{figure*}
\begin{table*}''',
        'expected': [('equation*', 0, 17), ('align*', 18, 32), ('figure*', 33, 48), ('table*', 49, 63)]
    },
    {
        'description': 'mixed star and non-star environments',
        'content': r'''\begin{equation}
\begin{equation*}
\begin{align}
\begin{align*}''',
        'expected': [('equation', 0, 16), ('equation*', 17, 34), ('align', 35, 48), ('align*', 49, 63)]
    }
]

FIND_ALL_END_ENVIRONMENTS_STAR_TESTS = [
    {
        'description': 'star end environments',
        'content': r'''\end{equation*}
\end{align*}
\end{figure*}''',
        'expected': [('equation*', 0, 15), ('align*', 16, 28), ('figure*', 29, 42)]
    }
]

FIND_BEGIN_ENVIRONMENT_STAR_TESTS = [
    {
        'description': 'find specific star environment',
        'content': r'''\begin{equation}
\begin{equation*}
\begin{align*}''',
        'environment_name': 'equation*',
        'expected': [(17, 34)]
    },
    {
        'description': 'no match for star when looking for non-star',
        'content': r'\begin{equation*}',
        'environment_name': 'equation',
        'expected': []
    }
]

FIND_END_ENVIRONMENT_STAR_TESTS = [
    {
        'description': 'find specific star end environment',
        'content': r'''\end{equation}
\end{equation*}
\end{align*}''',
        'environment_name': 'equation*',
        'expected': [(15, 30)]
    }
]