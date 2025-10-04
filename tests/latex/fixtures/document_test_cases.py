"""
Test fixture data for document input command modernization functionality.
"""

# Basic input command modernization test cases
DOCUMENT_INPUT_BASIC_TESTS = [
    {
        "id": "simple_input_no_braces",
        "description": "Simple \\input command without braces",
        "input": "\\input myfile.tex",
        "expected": "\\input{myfile.tex}"
    },
    {
        "id": "input_with_whitespace",
        "description": "\\input command with whitespace before filename",
        "input": "\\input   myfile.tex",
        "expected": "\\input{myfile.tex}"
    },
    {
        "id": "input_already_correct",
        "description": "\\input command already has braces",
        "input": "\\input{myfile.tex}",
        "expected": "\\input{myfile.tex}"
    },
    {
        "id": "input_with_whitespace_and_braces",
        "description": "\\input command with whitespace before braces",
        "input": "\\input   {myfile.tex}",
        "expected": "\\input   {myfile.tex}"
    },
    {
        "id": "input_with_path",
        "description": "\\input command with file path",
        "input": "\\input chapters/chapter1.tex",
        "expected": "\\input{chapters/chapter1.tex}"
    }
]

# Multiple input commands test cases
DOCUMENT_INPUT_MULTIPLE_TESTS = [
    {
        "id": "multiple_inputs_mixed",
        "description": "Multiple \\input commands, some need modernization",
        "input": "\\input preamble.tex\n\\input{body.tex}\n\\input   appendix.tex",
        "expected": "\\input{preamble.tex}\n\\input{body.tex}\n\\input{appendix.tex}"
    },
    {
        "id": "inputs_with_text",
        "description": "\\input commands mixed with regular text",
        "input": "Start of document\n\\input intro.tex\nSome content\n\\input{middle.tex}\nMore content\n\\input outro.tex\nEnd",
        "expected": "Start of document\n\\input{intro.tex}\nSome content\n\\input{middle.tex}\nMore content\n\\input{outro.tex}\nEnd"
    },
    {
        "id": "consecutive_inputs",
        "description": "Consecutive \\input commands",
        "input": "\\input file1.tex\\input file2.tex\\input{file3.tex}",
        "expected": "\\input{file1.tex}\\input{file2.tex}\\input{file3.tex}"
    }
]

# Complex content test cases
DOCUMENT_INPUT_COMPLEX_TESTS = [
    {
        "id": "input_in_comment",
        "description": "\\input command inside a comment should not be changed",
        "input": "% This is a comment with \\input myfile.tex\n\\input realfile.tex",
        "expected": "% This is a comment with \\input myfile.tex\n\\input{realfile.tex}"
    },
    {
        "id": "input_with_underscores",
        "description": "\\input command with underscores in filename",
        "input": "\\input my_file_name.tex",
        "expected": "\\input{my_file_name.tex}"
    },
    {
        "id": "input_with_numbers",
        "description": "\\input command with numbers in filename",
        "input": "\\input chapter1_section2.tex",
        "expected": "\\input{chapter1_section2.tex}"
    }
]

# Edge cases and error conditions
DOCUMENT_INPUT_EDGE_TESTS = [
    {
        "id": "empty_string",
        "description": "Empty string should return empty string",
        "input": "",
        "expected": ""
    },
    {
        "id": "no_input_commands",
        "description": "Content with no \\input commands",
        "input": "This is just regular LaTeX content with no input commands.",
        "expected": "This is just regular LaTeX content with no input commands."
    },
    {
        "id": "input_at_end",
        "description": "\\input command at end of content",
        "input": "Some content\\input finalfile.tex",
        "expected": "Some content\\input{finalfile.tex}"
    },
    {
        "id": "input_at_beginning",
        "description": "\\input command at beginning of content",
        "input": "\\input startfile.tex some content",
        "expected": "\\input{startfile.tex} some content"
    },
    {
        "id": "input_only",
        "description": "Content with only \\input command",
        "input": "\\input onlyfile.tex",
        "expected": "\\input{onlyfile.tex}"
    },
    {
        "id": "input_incomplete",
        "description": "\\input command without filename",
        "input": "\\input",
        "expected": "\\input"
    },
    {
        "id": "input_incomplete_with_space",
        "description": "\\input command with only whitespace after",
        "input": "\\input   ",
        "expected": "\\input   "
    },
    {
        "id": "input_with_newline",
        "description": "\\input command followed by newline",
        "input": "\\input myfile.tex\nNext line",
        "expected": "\\input{myfile.tex}\nNext line"
    },
    {
        "id": "escaped_backslash_input",
        "description": "Escaped input command - \\\\input should be escaped",
        "input": "\\\\input notacommand.tex", 
        "expected": "\\\\input notacommand.tex"
    },
    {
        "id": "input_with_extension",
        "description": "\\input with .tex extension",
        "input": "\\input document.tex",
        "expected": "\\input{document.tex}"
    },
    {
        "id": "input_without_extension",
        "description": "\\input without file extension",
        "input": "\\input document",
        "expected": "\\input{document}"
    }
]