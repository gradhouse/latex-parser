# File: command_conversion_test_cases.py
# Description: Test case fixtures for command and environment definition conversion methods
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

# Test cases for _convert_command_definition_to_syntax method
COMMAND_CONVERSION_BASIC_TESTS = [
    {
        'description': 'Simple command without parameters',
        'input': {
            'arguments': {
                'cmd': {'value': '\\foo'},
                'definition': {'value': 'Hello World'}
            }
        },
        'expected': {
            'syntax': '\\foo',
            'implementation': 'Hello World',
            'default': None
        }
    },
    {
        'description': 'Command with single parameter',
        'input': {
            'arguments': {
                'cmd': {'value': '\\ps'},
                'nargs': {'value': '1'},
                'definition': {'value': '\\begin{center}\\leavevmode \\hbox{\\epsfxsize=2.5in\\epsfbox{#1}}\\end{center}'}
            }
        },
        'expected': {
            'syntax': '\\ps{#1}',
            'implementation': '\\begin{center}\\leavevmode \\hbox{\\epsfxsize=2.5in\\epsfbox{#1}}\\end{center}',
            'default': None
        }
    },
    {
        'description': 'Command with multiple parameters',
        'input': {
            'arguments': {
                'cmd': {'value': '\\mycommand'},
                'nargs': {'value': '3'},
                'definition': {'value': 'Text with #1, #2, and #3'}
            }
        },
        'expected': {
            'syntax': '\\mycommand{#1}{#2}{#3}',
            'implementation': 'Text with #1, #2, and #3',
            'default': None
        }
    },
    {
        'description': 'Command with optional parameter (default value)',
        'input': {
            'arguments': {
                'cmd': {'value': '\\greet'},
                'nargs': {'value': '2'},
                'default': {'value': 'World'},
                'definition': {'value': 'Hello #1, welcome #2'}
            }
        },
        'expected': {
            'syntax': '\\greet[#1]{#2}',
            'implementation': 'Hello #1, welcome #2',
            'default': 'World'
        }
    }
]

COMMAND_CONVERSION_EDGE_TESTS = [
    {
        'description': 'Command with zero arguments explicitly specified',
        'input': {
            'arguments': {
                'cmd': {'value': '\\simple'},
                'nargs': {'value': '0'},
                'definition': {'value': 'Simple text'}
            }
        },
        'expected': {
            'syntax': '\\simple',
            'implementation': 'Simple text',
            'default': None
        }
    },
    {
        'description': 'Command with maximum arguments (9)',
        'input': {
            'arguments': {
                'cmd': {'value': '\\maxargs'},
                'nargs': {'value': '9'},
                'definition': {'value': '#1#2#3#4#5#6#7#8#9'}
            }
        },
        'expected': {
            'syntax': '\\maxargs{#1}{#2}{#3}{#4}{#5}{#6}{#7}{#8}{#9}',
            'implementation': '#1#2#3#4#5#6#7#8#9',
            'default': None
        }
    },
    {
        'description': 'Command with complex implementation',
        'input': {
            'arguments': {
                'cmd': {'value': '\\complex'},
                'nargs': {'value': '2'},
                'definition': {'value': '\\begin{itemize}\\item \\textbf{#1}: \\emph{#2}\\end{itemize}'}
            }
        },
        'expected': {
            'syntax': '\\complex{#1}{#2}',
            'implementation': '\\begin{itemize}\\item \\textbf{#1}: \\emph{#2}\\end{itemize}',
            'default': None
        }
    }
]

COMMAND_CONVERSION_ERROR_TESTS = [
    {
        'description': 'Invalid input - not a dictionary',
        'input': "not a dict",
        'should_raise': ValueError,
        'expected_message': 'Command entry must be a dictionary'
    },
    {
        'description': 'Missing arguments field',
        'input': {'command_name': '\\newcommand'},
        'should_raise': ValueError,
        'expected_message': 'Command entry missing \'arguments\' field'
    },
    {
        'description': 'Missing cmd field',
        'input': {
            'arguments': {
                'definition': {'value': 'text'}
            }
        },
        'should_raise': ValueError,
        'expected_message': 'Command entry missing command name in arguments.cmd.value'
    },
    {
        'description': 'Command name without backslash',
        'input': {
            'arguments': {
                'cmd': {'value': 'foo'},
                'definition': {'value': 'text'}
            }
        },
        'should_raise': ValueError,
        'expected_message': 'Command name must start with backslash, got: foo'
    },
    {
        'description': 'Missing definition field',
        'input': {
            'arguments': {
                'cmd': {'value': '\\foo'}
            }
        },
        'should_raise': ValueError,
        'expected_message': 'Command entry missing definition in arguments.definition.value'
    },
    {
        'description': 'Invalid number of arguments - too many',
        'input': {
            'arguments': {
                'cmd': {'value': '\\foo'},
                'nargs': {'value': '10'},
                'definition': {'value': 'text'}
            }
        },
        'should_raise': ValueError,
        'expected_message': 'Number of arguments must be between 0 and 9, got: 10'
    },
    {
        'description': 'Invalid number of arguments - negative',
        'input': {
            'arguments': {
                'cmd': {'value': '\\foo'},
                'nargs': {'value': '-1'},
                'definition': {'value': 'text'}
            }
        },
        'should_raise': ValueError,
        'expected_message': 'Number of arguments must be between 0 and 9, got: -1'
    },
    {
        'description': 'Invalid number of arguments - not a number',
        'input': {
            'arguments': {
                'cmd': {'value': '\\foo'},
                'nargs': {'value': 'abc'},
                'definition': {'value': 'text'}
            }
        },
        'should_raise': ValueError,
        'expected_message': 'Invalid number of arguments: abc'
    }
]

# Test cases for _convert_environment_definition_to_syntax method
ENVIRONMENT_CONVERSION_BASIC_TESTS = [
    {
        'description': 'Simple environment without parameters',
        'input': {
            'arguments': {
                'name': {'value': 'myenv'},
                'begin_definition': {'value': '\\begin{center}'},
                'end_definition': {'value': '\\end{center}'}
            }
        },
        'expected': {
            'syntax': '\\begin{myenv}',
            'begin_implementation': '\\begin{center}',
            'end_implementation': '\\end{center}',
            'default': None
        }
    },
    {
        'description': 'Environment with single parameter',
        'input': {
            'arguments': {
                'name': {'value': 'myquote'},
                'nargs': {'value': '1'},
                'begin_definition': {'value': '\\begin{quote}\\textbf{#1}:'},
                'end_definition': {'value': '\\end{quote}'}
            }
        },
        'expected': {
            'syntax': '\\begin{myquote}{#1}',
            'begin_implementation': '\\begin{quote}\\textbf{#1}:',
            'end_implementation': '\\end{quote}',
            'default': None
        }
    },
    {
        'description': 'Environment with multiple parameters',
        'input': {
            'arguments': {
                'name': {'value': 'custombox'},
                'nargs': {'value': '3'},
                'begin_definition': {'value': '\\begin{#1}\\section{#2}\\label{#3}'},
                'end_definition': {'value': '\\end{#1}'}
            }
        },
        'expected': {
            'syntax': '\\begin{custombox}{#1}{#2}{#3}',
            'begin_implementation': '\\begin{#1}\\section{#2}\\label{#3}',
            'end_implementation': '\\end{#1}',
            'default': None
        }
    },
    {
        'description': 'Environment with optional parameter (default value)',
        'input': {
            'arguments': {
                'name': {'value': 'myframe'},
                'nargs': {'value': '2'},
                'default': {'value': 'black'},
                'begin_definition': {'value': '\\begin{frame}[#1]\\title{#2}'},
                'end_definition': {'value': '\\end{frame}'}
            }
        },
        'expected': {
            'syntax': '\\begin{myframe}[#1]{#2}',
            'begin_implementation': '\\begin{frame}[#1]\\title{#2}',
            'end_implementation': '\\end{frame}',
            'default': 'black'
        }
    }
]

ENVIRONMENT_CONVERSION_EDGE_TESTS = [
    {
        'description': 'Environment with zero arguments explicitly specified',
        'input': {
            'arguments': {
                'name': {'value': 'simple'},
                'nargs': {'value': '0'},
                'begin_definition': {'value': '\\begin{itemize}'},
                'end_definition': {'value': '\\end{itemize}'}
            }
        },
        'expected': {
            'syntax': '\\begin{simple}',
            'begin_implementation': '\\begin{itemize}',
            'end_implementation': '\\end{itemize}',
            'default': None
        }
    },
    {
        'description': 'Environment with maximum arguments (9)',
        'input': {
            'arguments': {
                'name': {'value': 'maxargs'},
                'nargs': {'value': '9'},
                'begin_definition': {'value': 'Begin: #1#2#3#4#5#6#7#8#9'},
                'end_definition': {'value': 'End: #9#8#7#6#5#4#3#2#1'}
            }
        },
        'expected': {
            'syntax': '\\begin{maxargs}{#1}{#2}{#3}{#4}{#5}{#6}{#7}{#8}{#9}',
            'begin_implementation': 'Begin: #1#2#3#4#5#6#7#8#9',
            'end_implementation': 'End: #9#8#7#6#5#4#3#2#1',
            'default': None
        }
    },
    {
        'description': 'Environment with complex begin/end implementations',
        'input': {
            'arguments': {
                'name': {'value': 'complex'},
                'nargs': {'value': '2'},
                'begin_definition': {'value': '\\begin{minipage}{\\textwidth}\\section{#1}\\textbf{#2}'},
                'end_definition': {'value': '\\end{minipage}\\newpage'}
            }
        },
        'expected': {
            'syntax': '\\begin{complex}{#1}{#2}',
            'begin_implementation': '\\begin{minipage}{\\textwidth}\\section{#1}\\textbf{#2}',
            'end_implementation': '\\end{minipage}\\newpage',
            'default': None
        }
    }
]

ENVIRONMENT_CONVERSION_ERROR_TESTS = [
    {
        'description': 'Invalid input - not a dictionary',
        'input': "not a dict",
        'should_raise': ValueError,
        'expected_message': 'Environment entry must be a dictionary'
    },
    {
        'description': 'Missing arguments field',
        'input': {'command_name': '\\newenvironment'},
        'should_raise': ValueError,
        'expected_message': 'Environment entry missing \'arguments\' field'
    },
    {
        'description': 'Missing name field',
        'input': {
            'arguments': {
                'begin_definition': {'value': 'begin'},
                'end_definition': {'value': 'end'}
            }
        },
        'should_raise': ValueError,
        'expected_message': 'Environment entry missing environment name in arguments.name.value'
    },
    {
        'description': 'Missing begin_definition field',
        'input': {
            'arguments': {
                'name': {'value': 'myenv'},
                'end_definition': {'value': 'end'}
            }
        },
        'should_raise': ValueError,
        'expected_message': 'Environment entry missing begin definition in arguments.begin_definition.value'
    },
    {
        'description': 'Missing end_definition field',
        'input': {
            'arguments': {
                'name': {'value': 'myenv'},
                'begin_definition': {'value': 'begin'}
            }
        },
        'should_raise': ValueError,
        'expected_message': 'Environment entry missing end definition in arguments.end_definition.value'
    },
    {
        'description': 'Invalid number of arguments - too many',
        'input': {
            'arguments': {
                'name': {'value': 'myenv'},
                'nargs': {'value': '10'},
                'begin_definition': {'value': 'begin'},
                'end_definition': {'value': 'end'}
            }
        },
        'should_raise': ValueError,
        'expected_message': 'Number of arguments must be between 0 and 9, got: 10'
    },
    {
        'description': 'Invalid number of arguments - negative',
        'input': {
            'arguments': {
                'name': {'value': 'myenv'},
                'nargs': {'value': '-1'},
                'begin_definition': {'value': 'begin'},
                'end_definition': {'value': 'end'}
            }
        },
        'should_raise': ValueError,
        'expected_message': 'Number of arguments must be between 0 and 9, got: -1'
    },
    {
        'description': 'Invalid number of arguments - not a number',
        'input': {
            'arguments': {
                'name': {'value': 'myenv'},
                'nargs': {'value': 'abc'},
                'begin_definition': {'value': 'begin'},
                'end_definition': {'value': 'end'}
            }
        },
        'should_raise': ValueError,
        'expected_message': 'Invalid number of arguments: abc'
    }
]