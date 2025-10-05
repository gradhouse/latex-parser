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
            'command_name': '\\foo',
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
            'command_name': '\\ps',
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
            'command_name': '\\mycommand',
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
            'command_name': '\\greet',
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
            'command_name': '\\simple',
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
            'command_name': '\\maxargs',
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
            'command_name': '\\complex',
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
# Test cases for _apply_command_definition method
COMMAND_APPLICATION_BASIC_TESTS = [
    {
        'description': 'Simple command without parameters',
        'command_definition': {
            'command_name': '\foo',
            'syntax': '\foo',
            'implementation': 'Hello World',
            'default': None
        },
        'parsed_arguments': {
            'command_name': '\foo',
            'complete_start': 0,
            'complete_end': 4,
            'arguments': {}
        },
        'expected': 'Hello World'
    },
    {
        'description': 'Command with single required parameter',
        'command_definition': {
            'command_name': '\\ps',
            'syntax': '\\ps{#1}',
            'implementation': '\\begin{center}\\epsfbox{#1}\\end{center}',
            'default': None
        },
        'parsed_arguments': {
            'command_name': '\\ps',
            'complete_start': 0,
            'complete_end': 15,
            'arguments': {
                '#1': {'value': 'figure.eps', 'type': 'required'}
            }
        },
        'expected': '\\begin{center}\\epsfbox{figure.eps}\\end{center}'
    },
    {
        'description': 'Command with optional parameter missing (use default)',
        'command_definition': {
            'command_name': '\\greet',
            'syntax': '\\greet[#1]{#2}',
            'implementation': 'Hello #1, welcome #2',
            'default': 'World'
        },
        'parsed_arguments': {
            'command_name': '\\greet',
            'complete_start': 0,
            'complete_end': 12,
            'arguments': {
                '#2': {'value': 'John', 'type': 'required'}
            }
        },
        'expected': 'Hello World, welcome John'
    }
]

COMMAND_APPLICATION_ERROR_TESTS = [
    {
        'description': 'Invalid command definition - not a dictionary',
        'command_definition': "not a dict",
        'parsed_arguments': {'arguments': {}},
        'should_raise': ValueError,
        'expected_message': 'Command definition must be a dictionary'
    },
    {
        'description': 'Insufficient arguments provided',
        'command_definition': {
            'command_name': '\test',
            'syntax': '\test{#1}{#2}',
            'implementation': '#1 and #2',
            'default': None
        },
        'parsed_arguments': {
            'command_name': '\\test',
            'arguments': {}
        },
        'should_raise': ValueError,
        'expected_message': 'No value available for parameter #1 in command'
    }
]

COMMAND_APPLICATION_EDGE_TESTS = [
    {
        'description': 'Command with complex implementation containing multiple instances of same parameter',
        'command_definition': {
            'command_name': '\\repeat',
            'syntax': '\\repeat{#1}',
            'implementation': '#1 and #1 again, plus more #1',
            'default': None
        },
        'parsed_arguments': {
            'command_name': '\\repeat',
            'complete_start': 0,
            'complete_end': 15,
            'arguments': {
                '#1': {'value': 'test', 'type': 'required'}
            }
        },
        'expected': 'test and test again, plus more test'
    },
    {
        'description': 'Command with maximum parameters (9)',
        'command_definition': {
            'command_name': '\\maxargs',
            'syntax': '\\maxargs{#1}{#2}{#3}{#4}{#5}{#6}{#7}{#8}{#9}',
            'implementation': '#1-#2-#3-#4-#5-#6-#7-#8-#9',
            'default': None
        },
        'parsed_arguments': {
            'command_name': '\\maxargs',
            'complete_start': 0,
            'complete_end': 50,
            'arguments': {
                '#1': {'value': '1', 'type': 'required'},
                '#2': {'value': '2', 'type': 'required'},
                '#3': {'value': '3', 'type': 'required'},
                '#4': {'value': '4', 'type': 'required'},
                '#5': {'value': '5', 'type': 'required'},
                '#6': {'value': '6', 'type': 'required'},
                '#7': {'value': '7', 'type': 'required'},
                '#8': {'value': '8', 'type': 'required'},
                '#9': {'value': '9', 'type': 'required'}
            }
        },
        'expected': '1-2-3-4-5-6-7-8-9'
    },
    {
        'description': 'Command with optional parameter provided',
        'command_definition': {
            'command_name': '\\greet',
            'syntax': '\\greet[#1]{#2}',
            'implementation': 'Hello #1, welcome #2',
            'default': 'World'
        },
        'parsed_arguments': {
            'command_name': '\\greet',
            'complete_start': 0,
            'complete_end': 18,
            'arguments': {
                '#1': {'value': 'Alice', 'type': 'optional'},
                '#2': {'value': 'John', 'type': 'required'}
            }
        },
        'expected': 'Hello Alice, welcome John'
    },
    {
        'description': 'Command with multiple parameters',
        'command_definition': {
            'command_name': '\\mycommand',
            'syntax': '\\mycommand{#1}{#2}{#3}',
            'implementation': 'Text with #1, #2, and #3',
            'default': None
        },
        'parsed_arguments': {
            'command_name': '\\mycommand',
            'complete_start': 0,
            'complete_end': 25,
            'arguments': {
                '#1': {'value': 'first', 'type': 'required'},
                '#2': {'value': 'second', 'type': 'required'},
                '#3': {'value': 'third', 'type': 'required'}
            }
        },
        'expected': 'Text with first, second, and third'
    }
]

COMMAND_APPLICATION_ADDITIONAL_ERROR_TESTS = [
    {
        'description': 'Invalid parsed arguments - not a dictionary',
        'command_definition': {'command_name': '\\test', 'syntax': '\\test', 'implementation': 'test'},
        'parsed_arguments': "not a dict",
        'should_raise': ValueError,
        'expected_message': 'Parsed arguments must be a dictionary'
    },
    {
        'description': 'Missing command_name in definition',
        'command_definition': {'syntax': '\\test', 'implementation': 'test'},
        'parsed_arguments': {'arguments': {}},
        'should_raise': ValueError,
        'expected_message': 'Command definition missing required field: command_name'
    },
    {
        'description': 'Missing syntax in definition',
        'command_definition': {'command_name': '\\test', 'implementation': 'test'},
        'parsed_arguments': {'arguments': {}},
        'should_raise': ValueError,
        'expected_message': 'Command definition missing required field: syntax'
    },
    {
        'description': 'Missing implementation in definition',
        'command_definition': {'command_name': '\\test', 'syntax': '\\test'},
        'parsed_arguments': {'arguments': {}},
        'should_raise': ValueError,
        'expected_message': 'Command definition missing required field: implementation'
    },
    {
        'description': 'Missing arguments field in parsed arguments',
        'command_definition': {'command_name': '\\test', 'syntax': '\\test', 'implementation': 'test'},
        'parsed_arguments': {'command_name': '\\test'},
        'should_raise': ValueError,
        'expected_message': 'Parsed arguments missing \'arguments\' field'
    },
    {
        'description': 'Command name is not a string (None)',
        'command_definition': {'command_name': None, 'syntax': '\\test', 'implementation': 'test'},
        'parsed_arguments': {'arguments': {}},
        'should_raise': ValueError,
        'expected_message': 'Command name must be a string'
    },
    {
        'description': 'Syntax is not a string (None)',
        'command_definition': {'command_name': '\\test', 'syntax': None, 'implementation': 'test'},
        'parsed_arguments': {'arguments': {}},
        'should_raise': ValueError,
        'expected_message': 'Syntax must be a string'
    },
    {
        'description': 'Implementation is not a string (None)',
        'command_definition': {'command_name': '\\test', 'syntax': '\\test', 'implementation': None},
        'parsed_arguments': {'arguments': {}},
        'should_raise': ValueError,
        'expected_message': 'Implementation must be a string'
    },
    {
        'description': 'Missing argument with no default available',
        'command_definition': {
            'command_name': '\\test',
            'syntax': '\\test{#1}{#2}',
            'implementation': '#1 and #2',
            'default': None
        },
        'parsed_arguments': {
            'command_name': '\\test',
            'arguments': {
                '#2': {'value': 'second', 'type': 'required'}
            }
        },
        'should_raise': ValueError,
        'expected_message': 'No value available for parameter #1 in command'
    },
    {
        'description': 'Too many arguments provided',
        'command_definition': {
            'command_name': '\\test',
            'syntax': '\\test{#1}',
            'implementation': '#1',
            'default': None
        },
        'parsed_arguments': {
            'command_name': '\\test',
            'arguments': {
                '#1': {'value': 'first', 'type': 'required'},
                '#2': {'value': 'second', 'type': 'required'}
            }
        },
        'should_raise': ValueError,
        'expected_message': 'Too many arguments provided. Expected 1, got 2'
    },
    {
        'description': 'Cannot use default value - no optional parameters found',
        'command_definition': {
            'command_name': '\\test',
            'syntax': '\\test{#1}{#2}',
            'implementation': '#1 and #2',
            'default': 'default_value'
        },
        'parsed_arguments': {
            'command_name': '\\test',
            'arguments': {
                '#2': {'value': 'second', 'type': 'required'}
            }
        },
        'should_raise': ValueError,
        'expected_message': 'No value available for parameter #1 in command'
    }
]

# Additional edge case tests for comprehensive coverage
COMMAND_APPLICATION_COVERAGE_TESTS = [
    {
        'description': 'Command with empty implementation',
        'command_definition': {
            'command_name': '\\empty',
            'syntax': '\\empty{#1}',
            'implementation': '',
            'default': None
        },
        'parsed_arguments': {
            'command_name': '\\empty',
            'complete_start': 0,
            'complete_end': 10,
            'arguments': {
                '#1': {'value': 'anything', 'type': 'required'}
            }
        },
        'expected': ''
    },
    {
        'description': 'Command with no parameters in syntax but with implementation',
        'command_definition': {
            'command_name': '\\simple',
            'syntax': '\\simple',
            'implementation': 'Just plain text with no parameters',
            'default': None
        },
        'parsed_arguments': {
            'command_name': '\\simple',
            'complete_start': 0,
            'complete_end': 7,
            'arguments': {}
        },
        'expected': 'Just plain text with no parameters'
    },
    {
        'description': 'Command with complex parameter pattern in syntax',
        'command_definition': {
            'command_name': '\\complex',
            'syntax': '\\complex[#1]{#2}[#3]',
            'implementation': 'First: #1, Second: #2, Third: #3',
            'default': None
        },
        'parsed_arguments': {
            'command_name': '\\complex',
            'complete_start': 0,
            'complete_end': 25,
            'arguments': {
                '#1': {'value': 'opt1', 'type': 'optional'},
                '#2': {'value': 'req1', 'type': 'required'},
                '#3': {'value': 'opt2', 'type': 'optional'}
            }
        },
        'expected': 'First: opt1, Second: req1, Third: opt2'
    },
    {
        'description': 'Command with parameters not in sequential order in syntax',
        'command_definition': {
            'command_name': '\\reorder',
            'syntax': '\\reorder{#2}[#1]{#3}',
            'implementation': 'First: #1, Second: #2, Third: #3',
            'default': None
        },
        'parsed_arguments': {
            'command_name': '\\reorder',
            'complete_start': 0,
            'complete_end': 25,
            'arguments': {
                '#1': {'value': 'first', 'type': 'optional'},
                '#2': {'value': 'second', 'type': 'required'},
                '#3': {'value': 'third', 'type': 'required'}
            }
        },
        'expected': 'First: first, Second: second, Third: third'
    }
]

# Specific tests to achieve 100% coverage of uncovered lines
COMMAND_APPLICATION_COVERAGE_SPECIFIC_TESTS = [
    {
        'description': 'Test parameter type detection - optional parameter in brackets (lines 1374-1377)',
        'command_definition': {
            'command_name': '\\testopt',
            'syntax': '\\testopt[#1]',  # This should trigger bracket detection logic
            'implementation': 'Optional: #1',
            'default': 'DefaultValue'
        },
        'parsed_arguments': {
            'command_name': '\\testopt',
            'complete_start': 0,
            'complete_end': 10,
            'arguments': {}  # Missing optional argument to trigger default usage (line 1434)
        },
        'expected': 'Optional: DefaultValue'
    },
    {
        'description': 'Test parameter type detection - parameter in brackets with closing bracket',
        'command_definition': {
            'command_name': '\\opttest',
            'syntax': '\\opttest[#1]{#2}',  # This has both optional and required
            'implementation': 'First: #1, Second: #2',
            'default': 'Default1'
        },
        'parsed_arguments': {
            'command_name': '\\opttest',
            'complete_start': 0,
            'complete_end': 15,
            'arguments': {
                '#2': {'value': 'value2', 'type': 'required'}  # Only required, missing optional
            }
        },
        'expected': 'First: Default1, Second: value2'
    },
    {
        'description': 'Test bracket position detection edge case',
        'command_definition': {
            'command_name': '\\complex',
            'syntax': '\\complex{#1}[#2]',  # Parameter #2 in brackets after #1
            'implementation': 'Param1: #1, Param2: #2',
            'default': 'OptDefault'
        },
        'parsed_arguments': {
            'command_name': '\\complex',
            'complete_start': 0,
            'complete_end': 18,
            'arguments': {
                '#1': {'value': 'first', 'type': 'required'}  # Missing #2 to trigger default
            }
        },
        'expected': 'Param1: first, Param2: OptDefault'
    },
    {
        'description': 'Test line 1434 coverage - multiple optional parameters with one missing',
        'command_definition': {
            'command_name': '\\multiopt',
            'syntax': '\\multiopt[#1][#2]',  # Two optional parameters
            'implementation': 'First: #1, Second: #2',
            'default': 'SharedDefault'
        },
        'parsed_arguments': {
            'command_name': '\\multiopt',
            'complete_start': 0,
            'complete_end': 12,
            'arguments': {
                '#1': {'value': 'first_provided', 'type': 'optional'}
                # Missing #2 - should trigger line 1434 for #2 parameter
            }
        },
        'expected': 'First: first_provided, Second: SharedDefault'
    },
    {
        'description': 'Test line 1434 coverage - required then optional with optional missing',
        'command_definition': {
            'command_name': '\\reqopt',
            'syntax': '\\reqopt{#1}[#2]',  # Required first, optional second
            'implementation': 'Req: #1, Opt: #2',
            'default': 'OptionalDefault'
        },
        'parsed_arguments': {
            'command_name': '\\reqopt',
            'complete_start': 0,
            'complete_end': 10,
            'arguments': {
                '#1': {'value': 'required_val', 'type': 'required'}
                # Missing #2 (optional) - should use default via line 1434
            }
        },
        'expected': 'Req: required_val, Opt: OptionalDefault'
    },
    {
        'description': 'Test missing branch 1374->1377 - unclosed bracket',
        'command_definition': {
            'command_name': '\\unclosed',
            'syntax': '\\unclosed[#1',  # Opening bracket but NO closing bracket
            'implementation': 'Value: #1',
            'default': 'DefaultValue'
        },
        'parsed_arguments': {
            'command_name': '\\unclosed',
            'complete_start': 0,
            'complete_end': 10,
            'arguments': {}  # No arguments provided - should fail since #1 is required (no closing bracket)
        },
        'expected': 'Error: No value available for parameter #1 in command'
    }
]

# Test cases for _apply_environment_definition method
ENVIRONMENT_APPLICATION_BASIC_TESTS = [
    {
        'description': 'Simple environment without parameters',
        'environment_definition': {
            'syntax': r'\begin{simpleenv}',
            'begin_implementation': r'\begin{center}',
            'end_implementation': r'\end{center}',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'simpleenv',
            'arguments': {}
        },
        'expected': (r'\begin{center}', r'\end{center}')
    },
    {
        'description': 'Environment with single required parameter',
        'environment_definition': {
            'syntax': r'\begin{myenv}{#1}',
            'begin_implementation': r'\begin{center}\textbf{#1}',
            'end_implementation': r'\end{center}',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'myenv',
            'arguments': {
                '#1': {'value': 'Hello World', 'type': 'required'}
            }
        },
        'expected': (r'\begin{center}\textbf{Hello World}', r'\end{center}')
    },
    {
        'description': 'Environment with multiple parameters',
        'environment_definition': {
            'syntax': r'\begin{complexenv}{#1}{#2}',
            'begin_implementation': r'\begin{#1}\large #2',
            'end_implementation': r'\end{#1}',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'complexenv',
            'arguments': {
                '#1': {'value': 'quote', 'type': 'required'},
                '#2': {'value': 'Important Text', 'type': 'required'}
            }
        },
        'expected': (r'\begin{quote}\large Important Text', r'\end{quote}')
    },
    {
        'description': 'Environment with optional parameter and default',
        'environment_definition': {
            'syntax': r'\begin{optenv}[#1]{#2}',
            'begin_implementation': r'\section*{#1}\begin{itemize} #2',
            'end_implementation': r'\end{itemize}',
            'default': 'Default Title'
        },
        'parsed_arguments': {
            'environment_name': 'optenv',
            'arguments': {
                '#2': {'value': 'List content', 'type': 'required'}
            }
        },
        'expected': (r'\section*{Default Title}\begin{itemize} List content', r'\end{itemize}')
    },
    {
        'description': 'Environment with provided optional parameter',
        'environment_definition': {
            'syntax': r'\begin{greetenv}[#1]{#2}',
            'begin_implementation': r'Hello #1, welcome #2',
            'end_implementation': r'Goodbye #1',
            'default': 'World'
        },
        'parsed_arguments': {
            'environment_name': 'greetenv',
            'arguments': {
                '#1': {'value': 'Friend', 'type': 'optional'},
                '#2': {'value': 'to our community', 'type': 'required'}
            }
        },
        'expected': ('Hello Friend, welcome to our community', 'Goodbye Friend')
    }
]

ENVIRONMENT_APPLICATION_EDGE_TESTS = [
    {
        'description': 'Environment with complex LaTeX in implementation',
        'environment_definition': {
            'syntax': r'\begin{mathenv}[#1]{#2}',
            'begin_implementation': r'\begin{equation}\label{#1} #2 =',
            'end_implementation': r'\end{equation}',
            'default': 'eq:default'
        },
        'parsed_arguments': {
            'environment_name': 'mathenv',
            'arguments': {
                '#2': {'value': r'E = mc^2', 'type': 'required'}
            }
        },
        'expected': (r'\begin{equation}\label{eq:default} E = mc^2 =', r'\end{equation}')
    },
    {
        'description': 'Environment with parameters appearing multiple times',
        'environment_definition': {
            'syntax': r'\begin{repeatenv}{#1}',
            'begin_implementation': r'Start #1, middle #1, prep #1',
            'end_implementation': r'End #1, final #1',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'repeatenv',
            'arguments': {
                '#1': {'value': 'TEST', 'type': 'required'}
            }
        },
        'expected': ('Start TEST, middle TEST, prep TEST', 'End TEST, final TEST')
    },
    {
        'description': 'Environment with special characters in parameters',
        'environment_definition': {
            'syntax': r'\begin{specialenv}{#1}',
            'begin_implementation': r'\texttt{#1}',
            'end_implementation': r'',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'specialenv',
            'arguments': {
                '#1': {'value': '\\LaTeX & $math$', 'type': 'required'}
            }
        },
        'expected': (r'\texttt{\LaTeX & $math$}', '')
    },
    {
        'description': 'Environment with empty implementations',
        'environment_definition': {
            'syntax': r'\begin{emptyenv}',
            'begin_implementation': '',
            'end_implementation': '',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'emptyenv',
            'arguments': {}
        },
        'expected': ('', '')
    },
    {
        'description': 'Environment with maximum parameters (9)',
        'environment_definition': {
            'syntax': r'\begin{maxenv}{#1}{#2}{#3}{#4}{#5}{#6}{#7}{#8}{#9}',
            'begin_implementation': r'#1#2#3#4#5#6#7#8#9',
            'end_implementation': r'#9#8#7#6#5#4#3#2#1',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'maxenv',
            'arguments': {
                f'#{i}': {'value': str(i), 'type': 'required'} for i in range(1, 10)
            }
        },
        'expected': ('123456789', '987654321')
    }
]

ENVIRONMENT_APPLICATION_ERROR_TESTS = [
    {
        'description': 'Invalid environment definition - not a dictionary',
        'environment_definition': 'not a dict',
        'parsed_arguments': {
            'environment_name': 'test',
            'arguments': {}
        },
        'expected_error': 'Environment definition must be a dictionary'
    },
    {
        'description': 'Invalid parsed arguments - not a dictionary',
        'environment_definition': {
            'syntax': r'\begin{test}',
            'begin_implementation': 'test',
            'end_implementation': 'test',
            'default': None
        },
        'parsed_arguments': 'not a dict',
        'expected_error': 'Parsed arguments must be a dictionary'
    },
    {
        'description': 'Missing syntax field',
        'environment_definition': {
            'begin_implementation': 'test',
            'end_implementation': 'test',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'test',
            'arguments': {}
        },
        'expected_error': 'Environment definition missing required field: syntax'
    },
    {
        'description': 'Missing begin_implementation field',
        'environment_definition': {
            'syntax': r'\begin{test}',
            'end_implementation': 'test',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'test',
            'arguments': {}
        },
        'expected_error': 'Environment definition missing required field: begin_implementation'
    },
    {
        'description': 'Missing end_implementation field',
        'environment_definition': {
            'syntax': r'\begin{test}',
            'begin_implementation': 'test',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'test',
            'arguments': {}
        },
        'expected_error': 'Environment definition missing required field: end_implementation'
    },
    {
        'description': 'Missing arguments field in parsed_arguments',
        'environment_definition': {
            'syntax': r'\begin{test}',
            'begin_implementation': 'test',
            'end_implementation': 'test',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'test'
        },
        'expected_error': "Parsed arguments missing 'arguments' field"
    },
    {
        'description': 'Syntax is not a string',
        'environment_definition': {
            'syntax': None,
            'begin_implementation': 'test',
            'end_implementation': 'test',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'test',
            'arguments': {}
        },
        'expected_error': 'Syntax must be a string'
    },
    {
        'description': 'Begin implementation is not a string',
        'environment_definition': {
            'syntax': r'\begin{test}',
            'begin_implementation': None,
            'end_implementation': 'test',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'test',
            'arguments': {}
        },
        'expected_error': 'Begin implementation must be a string'
    },
    {
        'description': 'End implementation is not a string',
        'environment_definition': {
            'syntax': r'\begin{test}',
            'begin_implementation': 'test',
            'end_implementation': None,
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'test',
            'arguments': {}
        },
        'expected_error': 'End implementation must be a string'
    },
    {
        'description': 'Too many arguments provided',
        'environment_definition': {
            'syntax': r'\begin{onearg}{#1}',
            'begin_implementation': 'Value: #1',
            'end_implementation': 'End',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'onearg',
            'arguments': {
                '#1': {'value': 'first', 'type': 'required'},
                '#2': {'value': 'second', 'type': 'required'}
            }
        },
        'expected_error': 'Too many arguments provided. Expected 1, got 2 for environment \'onearg\'.'
    },
    {
        'description': 'Missing required parameter',
        'environment_definition': {
            'syntax': r'\begin{reqenv}{#1}',
            'begin_implementation': 'Required: #1',
            'end_implementation': 'End',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'reqenv',
            'arguments': {}
        },
        'expected_error': "No value available for parameter #1 in environment 'reqenv'"
    },
    {
        'description': 'Missing optional parameter with no default',
        'environment_definition': {
            'syntax': r'\begin{optenv}[#1]{#2}',
            'begin_implementation': 'Opt: #1, Req: #2',
            'end_implementation': 'End',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'optenv',
            'arguments': {
                '#2': {'value': 'required_val', 'type': 'required'}
            }
        },
        'expected_error': "No value available for parameter #1 in environment 'optenv'"
    }
]

ENVIRONMENT_APPLICATION_COVERAGE_TESTS = [
    {
        'description': 'Coverage test - extract environment name from complex syntax',
        'environment_definition': {
            'syntax': r'\begin{complex_env_name}[#1]{#2}',
            'begin_implementation': 'Begin: #1, #2',
            'end_implementation': 'End: #1',
            'default': 'default_val'
        },
        'parsed_arguments': {
            'environment_name': 'complex_env_name',
            'arguments': {
                '#2': {'value': 'test_value', 'type': 'required'}
            }
        },
        'expected': ('Begin: default_val, test_value', 'End: default_val')
    },
    {
        'description': 'Coverage test - malformed syntax without environment name',
        'environment_definition': {
            'syntax': r'malformed_syntax',  # No \begin{} pattern
            'begin_implementation': 'test',
            'end_implementation': 'test',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'unknown',
            'arguments': {}
        },
        'expected': ('test', 'test')  # Should still work, env_name used for error messages only
    },
    {
        'description': 'Coverage test - optional parameter with exactly one missing argument',
        'environment_definition': {
            'syntax': r'\begin{opttest}[#1]{#2}',
            'begin_implementation': 'Start #1: #2',
            'end_implementation': 'End #1',
            'default': 'DefaultOpt'
        },
        'parsed_arguments': {
            'environment_name': 'opttest',
            'arguments': {
                '#2': {'value': 'RequiredValue', 'type': 'required'}
            }
        },
        'expected': ('Start DefaultOpt: RequiredValue', 'End DefaultOpt')
    },
    {
        'description': 'Coverage test - required parameter type detection in bracket analysis',
        'environment_definition': {
            'syntax': r'\begin{brackettest}{#1}[#2]',  # Required then optional
            'begin_implementation': 'Req: #1, Opt: #2',
            'end_implementation': 'End',
            'default': 'OptDefault'
        },
        'parsed_arguments': {
            'environment_name': 'brackettest',
            'arguments': {
                '#1': {'value': 'ReqValue', 'type': 'required'}
            }
        },
        'expected': ('Req: ReqValue, Opt: OptDefault', 'End')
    },
    {
        'description': 'Coverage test - parameter without surrounding brackets',
        'environment_definition': {
            'syntax': r'\begin{nobracket}#1',  # Parameter without brackets
            'begin_implementation': 'Value: #1',
            'end_implementation': 'End',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'nobracket',
            'arguments': {
                '#1': {'value': 'TestValue', 'type': 'required'}
            }
        },
        'expected': ('Value: TestValue', 'End')
    },
    {
        'description': 'Coverage test - parameter at start position (start_pos = 0)',
        'environment_definition': {
            'syntax': r'#1\begin{startparam}',  # Parameter at very beginning
            'begin_implementation': 'Start: #1',
            'end_implementation': 'End',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'startparam',
            'arguments': {}  # No arguments since parameter at start_pos=0 won't be processed
        },
        'expected': ('Start: #1', 'End')  # Parameter won't be substituted
    },
    {
        'description': 'Coverage test - unclosed bracket (no closing ] found)',
        'environment_definition': {
            'syntax': r'\begin{unclosed}[#1',  # Opening bracket but no closing bracket
            'begin_implementation': 'Value: #1',
            'end_implementation': 'End',
            'default': None
        },
        'parsed_arguments': {
            'environment_name': 'unclosed',
            'arguments': {
                '#1': {'value': 'TestValue', 'type': 'required'}
            }
        },
        'expected': ('Value: TestValue', 'End')
    }
]
