# File: def_command_test_cases.py
# Description: Test case fixtures for TeX \def command parsing
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

# Basic \def command parsing test cases
DEF_COMMAND_BASIC_TESTS = [
    {
        'description': 'Basic def command without parameters',
        'content': r'\def\mycommand{Hello World}',
        'start_pos': 0,
        'end_pos': 4,
        'expected': {
            'command_name': '\\def',
            'complete_start': 0,
            'complete_end': 27,
            'arguments': {
                'pattern': {
                    'value': r'\mycommand',
                    'start': 4,
                    'end': 14,
                    'type': 'def_pattern',
                    'parameters': [],
                    'delimiters': [{'text': r'\mycommand', 'before_param': None}]
                },
                'replacement': {
                    'value': 'Hello World',
                    'start': 14,
                    'end': 27,
                    'type': 'def_replacement'
                }
            }
        }
    },
    {
        'description': 'Def command with single parameter',
        'content': r'\def\mycommand#1{Hello #1}',
        'start_pos': 0,
        'end_pos': 4,
        'expected': {
            'arguments': {
                'pattern': {
                    'value': r'\mycommand#1',
                    'parameters': [{'number': 1, 'position': 10, 'text': '#1'}],
                    'delimiters': [{'text': r'\mycommand', 'before_param': 1}]
                },
                'replacement': {
                    'value': 'Hello #1'
                }
            }
        }
    },
    {
        'description': 'Def command with multiple parameters',
        'content': r'\def\mycommand#1#2{#1 and #2}',
        'start_pos': 0,
        'end_pos': 4,
        'expected': {
            'arguments': {
                'pattern': {
                    'value': r'\mycommand#1#2',
                    'parameters': [
                        {'number': 1, 'position': 10, 'text': '#1'},
                        {'number': 2, 'position': 12, 'text': '#2'}
                    ],
                    'delimiters': [{'text': r'\mycommand', 'before_param': 1}]
                },
                'replacement': {
                    'value': '#1 and #2'
                }
            }
        }
    },
    {
        'description': 'Def command with delimited parameter',
        'content': r'\def\mycommand#1 stop{Hello #1}',
        'start_pos': 0,
        'end_pos': 4,
        'expected': {
            'arguments': {
                'pattern': {
                    'value': r'\mycommand#1 stop',
                    'parameters': [{'number': 1, 'position': 10, 'text': '#1'}],
                    'delimiters': [
                        {'text': r'\mycommand', 'before_param': 1},
                        {'text': 'stop', 'after_last_param': True}
                    ]
                },
                'replacement': {
                    'value': 'Hello #1'
                }
            }
        }
    }
]

# Complex \def command pattern tests
DEF_COMMAND_COMPLEX_TESTS = [
    {
        'description': 'Complex pattern with multiple parameters and delimiters',
        'content': r'\def\mycommand#1[#2]#3{replacement}',
        'start_pos': 0,
        'end_pos': 4,
        'expected': {
            'arguments': {
                'pattern': {
                    'value': r'\mycommand#1[#2]#3',
                    'parameters': [
                        {'number': 1, 'position': 10, 'text': '#1'},
                        {'number': 2, 'position': 13, 'text': '#2'},
                        {'number': 3, 'position': 16, 'text': '#3'}
                    ],
                    'delimiters': [
                        {'text': r'\mycommand', 'before_param': 1},
                        {'text': '[', 'before_param': 2},
                        {'text': ']', 'before_param': 3}
                    ]
                },
                'replacement': {
                    'value': 'replacement'
                }
            }
        }
    },
    {
        'description': 'Pattern with text after last parameter',
        'content': r'\def\cmd#1end{replacement}',
        'start_pos': 0,
        'end_pos': 4,
        'expected': {
            'arguments': {
                'pattern': {
                    'value': r'\cmd#1end',
                    'parameters': [{'number': 1, 'position': 4, 'text': '#1'}],
                    'delimiters': [
                        {'text': r'\cmd', 'before_param': 1},
                        {'text': 'end', 'after_last_param': True}
                    ]
                },
                'replacement': {
                    'value': 'replacement'
                }
            }
        }
    }
]

# Edge case tests for \def commands
DEF_COMMAND_EDGE_TESTS = [
    {
        'description': 'Def command with whitespace after \\def',
        'content': r'\def  \mycommand{replacement}',
        'start_pos': 0,
        'end_pos': 4,
        'expected': {
            'arguments': {
                'pattern': {
                    'value': r'\mycommand'
                },
                'replacement': {
                    'value': 'replacement'
                }
            }
        }
    },
    {
        'description': 'Def command with nested braces in replacement',
        'content': r'\def\mycommand{nested{deeper}}',
        'start_pos': 0,
        'end_pos': 4,
        'expected': {
            'arguments': {
                'pattern': {
                    'value': r'\mycommand'
                },
                'replacement': {
                    'value': 'nested{deeper}'
                }
            }
        }
    },
    {
        'description': 'Def command with empty replacement',
        'content': r'\def\empty{}',
        'start_pos': 0,
        'end_pos': 4,
        'expected': {
            'arguments': {
                'pattern': {
                    'value': r'\empty'
                },
                'replacement': {
                    'value': ''
                }
            }
        }
    },
    {
        'description': 'Empty pattern (whitespace only)',
        'content': r'\def   {replacement}',
        'start_pos': 0,
        'end_pos': 4,
        'expected': {
            'arguments': {
                'pattern': {
                    'value': '',  # The pattern is stripped, so whitespace becomes empty string
                    'parameters': [],
                    'delimiters': []
                },
                'replacement': {
                    'value': 'replacement'
                }
            }
        }
    }
]

# Error case tests for \def commands
DEF_COMMAND_ERROR_TESTS = [
    {
        'description': 'Def command with missing replacement braces',
        'content': r'\def\mycommand',
        'start_pos': 0,
        'end_pos': 4,
        'expected': None
    },
    {
        'description': 'Def command with unclosed replacement',
        'content': r'\def\mycommand{unclosed',
        'start_pos': 0,
        'end_pos': 4,
        'expected': None
    },
    {
        'description': 'Def command with content ending at def',
        'content': r'\def',
        'start_pos': 0,
        'end_pos': 4,
        'expected': None
    },
    {
        'description': 'Def command with only whitespace after def',
        'content': r'\def   ',
        'start_pos': 0,
        'end_pos': 4,
        'expected': None
    }
]

# Integration test cases
DEF_COMMAND_INTEGRATION_TESTS = [
    {
        'description': 'Integration with parse_command_arguments',
        'content': r'\def\mycommand#1{Hello #1}',
        'command_name': r'\def',
        'start_pos': 0,
        'end_pos': 4,
        'syntax': r'\def⟨pattern⟩{⟨replacement⟩}',
        'expected': {
            'arguments': {
                'pattern': {
                    'value': r'\mycommand#1'
                },
                'replacement': {
                    'value': 'Hello #1'
                }
            }
        }
    }
]

# Special handling test cases
DEF_COMMAND_SPECIAL_TESTS = [
    {
        'description': 'Special handling in parse_arguments',
        'content': r'\def\mycommand{replacement text}',
        'command_name': r'\def',
        'start_pos': 0,
        'end_pos': 4,
        'syntax': r'\def⟨pattern⟩{⟨replacement⟩}',
        'is_environment': False,
        'expected': {
            'arguments': {
                'pattern': {
                    'value': r'\mycommand'
                },
                'replacement': {
                    'value': 'replacement text'
                }
            }
        }
    }
]

# Modernize def commands - basic conversion tests
MODERNIZE_DEF_COMMANDS_BASIC_TESTS = [
    {
        'description': 'Simple def without parameters',
        'input': r'\def\mycommand{Hello World}',
        'is_strict': False,
        'expected': r'\newcommand{\mycommand}{Hello World}',
        'should_raise': False
    },
    {
        'description': 'Def with single parameter',
        'input': r'\def\greet#1{Hello #1}',
        'is_strict': False,
        'expected': r'\newcommand{\greet}[1]{Hello #1}',
        'should_raise': False
    },
    {
        'description': 'Def with two parameters',
        'input': r'\def\combine#1#2{#1 and #2}',
        'is_strict': False,
        'expected': r'\newcommand{\combine}[2]{#1 and #2}',
        'should_raise': False
    },
    {
        'description': 'Def with three parameters',
        'input': r'\def\triple#1#2#3{First: #1, Second: #2, Third: #3}',
        'is_strict': False,
        'expected': r'\newcommand{\triple}[3]{First: #1, Second: #2, Third: #3}',
        'should_raise': False
    },
    {
        'description': 'Multiple simple def commands',
        'input': r'\def\first{One}\def\second{Two}\def\third{Three}',
        'is_strict': False,
        'expected': r'\newcommand{\first}{One}\newcommand{\second}{Two}\newcommand{\third}{Three}',
        'should_raise': False
    },
    {
        'description': 'Mixed simple and parameter def commands',
        'input': r'\def\simple{text}\def\param#1{Hello #1}',
        'is_strict': False,
        'expected': r'\newcommand{\simple}{text}\newcommand{\param}[1]{Hello #1}',
        'should_raise': False
    }
]

# Modernize def commands - non-convertible tests (normal mode)
MODERNIZE_DEF_COMMANDS_SKIP_TESTS = [
    {
        'description': 'Delimited parameter should be skipped',
        'input': r'\def\delimited#1 stop{Hello #1}',
        'is_strict': False,
        'expected': r'\def\delimited#1 stop{Hello #1}',  # Unchanged
        'should_raise': False
    },
    {
        'description': 'Non-sequential parameters should be skipped',
        'input': r'\def\nonseq#1#3{#1 and #3}',
        'is_strict': False,
        'expected': r'\def\nonseq#1#3{#1 and #3}',  # Unchanged
        'should_raise': False
    },
    {
        'description': 'Complex pattern with delimiters should be skipped',
        'input': r'\def\complex#1[#2]#3{Complex #1 #2 #3}',
        'is_strict': False,
        'expected': r'\def\complex#1[#2]#3{Complex #1 #2 #3}',  # Unchanged
        'should_raise': False
    },
    {
        'description': 'Mixed convertible and non-convertible',
        'input': r'\def\simple{text}\def\delimited#1 stop{Hello #1}\def\normal#1{Hi #1}',
        'is_strict': False,
        'expected': r'\newcommand{\simple}{text}\def\delimited#1 stop{Hello #1}\newcommand{\normal}[1]{Hi #1}',
        'should_raise': False
    }
]

# Modernize def commands - strict mode failure tests
MODERNIZE_DEF_COMMANDS_STRICT_TESTS = [
    {
        'description': 'Delimited parameter in strict mode should raise',
        'input': r'\def\delimited#1 stop{Hello #1}',
        'is_strict': True,
        'expected': None,
        'should_raise': True,
        'exception_type': ValueError,
        'exception_message': 'Contains delimited parameters'
    },
    {
        'description': 'Non-sequential parameters in strict mode should raise',
        'input': r'\def\nonseq#1#3{#1 and #3}',
        'is_strict': True,
        'expected': None,
        'should_raise': True,
        'exception_type': ValueError,
        'exception_message': 'Non-sequential parameters'
    },
    {
        'description': 'Complex pattern in strict mode should raise',
        'input': r'\def\complex#1[#2]#3{Complex #1 #2 #3}',
        'is_strict': True,
        'expected': None,
        'should_raise': True,
        'exception_type': ValueError,
        'exception_message': 'Contains delimited parameters'
    },
    {
        'description': 'Convertible commands should work in strict mode',
        'input': r'\def\simple{text}\def\param#1{Hello #1}',
        'is_strict': True,
        'expected': r'\newcommand{\simple}{text}\newcommand{\param}[1]{Hello #1}',
        'should_raise': False
    }
]

# Modernize def commands - edge case tests
MODERNIZE_DEF_COMMANDS_EDGE_TESTS = [
    {
        'description': 'Empty content',
        'input': '',
        'is_strict': False,
        'expected': '',
        'should_raise': False
    },
    {
        'description': 'No def commands',
        'input': r'\textbf{hello} \emph{world}',
        'is_strict': False,
        'expected': r'\textbf{hello} \emph{world}',
        'should_raise': False
    },
    {
        'description': 'Def with nested braces',
        'input': r'\def\nested{text with {nested} braces}',
        'is_strict': False,
        'expected': r'\newcommand{\nested}{text with {nested} braces}',
        'should_raise': False
    },
    {
        'description': 'Def with empty replacement',
        'input': r'\def\empty{}',
        'is_strict': False,
        'expected': r'\newcommand{\empty}{}',
        'should_raise': False
    },
    {
        'description': 'Def with whitespace after command',
        'input': r'\def  \spaced{content}',
        'is_strict': False,
        'expected': r'\newcommand{\spaced}{content}',
        'should_raise': False
    }
]

# Modernize def commands - coverage completion tests
MODERNIZE_DEF_COMMANDS_COVERAGE_TESTS = [
    {
        'description': 'Multiple parameters with complex replacement',
        'input': r'\def\formula#1#2#3{The result of #1 + #2 * #3 is calculated}',
        'is_strict': False,
        'expected': r'\newcommand{\formula}[3]{The result of #1 + #2 * #3 is calculated}',
        'should_raise': False
    },
    {
        'description': 'Def commands within LaTeX document',
        'input': r'\documentclass{article}\def\myauthor{John Doe}\def\mytitle#1{Title: #1}\begin{document}\end{document}',
        'is_strict': False,
        'expected': r'\documentclass{article}\newcommand{\myauthor}{John Doe}\newcommand{\mytitle}[1]{Title: #1}\begin{document}\end{document}',
        'should_raise': False
    },
    {
        'description': 'Mixed def commands with different patterns',
        'input': r'\def\a{A}\def\b#1{B:#1}\def\c#1#2{C:#1,#2}\def\d#1 end{D:#1}',
        'is_strict': False,
        'expected': r'\newcommand{\a}{A}\newcommand{\b}[1]{B:#1}\newcommand{\c}[2]{C:#1,#2}\def\d#1 end{D:#1}',
        'should_raise': False
    }
]

# Additional edge cases for complete coverage
MODERNIZE_DEF_COMMANDS_EDGE_COVERAGE_TESTS = [
    {
        'description': 'Pattern with space in command name (should fail extraction)',
        'input': r'\def\my command{text}',
        'is_strict': False,
        'expected': r'\def\my command{text}',  # Should remain unchanged
        'should_raise': False
    },
    {
        'description': 'Pattern not starting with backslash (should fail extraction)',
        'input': r'\def mycommand{text}',
        'is_strict': False,
        'expected': r'\def mycommand{text}',  # Should remain unchanged
        'should_raise': False
    },
    {
        'description': 'Empty pattern edge case',
        'input': r'\def {text}',
        'is_strict': False,
        'expected': r'\def {text}',  # Should remain unchanged
        'should_raise': False
    },
    {
        'description': 'Pattern with space and parameters (should fail)',
        'input': r'\def\my command#1{text}',
        'is_strict': False,
        'expected': r'\def\my command#1{text}',  # Should remain unchanged
        'should_raise': False
    }
]