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