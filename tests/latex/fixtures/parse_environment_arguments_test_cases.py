# Test cases for parse_environment_arguments method

PARSE_ENVIRONMENT_ARGUMENTS_BASIC_TESTS = [
    {
        'description': 'array environment with optional and required arguments',
        'content': r'\begin{array}[c]{llr}',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{array}[pos]{cols}',
        'expected': {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 21,
            'arguments': {
                'pos': {
                    'value': 'c',
                    'start': 13,
                    'end': 16,
                    'type': 'optional'
                },
                'cols': {
                    'value': 'llr',
                    'start': 16,
                    'end': 21,
                    'type': 'required'
                }
            }
        }
    },
    {
        'description': 'tabular* environment with width, optional pos, and required cols',
        'content': r'\begin{tabular*}{10cm}[t]{lrc}',
        'environment_name': 'tabular*',
        'begin_start': 0,
        'begin_end': 16,
        'syntax': r'\begin{tabular*}{width}[pos]{cols}',
        'expected': {
            'environment_name': 'tabular*',
            'complete_start': 0,
            'complete_end': 30,
            'arguments': {
                'width': {
                    'value': '10cm',
                    'start': 16,
                    'end': 22,
                    'type': 'required'
                },
                'pos': {
                    'value': 't',
                    'start': 22,
                    'end': 25,
                    'type': 'optional'
                },
                'cols': {
                    'value': 'lrc',
                    'start': 25,
                    'end': 30,
                    'type': 'required'
                }
            }
        }
    },
    {
        'description': 'figure environment with optional location argument',
        'content': r'\begin{figure}[htbp]',
        'environment_name': 'figure',
        'begin_start': 0,
        'begin_end': 14,
        'syntax': r'\begin{figure}[loc]',
        'expected': {
            'environment_name': 'figure',
            'complete_start': 0,
            'complete_end': 20,
            'arguments': {
                'loc': {
                    'value': 'htbp',
                    'start': 14,
                    'end': 20,
                    'type': 'optional'
                }
            }
        }
    },
    {
        'description': 'equation environment with no arguments',
        'content': r'\begin{equation}',
        'environment_name': 'equation',
        'begin_start': 0,
        'begin_end': 16,
        'syntax': r'\begin{equation}',
        'expected': {
            'environment_name': 'equation',
            'complete_start': 0,
            'complete_end': 16,
            'arguments': {}
        }
    }
]

PARSE_ENVIRONMENT_ARGUMENTS_WHITESPACE_TESTS = [
    {
        'description': 'array environment with whitespace around arguments',
        'content': r'\begin{array}  [c]  {llr}',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{array}[pos]{cols}',
        'expected': {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 25,
            'arguments': {
                'pos': {
                    'value': 'c',
                    'start': 15,
                    'end': 18,
                    'type': 'optional'
                },
                'cols': {
                    'value': 'llr',
                    'start': 20,
                    'end': 25,
                    'type': 'required'
                }
            }
        }
    }
]

PARSE_ENVIRONMENT_ARGUMENTS_OPTIONAL_TESTS = [
    {
        'description': 'array environment missing optional argument',
        'content': r'\begin{array}{llr}',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{array}[pos]{cols}',
        'expected': {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 18,
            'arguments': {
                'cols': {
                    'value': 'llr',
                    'start': 13,
                    'end': 18,
                    'type': 'required'
                }
            }
        }
    },
    {
        'description': 'figure environment missing optional argument',
        'content': r'\begin{figure}',
        'environment_name': 'figure',
        'begin_start': 0,
        'begin_end': 14,
        'syntax': r'\begin{figure}[loc]',
        'expected': {
            'environment_name': 'figure',
            'complete_start': 0,
            'complete_end': 14,
            'arguments': {}
        }
    }
]

PARSE_ENVIRONMENT_ARGUMENTS_EDGE_CASE_TESTS = [
    {
        'description': 'empty content',
        'content': '',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 5,
        'syntax': r'\begin{array}[pos]{cols}',
        'expected': None
    },
    {
        'description': 'invalid positions',
        'content': r'\begin{array}[c]{llr}',
        'environment_name': 'array',
        'begin_start': 5,
        'begin_end': 3,  # end before start
        'syntax': r'\begin{array}[pos]{cols}',
        'expected': None
    },
    {
        'description': 'missing required argument',
        'content': r'\begin{array}[c]',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{array}[pos]{cols}',
        'expected': {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 16,
            'arguments': {
                'pos': {
                    'value': 'c',
                    'start': 13,
                    'end': 16,
                    'type': 'optional'
                }
            }
        }
    }
]

PARSE_ENVIRONMENT_ARGUMENTS_NESTED_TESTS = [
    {
        'description': 'nested braces in argument',
        'content': r'\begin{array}{l{2cm}r}',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{array}{cols}',
        'expected': {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 22,
            'arguments': {
                'cols': {
                    'value': 'l{2cm}r',
                    'start': 13,
                    'end': 22,
                    'type': 'required'
                }
            }
        }
    },
    {
        'description': 'nested brackets in optional argument',
        'content': r'\begin{figure}[[htbp]]',
        'environment_name': 'figure',
        'begin_start': 0,
        'begin_end': 14,
        'syntax': r'\begin{figure}[loc]',
        'expected': {
            'environment_name': 'figure',
            'complete_start': 0,
            'complete_end': 22,
            'arguments': {
                'loc': {
                    'value': '[htbp]',
                    'start': 14,
                    'end': 22,
                    'type': 'optional'
                }
            }
        }
    }
]

PARSE_ENVIRONMENT_ARGUMENTS_COMPLEX_TESTS = [
    {
        'description': 'complex tabular column specification',
        'content': r'\begin{tabular}{|>{\raggedleft\hspace{0pt}}p{14mm}|>{\centering\hspace{0pt}}p{14mm}|>{\raggedright\hspace{0pt}}p{14mm}|}',
        'environment_name': 'tabular',
        'begin_start': 0,
        'begin_end': 15,
        'syntax': r'\begin{tabular}[pos]{cols}',
        'expected': {
            'environment_name': 'tabular',
            'complete_start': 0,
            'complete_end': 120,
            'arguments': {
                'cols': {
                    'value': r'|>{\raggedleft\hspace{0pt}}p{14mm}|>{\centering\hspace{0pt}}p{14mm}|>{\raggedright\hspace{0pt}}p{14mm}|',
                    'start': 15,
                    'end': 120,
                    'type': 'required'
                }
            }
        }
    },
    {
        'description': 'deeply nested braces',
        'content': r'\begin{array}{c{{{inner}}}c}',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{array}{cols}',
        'expected': {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 28,
            'arguments': {
                'cols': {
                    'value': 'c{{{inner}}}c',
                    'start': 13,
                    'end': 28,
                    'type': 'required'
                }
            }
        }
    },
    {
        'description': 'mixed brackets and braces in tabular',
        'content': r'\begin{tabular}[t]{|>{\centering[width]{5cm}}p{2cm}|}',
        'environment_name': 'tabular',
        'begin_start': 0,
        'begin_end': 15,
        'syntax': r'\begin{tabular}[pos]{cols}',
        'expected': {
            'environment_name': 'tabular',
            'complete_start': 0,
            'complete_end': 53,
            'arguments': {
                'pos': {
                    'value': 't',
                    'start': 15,
                    'end': 18,
                    'type': 'optional'
                },
                'cols': {
                    'value': r'|>{\centering[width]{5cm}}p{2cm}|',
                    'start': 18,
                    'end': 53,
                    'type': 'required'
                }
            }
        }
    },
    {
        'description': 'escaped braces',
        'content': r'\begin{array}{\{c\}c}',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{array}{cols}',
        'expected': {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 21,
            'arguments': {
                'cols': {
                    'value': r'\{c\}c',
                    'start': 13,
                    'end': 21,
                    'type': 'required'
                }
            }
        }
    },
    {
        'description': 'complex optional with nested braces',
        'content': r'\begin{figure}[h!{special}]',
        'environment_name': 'figure',
        'begin_start': 0,
        'begin_end': 14,
        'syntax': r'\begin{figure}[loc]',
        'expected': {
            'environment_name': 'figure',
            'complete_start': 0,
            'complete_end': 27,
            'arguments': {
                'loc': {
                    'value': 'h!{special}',
                    'start': 14,
                    'end': 27,
                    'type': 'optional'
                }
            }
        }
    },
    {
        'description': 'multiple levels tabular*',
        'content': r'\begin{tabular*}{10cm}[b]{|>{\textbf{test}}c<{[end]}|}',
        'environment_name': 'tabular*',
        'begin_start': 0,
        'begin_end': 16,
        'syntax': r'\begin{tabular*}{width}[pos]{cols}',
        'expected': {
            'environment_name': 'tabular*',
            'complete_start': 0,
            'complete_end': 54,
            'arguments': {
                'width': {
                    'value': '10cm',
                    'start': 16,
                    'end': 22,
                    'type': 'required'
                },
                'pos': {
                    'value': 'b',
                    'start': 22,
                    'end': 25,
                    'type': 'optional'
                },
                'cols': {
                    'value': r'|>{\textbf{test}}c<{[end]}|',
                    'start': 25,
                    'end': 54,
                    'type': 'required'
                }
            }
        }
    },
    {
        'description': 'array with LaTeX environments inside',
        'content': r'\begin{array}[c]{>{\begin{small}}c<{\end{small}}|>{$}c<{$}}',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{array}[pos]{cols}',
        'expected': {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 59,
            'arguments': {
                'pos': {
                    'value': 'c',
                    'start': 13,
                    'end': 16,
                    'type': 'optional'
                },
                'cols': {
                    'value': r'>{\begin{small}}c<{\end{small}}|>{$}c<{$}',
                    'start': 16,
                    'end': 59,
                    'type': 'required'
                }
            }
        }
    }
]

PARSE_ENVIRONMENT_ARGUMENTS_ERROR_HANDLING_TESTS = [
    {
        'description': 'unmatched opening brace - graceful failure',
        'content': r'\begin{array}{c{missing',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{array}{cols}',
        'expected': {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 13,
            'arguments': {}
        }
    },
    {
        'description': 'unmatched opening bracket - skips malformed optional',
        'content': r'\begin{figure}[h[missing',
        'environment_name': 'figure',
        'begin_start': 0,
        'begin_end': 14,
        'syntax': r'\begin{figure}[loc]',
        'expected': {
            'environment_name': 'figure',
            'complete_start': 0,
            'complete_end': 14,
            'arguments': {}
        }
    },
    {
        'description': 'content too short for required argument',
        'content': r'\begin{array}',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{array}{cols}',
        'expected': {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 13,
            'arguments': {}
        }
    }
]

# Additional test cases for edge case coverage
PARSE_ENVIRONMENT_ARGUMENTS_EDGE_COVERAGE_TESTS = [
    {
        'description': 'required argument missing opening brace',
        'content': r'\begin{array}[pos]missing_brace',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{array}[pos]{cols}',
        'expected': {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 18,
            'arguments': {
                'pos': {
                    'value': 'pos',
                    'start': 13,
                    'end': 18,
                    'type': 'optional'
                }
            }
        }
    },
    {
        'description': 'required argument with no closing brace',
        'content': r'\begin{array}{unclosed_brace',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{array}{cols}',
        'expected': {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 13,
            'arguments': {}
        }
    },
    {
        'description': 'optional argument with no closing bracket',
        'content': r'\begin{array}[unclosed_bracket',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{array}[pos]{cols}',
        'expected': {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 13,
            'arguments': {}
        }
    },
    {
        'description': 'optional argument at wrong position',
        'content': r'\begin{array}{cols}[pos]',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{array}[pos]{cols}',
        'expected': {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 19,
            'arguments': {
                'cols': {
                    'value': 'cols',
                    'start': 13,
                    'end': 19,
                    'type': 'required'
                }
            }
        }
    },
    {
        'description': 'required argument missing but optional present',
        'content': r'\begin{tabular}[t]',
        'environment_name': 'tabular',
        'begin_start': 0,
        'begin_end': 15,
        'syntax': r'\begin{tabular}{cols}[pos]',
        'expected': {
            'environment_name': 'tabular',
            'complete_start': 0,
            'complete_end': 15,
            'arguments': {}
        }
    },
    {
        'description': 'required argument malformed brace parsing fails',
        'content': r'\begin{array}{unclosed_brace_content',
        'environment_name': 'array',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{array}{cols}',
        'expected': {
            'environment_name': 'array',
            'complete_start': 0,
            'complete_end': 13,
            'arguments': {}
        }
    },
    {
        'description': 'multiple required arguments to trigger continue branch',
        'content': r'\begin{minipage}{5cm}{content here}',
        'environment_name': 'minipage',
        'begin_start': 0,
        'begin_end': 16,
        'syntax': r'\begin{minipage}{width}{content}',
        'expected': {
            'environment_name': 'minipage',
            'complete_start': 0,
            'complete_end': 35,
            'arguments': {
                'width': {
                    'value': '5cm',
                    'start': 16,
                    'end': 21,
                    'type': 'required'
                },
                'content': {
                    'value': 'content here',
                    'start': 21,
                    'end': 35,
                    'type': 'required'
                }
            }
        }
    },
    {
        'description': 'required argument followed by optional to trigger continue',
        'content': r'\begin{table}{cols}[pos]',
        'environment_name': 'table',
        'begin_start': 0,
        'begin_end': 13,
        'syntax': r'\begin{table}{cols}[pos]',
        'expected': {
            'environment_name': 'table',
            'complete_start': 0,
            'complete_end': 24,
            'arguments': {
                'cols': {
                    'value': 'cols',
                    'start': 13,
                    'end': 19,
                    'type': 'required'
                },
                'pos': {
                    'value': 'pos',
                    'start': 19,
                    'end': 24,
                    'type': 'optional'
                }
            }
        }
    }
]

# Test cases for multiple required arguments to hit 182->156 branch
PARSE_ENVIRONMENT_ARGUMENTS_MULTIPLE_REQUIRED_TESTS = [
    {
        'description': 'multiple required arguments - hits 182->156 branch',
        'content': r'\begin{foo}{abc}{def}',
        'environment_name': 'foo',
        'begin_start': 0,
        'begin_end': 11,
        'syntax': r'\begin{foo}{first}{second}',
        'expected': {
            'environment_name': 'foo',
            'complete_start': 0,
            'complete_end': 21,
            'arguments': {
                'first': {
                    'value': 'abc',
                    'start': 11,
                    'end': 16,
                    'type': 'required'
                },
                'second': {
                    'value': 'def',
                    'start': 16,
                    'end': 21,
                    'type': 'required'
                }
            }
        }
    }
]

# Test case for the ValueError path - this should only be used internally 
# to test error handling for malformed syntax definitions
PARSE_ENVIRONMENT_ARGUMENTS_ERROR_COVERAGE_TESTS = [
    {
        'content': r'\begin{foo}',
        'syntax': r'\begin{foo}',  # This will be modified in the test to have invalid arg_type
        'expected_error': ValueError,
        'expected_message': 'can not happen'
    }
]

# Test cases for environments with * character
PARSE_ENVIRONMENT_ARGUMENTS_STAR_TESTS = [
    {
        'description': 'equation* environment basic',
        'content': r'\begin{equation*}',
        'environment_name': 'equation*',
        'begin_start': 0,
        'begin_end': 17,
        'syntax': r'\begin{equation*}',
        'expected': {
            'environment_name': 'equation*',
            'complete_start': 0,
            'complete_end': 17,
            'arguments': {}
        }
    },
    {
        'description': 'align* environment with arguments',
        'content': r'\begin{align*}[t]',
        'environment_name': 'align*',
        'begin_start': 0,
        'begin_end': 14,
        'syntax': r'\begin{align*}[pos]',
        'expected': {
            'environment_name': 'align*',
            'complete_start': 0,
            'complete_end': 17,
            'arguments': {
                'pos': {
                    'value': 't',
                    'start': 14,
                    'end': 17,
                    'type': 'optional'
                }
            }
        }
    },
    {
        'description': 'tabular* environment with width and position',
        'content': r'\begin{tabular*}{10cm}[b]',
        'environment_name': 'tabular*',
        'begin_start': 0,
        'begin_end': 16,
        'syntax': r'\begin{tabular*}{width}[pos]',
        'expected': {
            'environment_name': 'tabular*',
            'complete_start': 0,
            'complete_end': 25,
            'arguments': {
                'width': {
                    'value': '10cm',
                    'start': 16,
                    'end': 22,
                    'type': 'required'
                },
                'pos': {
                    'value': 'b',
                    'start': 22,
                    'end': 25,
                    'type': 'optional'
                }
            }
        }
    }
]