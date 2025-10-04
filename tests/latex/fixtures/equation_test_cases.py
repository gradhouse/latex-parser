"""
Test fixture data for equation math delimiter modernization functionality.
"""

# Basic replacement test cases
EQUATION_MODERNIZE_BASIC_TESTS = [
    {
        "id": "single_closing_paren",
        "description": "Single \\) delimiter with no opening", 
        "input": "\\)",
        "expected": "\\)"
    },
    {
        "id": "inline_parentheses",
        "description": "Convert \\( \\) to \\begin{math} \\end{math}",
        "input": "Some text \\(x + y\\) more text",
        "expected": "Some text \\begin{math}x + y\\end{math} more text"
    },
    {
        "id": "single_dollar",
        "description": "Convert $ $ to \\begin{math} \\end{math}",
        "input": "Some text $x + y$ more text",
        "expected": "Some text \\begin{math}x + y\\end{math} more text"
    },
    {
        "id": "display_brackets", 
        "description": "Convert \\[ \\] to \\begin{displaymath} \\end{displaymath}",
        "input": "Some text \\[x + y\\] more text",
        "expected": "Some text \\begin{displaymath}x + y\\end{displaymath} more text"
    },
    {
        "id": "double_dollar",
        "description": "Convert $$ $$ to \\begin{displaymath} \\end{displaymath}",
        "input": "Some text $$x + y$$ more text", 
        "expected": "Some text \\begin{displaymath}x + y\\end{displaymath} more text"
    }
]

# Multiple delimiter test cases
EQUATION_MODERNIZE_MULTIPLE_TESTS = [
    {
        "id": "multiple_inline_math",
        "description": "Multiple inline math expressions",
        "input": "First $a$ then \\(b\\) and $c$",
        "expected": "First \\begin{math}a\\end{math} then \\begin{math}b\\end{math} and \\begin{math}c\\end{math}"
    },
    {
        "id": "multiple_display_math",
        "description": "Multiple display math expressions", 
        "input": "First $$a$$ then \\[b\\] and $$c$$",
        "expected": "First \\begin{displaymath}a\\end{displaymath} then \\begin{displaymath}b\\end{displaymath} and \\begin{displaymath}c\\end{displaymath}"
    },
    {
        "id": "mixed_math_types",
        "description": "Mixed inline and display math",
        "input": "Inline $x$ and display $$y$$ and \\(z\\) and \\[w\\]",
        "expected": "Inline \\begin{math}x\\end{math} and display \\begin{displaymath}y\\end{displaymath} and \\begin{math}z\\end{math} and \\begin{displaymath}w\\end{displaymath}"
    }
]

# Complex content test cases
EQUATION_MODERNIZE_COMPLEX_TESTS = [
    {
        "id": "escaped_dollars_ignored",
        "description": "Escaped dollars should not be replaced",
        "input": "Price is \\$5 and math is $x + y$",
        "expected": "Price is \\$5 and math is \\begin{math}x + y\\end{math}"
    },
    {
        "id": "nested_content",
        "description": "Math with complex nested LaTeX commands",
        "input": "Complex \\(\\frac{a}{b} + \\sqrt{c}\\) expression",
        "expected": "Complex \\begin{math}\\frac{a}{b} + \\sqrt{c}\\end{math} expression"
    },
    {
        "id": "complex_display_math",
        "description": "Display math with complex content",
        "input": "Equation $$\\sum_{i=1}^{n} x_i = \\int_0^1 f(x) dx$$ is important",
        "expected": "Equation \\begin{displaymath}\\sum_{i=1}^{n} x_i = \\int_0^1 f(x) dx\\end{displaymath} is important"
    }
]

# Edge case test cases
EQUATION_MODERNIZE_EDGE_TESTS = [
    {
        "id": "empty_content",
        "description": "Empty content should return empty",
        "input": "",
        "expected": ""
    },
    {
        "id": "no_math_delimiters",
        "description": "Content with no math delimiters",
        "input": "Just regular text with no math",
        "expected": "Just regular text with no math"
    },
    {
        "id": "unmatched_single_dollar",
        "description": "Unmatched single dollar should be left as-is",
        "input": "Incomplete math $x + y and more text",
        "expected": "Incomplete math $x + y and more text"
    },
    {
        "id": "unmatched_double_dollar",
        "description": "Unmatched double dollar should be left as-is",
        "input": "Incomplete math $$x + y and more text",
        "expected": "Incomplete math $$x + y and more text"
    },
    {
        "id": "unmatched_parentheses",
        "description": "Unmatched \\( should be left as-is",
        "input": "Incomplete math \\(x + y and more text",
        "expected": "Incomplete math \\(x + y and more text"
    },
    {
        "id": "unmatched_brackets",
        "description": "Unmatched \\[ should be left as-is",
        "input": "Incomplete math \\[x + y and more text",
        "expected": "Incomplete math \\[x + y and more text"
    },
    {
        "id": "unmatched_closing_parentheses",
        "description": "Unmatched \\) should be left as-is",
        "input": "Incomplete math x + y\\) and more text",
        "expected": "Incomplete math x + y\\) and more text"
    },
    {
        "id": "unmatched_closing_brackets",
        "description": "Unmatched \\] should be left as-is",
        "input": "Incomplete math x + y\\] and more text",
        "expected": "Incomplete math x + y\\] and more text"
    },
    {
        "id": "mixed_unmatched_delimiters",
        "description": "Mixed unmatched delimiters should be left as-is",
        "input": "Mix \\( with \\] mismatch and \\[ with \\) mismatch",
        "expected": "Mix \\begin{math} with \\] mismatch and \\[ with \\end{math} mismatch"
    },
    {
        "id": "just_closing_bracket",
        "description": "Just \\] with no opening bracket",
        "input": "Just \\] alone",
        "expected": "Just \\] alone"
    },
    {
        "id": "just_closing_paren",
        "description": "Just \\) with no opening paren",
        "input": "Just \\) alone", 
        "expected": "Just \\) alone"
    },
    {
        "id": "single_closing_bracket",
        "description": "Single \\] delimiter with no opening",
        "input": "\\]",
        "expected": "\\]"
    },
    {
        "id": "single_closing_paren",
        "description": "Single \\) delimiter with no opening", 
        "input": "\\)",
        "expected": "\\)"
    },
    {
        "id": "empty_math_content",
        "description": "Empty math expressions should work",
        "input": "Empty $$$$text and \\(\\) and \\[\\]",
        "expected": "Empty \\begin{displaymath}\\end{displaymath}text and \\begin{math}\\end{math} and \\begin{displaymath}\\end{displaymath}"
    }
]