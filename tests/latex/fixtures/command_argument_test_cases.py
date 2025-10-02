# File: command_argument_test_cases.py
# Description: Test fixtures for LaTeX command argument parsing
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

# Test cases for parse_syntax_arguments method
PARSE_SYNTAX_ARGUMENTS_TESTS = [
    {
        'description': 'Command with no arguments',
        'syntax': r'\textbf',
        'command_name': 'textbf',
        'is_environment': False,
        'expected': []
    },
    {
        'description': 'Command with one required argument',
        'syntax': r'\textbf{text}',
        'command_name': 'textbf',
        'is_environment': False,
        'expected': [
            {'type': 'required', 'name': 'text', 'position': 0}
        ]
    },
    {
        'description': 'Command with one optional argument',
        'syntax': r'\section[short]{title}',
        'command_name': 'section',
        'is_environment': False,
        'expected': [
            {'type': 'optional', 'name': 'short', 'position': 0},
            {'type': 'required', 'name': 'title', 'position': 7}
        ]
    },
    {
        'description': 'Command with multiple arguments',
        'syntax': r'\includegraphics[width=0.5\textwidth]{filename}',
        'command_name': 'includegraphics',
        'is_environment': False,
        'expected': [
            {'type': 'optional', 'name': 'width=0.5\\textwidth', 'position': 0},
            {'type': 'required', 'name': 'filename', 'position': 21}
        ]
    },
    {
        'description': 'Environment with no arguments',
        'syntax': r'\begin{document}',
        'command_name': 'document',
        'is_environment': True,
        'expected': []
    },
    {
        'description': 'Environment with arguments',
        'syntax': r'\begin{array}[pos]{cols}',
        'command_name': 'array',
        'is_environment': True,
        'expected': [
            {'type': 'optional', 'name': 'pos', 'position': 0},
            {'type': 'required', 'name': 'cols', 'position': 5}
        ]
    },
    {
        'description': 'Environment with multiple arguments',
        'syntax': r'\begin{tabular}[pos]{col_spec}',
        'command_name': 'tabular',
        'is_environment': True,
        'expected': [
            {'type': 'optional', 'name': 'pos', 'position': 0},
            {'type': 'required', 'name': 'col_spec', 'position': 5}
        ]
    }
]

# Test cases for syntax validation errors
PARSE_SYNTAX_ARGUMENTS_ERROR_TESTS = [
    {
        'description': 'Command syntax mismatch',
        'syntax': r'\textit{text}',
        'command_name': 'textbf',
        'is_environment': False,
        'expected_error': r"Syntax '\\textit\{text\}' doesn't match expected pattern for command 'textbf'"
    },
    {
        'description': 'Environment syntax mismatch',
        'syntax': r'\begin{itemize}',
        'command_name': 'enumerate',
        'is_environment': True,
        'expected_error': r"Syntax '\\begin\{itemize\}' doesn't match expected pattern for environment 'enumerate'"
    },
    {
        'description': 'Wrong prefix for command',
        'syntax': r'\begin{textbf}',
        'command_name': 'textbf',
        'is_environment': False,
        'expected_error': r"Syntax '\\begin\{textbf\}' doesn't match expected pattern for command 'textbf'"
    }
]

# Test cases for parse_command_arguments method
PARSE_COMMAND_ARGUMENTS_TESTS = [
    {
        'description': 'Command with no arguments',
        'content': r'\textbf and more text',
        'command_name': 'textbf',
        'command_start': 0,
        'command_end': 7,
        'syntax': r'\textbf',
        'expected': {
            'command_name': 'textbf',
            'complete_start': 0,
            'complete_end': 7,
            'arguments': {}
        }
    },
    {
        'description': 'Command with required argument',
        'content': r'\textbf{bold text} and more',
        'command_name': 'textbf',
        'command_start': 0,
        'command_end': 7,
        'syntax': r'\textbf{text}',
        'expected': {
            'command_name': 'textbf',
            'complete_start': 0,
            'complete_end': 18,
            'arguments': {
                'text': {
                    'value': 'bold text',
                    'start': 7,
                    'end': 18,
                    'type': 'required'
                }
            }
        }
    },
    {
        'description': 'Command with optional and required arguments',
        'content': r'\section[Short]{Long Title} text',
        'command_name': 'section',
        'command_start': 0,
        'command_end': 8,
        'syntax': r'\section[short]{title}',
        'expected': {
            'command_name': 'section',
            'complete_start': 0,
            'complete_end': 27,
            'arguments': {
                'short': {
                    'value': 'Short',
                    'start': 8,
                    'end': 15,
                    'type': 'optional'
                },
                'title': {
                    'value': 'Long Title',
                    'start': 15,
                    'end': 27,
                    'type': 'required'
                }
            }
        }
    },
    {
        'description': 'Command with skipped optional argument',
        'content': r'\section{Title Only} text',
        'command_name': 'section',
        'command_start': 0,
        'command_end': 8,
        'syntax': r'\section[short]{title}',
        'expected': {
            'command_name': 'section',
            'complete_start': 0,
            'complete_end': 20,
            'arguments': {
                'title': {
                    'value': 'Title Only',
                    'start': 8,
                    'end': 20,
                    'type': 'required'
                }
            }
        }
    },
    {
        'description': 'Command with whitespace between arguments',
        'content': r'\textcolor   [rgb] {red}   {colored text}',
        'command_name': 'textcolor',
        'command_start': 0,
        'command_end': 10,
        'syntax': r'\textcolor[model]{color}{text}',
        'expected': {
            'command_name': 'textcolor',
            'complete_start': 0,
            'complete_end': 41,
            'arguments': {
                'model': {
                    'value': 'rgb',
                    'start': 13,
                    'end': 18,
                    'type': 'optional'
                },
                'color': {
                    'value': 'red',
                    'start': 19,
                    'end': 24,
                    'type': 'required'
                },
                'text': {
                    'value': 'colored text',
                    'start': 27,
                    'end': 41,
                    'type': 'required'
                }
            }
        }
    }
]

# Test cases for helper methods
PARSE_BRACKET_ARGUMENT_TESTS = [
    {
        'description': 'Simple optional argument',
        'content': r'[option] text',
        'start_pos': 0,
        'expected': {
            'value': 'option',
            'start': 0,
            'end': 8
        }
    },
    {
        'description': 'Nested brackets',
        'content': r'[outer[inner]outer] text',
        'start_pos': 0,
        'expected': {
            'value': 'outer[inner]outer',
            'start': 0,
            'end': 19
        }
    },
    {
        'description': 'Empty optional argument',
        'content': r'[] text',
        'start_pos': 0,
        'expected': {
            'value': '',
            'start': 0,
            'end': 2
        }
    },
    {
        'description': 'Invalid start position',
        'content': r'[option] text',
        'start_pos': 1,
        'expected': None
    },
    {
        'description': 'No closing bracket',
        'content': r'[option text',
        'start_pos': 0,
        'expected': None
    }
]

PARSE_BRACE_ARGUMENT_TESTS = [
    {
        'description': 'Simple required argument',
        'content': r'{argument} text',
        'start_pos': 0,
        'expected': {
            'value': 'argument',
            'start': 0,
            'end': 10
        }
    },
    {
        'description': 'Nested braces',
        'content': r'{outer{inner}outer} text',
        'start_pos': 0,
        'expected': {
            'value': 'outer{inner}outer',
            'start': 0,
            'end': 19
        }
    },
    {
        'description': 'Empty required argument',
        'content': r'{} text',
        'start_pos': 0,
        'expected': {
            'value': '',
            'start': 0,
            'end': 2
        }
    },
    {
        'description': 'Invalid start position',
        'content': r'{argument} text',
        'start_pos': 1,
        'expected': None
    },
    {
        'description': 'No closing brace',
        'content': r'{argument text',
        'start_pos': 0,
        'expected': None
    }
]

# Edge cases and error handling
PARSE_ARGUMENTS_ERROR_TESTS = [
    {
        'description': 'Missing required argument',
        'content': r'\textbf and more text',
        'command_name': 'textbf',
        'command_start': 0,
        'command_end': 7,
        'syntax': r'\textbf{text}',
        'expected': {
            'command_name': 'textbf',
            'complete_start': 0,
            'complete_end': 7,
            'arguments': {}
        }
    },
    {
        'description': 'Incomplete required argument',
        'content': r'\textbf{incomplete',
        'command_name': 'textbf',
        'command_start': 0,
        'command_end': 7,
        'syntax': r'\textbf{text}',
        'expected': {
            'command_name': 'textbf',
            'complete_start': 0,
            'complete_end': 7,
            'arguments': {}
        }
    }
]

# Complex nested argument cases
PARSE_ARGUMENTS_COMPLEX_TESTS = [
    {
        'description': 'Command with complex nested arguments',
        'content': r'\newcommand{\mycmd}[2][default]{#1 and #2}',
        'command_name': 'newcommand',
        'command_start': 0,
        'command_end': 11,
        'syntax': r'\newcommand{name}[args][default]{definition}',
        'expected': {
            'command_name': 'newcommand',
            'complete_start': 0,
            'complete_end': 42,
            'arguments': {
                'name': {
                    'value': '\\mycmd',
                    'start': 11,
                    'end': 19,
                    'type': 'required'
                },
                'args': {
                    'value': '2',
                    'start': 19,
                    'end': 22,
                    'type': 'optional'
                },
                'default': {
                    'value': 'default',
                    'start': 22,
                    'end': 31,
                    'type': 'optional'
                },
                'definition': {
                    'value': '#1 and #2',
                    'start': 31,
                    'end': 42,
                    'type': 'required'
                }
            }
        }
    }
]