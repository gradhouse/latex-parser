# File: register_environment_definitions.py
# Description: Register LaTeX environment definitions
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

from typing import List
from latex_parser.latex.definitions.environment_definition import EnvironmentDefinition, EnvironmentType, EnvironmentMode, EnvironmentRobustness
from latex_parser.latex.definitions.environment_definition_registry import EnvironmentDefinitionRegistry


def register_tabular_environments(registry: EnvironmentDefinitionRegistry) -> None:
    """
    Register tabular environments in the environment definition registry.
    
    :param registry: EnvironmentDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for tabular environments
    references = [{'ref_id': 'latex_companion_2004', 'sections': 'C.10.2', 'pages': '204-207'}]
    
    def add_tabular_env(name: str, syntax: str, description: str, modes: List[EnvironmentMode]) -> None:
        registry.add_entry(name, EnvironmentDefinition(
            name=name, syntax=syntax, environment_type=EnvironmentType.TABULAR,
            robustness=EnvironmentRobustness.ROBUST, modes=modes,
            description=description, references=references
        ))
    
    # Array environment (math mode tabular - works in both inline and display math)
    add_tabular_env('array', '\\begin{array}[pos]{cols}', 
                   'tabular environment for math mode with column alignment specification', 
                   [EnvironmentMode.MATH_INLINE, EnvironmentMode.MATH_DISPLAY])
    
    # Basic tabular environment (works in most modes)
    add_tabular_env('tabular', '\\begin{tabular}[pos]{cols}', 
                   'tabular environment for creating tables with column alignment specification', 
                   [EnvironmentMode.PARAGRAPH, EnvironmentMode.LEFT_RIGHT, EnvironmentMode.MATH_INLINE, EnvironmentMode.MATH_DISPLAY])
    
    # Tabular* environment with specified width (works in most modes)
    add_tabular_env('tabular*', '\\begin{tabular*}{width}[pos]{cols}', 
                   'tabular environment with specified total width for creating tables', 
                   [EnvironmentMode.PARAGRAPH, EnvironmentMode.LEFT_RIGHT, EnvironmentMode.MATH_INLINE, EnvironmentMode.MATH_DISPLAY])


def register_equation_environments(registry: EnvironmentDefinitionRegistry) -> None:
    """
    Register equation and math display environments in the environment definition registry.
    
    :param registry: EnvironmentDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for equation environments
    references = [
        {'ref_id': 'latex_companion_2004', 'sections': '8.2, 8.2.1', 'pages': '468-471'},
        {'ref_id': 'lamport_1994', 'sections': 'C.7.1', 'pages': '187-189'}
    ]
    
    def add_equation_env(name: str, syntax: str, description: str, robustness: EnvironmentRobustness) -> None:
        registry.add_entry(name, EnvironmentDefinition(
            name=name, syntax=syntax, environment_type=EnvironmentType.MATH_DISPLAY,
            robustness=robustness, modes=[EnvironmentMode.PARAGRAPH],
            description=description, references=references
        ))
    
    # Basic equation environments (likely robust based on fundamental nature)
    add_equation_env('equation', '\\begin{equation}', 
                    'numbered displayed equation environment for single equations', 
                    EnvironmentRobustness.ROBUST)
    add_equation_env('equation*', '\\begin{equation*}', 
                    'unnumbered displayed equation environment for single equations', 
                    EnvironmentRobustness.ROBUST)
    
    # Multi-line equation environments (assuming robust but could be fragile)
    add_equation_env('multline', '\\begin{multline}', 
                    'numbered multi-line equation environment with automatic line breaking', 
                    EnvironmentRobustness.ROBUST)
    add_equation_env('multline*', '\\begin{multline*}', 
                    'unnumbered multi-line equation environment with automatic line breaking', 
                    EnvironmentRobustness.ROBUST)
    
    # Gather environments for multiple equations
    add_equation_env('gather', '\\begin{gather}', 
                    'numbered environment for gathering multiple equations with centered alignment', 
                    EnvironmentRobustness.ROBUST)
    add_equation_env('gather*', '\\begin{gather*}', 
                    'unnumbered environment for gathering multiple equations with centered alignment', 
                    EnvironmentRobustness.ROBUST)
    
    # Align environments for aligned equations
    add_equation_env('align', '\\begin{align}', 
                    'numbered environment for aligning multiple equations at specified points', 
                    EnvironmentRobustness.ROBUST)
    add_equation_env('align*', '\\begin{align*}', 
                    'unnumbered environment for aligning multiple equations at specified points', 
                    EnvironmentRobustness.ROBUST)
    
    # Full-width align environments
    add_equation_env('flalign', '\\begin{flalign}', 
                    'numbered full-width alignment environment for equations', 
                    EnvironmentRobustness.ROBUST)
    add_equation_env('flalign*', '\\begin{flalign*}', 
                    'unnumbered full-width alignment environment for equations', 
                    EnvironmentRobustness.ROBUST)
    
    # Subsidiary alignment environments (these might be more fragile)
    add_equation_env('split', '\\begin{split}', 
                    'environment for splitting single equations across multiple lines within other math environments', 
                    EnvironmentRobustness.FRAGILE)
    add_equation_env('gathered', '\\begin{gathered}', 
                    'subsidiary environment for gathering equations within other math environments', 
                    EnvironmentRobustness.FRAGILE)
    add_equation_env('aligned', '\\begin{aligned}', 
                    'subsidiary environment for aligned equations within other math environments', 
                    EnvironmentRobustness.FRAGILE)
    
    # Legacy equation environment
    add_equation_env('eqnarray', '\\begin{eqnarray}', 
                    'legacy numbered equation array environment (deprecated, use align instead)', 
                    EnvironmentRobustness.FRAGILE)


def register_math_environments(registry: EnvironmentDefinitionRegistry) -> None:
    """
    Register basic math environments in the environment definition registry.
    
    :param registry: EnvironmentDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for basic math environments
    references = [
        {'ref_id': 'lamport_1994', 'sections': 'C.7.1', 'pages': '187-189'}
    ]
    
    # Inline math environment
    registry.add_entry('math', EnvironmentDefinition(
        name='math', syntax='\\begin{math}', environment_type=EnvironmentType.MATH_INLINE,
        robustness=EnvironmentRobustness.ROBUST, modes=[EnvironmentMode.PARAGRAPH, EnvironmentMode.LEFT_RIGHT],
        description='verbose form of inline math environment, equivalent to \\(...\\)',
        references=references
    ))
    
    # Display math environment (unnumbered)
    registry.add_entry('displaymath', EnvironmentDefinition(
        name='displaymath', syntax='\\begin{displaymath}', environment_type=EnvironmentType.MATH_DISPLAY,
        robustness=EnvironmentRobustness.ROBUST, modes=[EnvironmentMode.PARAGRAPH],
        description='verbose form of display math environment, equivalent to \\[...\\]',
        references=references
    ))


def register_float_environments(registry: EnvironmentDefinitionRegistry) -> None:
    """
    Register float environments in the environment definition registry.
    
    :param registry: EnvironmentDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for float environments
    references = [
        {'ref_id': 'lamport_1994', 'sections': '3.5.1, C.9.1', 'pages': '58-59, 197-200'}
    ]
    
    def add_float_env(name: str, syntax: str, description: str, robustness: EnvironmentRobustness) -> None:
        registry.add_entry(name, EnvironmentDefinition(
            name=name, syntax=syntax, environment_type=EnvironmentType.FLOAT,
            robustness=robustness, modes=[EnvironmentMode.PARAGRAPH],
            description=description, references=references
        ))
    
    # Figure environments
    add_float_env('figure', '\\begin{figure}[loc]', 
                  'floating environment for figures with captions and cross-references', 
                  EnvironmentRobustness.FRAGILE)
    add_float_env('figure*', '\\begin{figure*}[loc]', 
                  'two-column floating environment for figures spanning both columns in two-column documents', 
                  EnvironmentRobustness.FRAGILE)
    
    # Table environments  
    add_float_env('table', '\\begin{table}[loc]', 
                  'floating environment for tables with captions and cross-references', 
                  EnvironmentRobustness.FRAGILE)
    add_float_env('table*', '\\begin{table*}[loc]', 
                  'two-column floating environment for tables spanning both columns in two-column documents', 
                  EnvironmentRobustness.FRAGILE)


def register_alignment_environments(registry: EnvironmentDefinitionRegistry) -> None:
    """
    Register alignment environments in the environment definition registry.
    
    :param registry: EnvironmentDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for alignment environments
    references = [
        {'ref_id': 'lamport_1994', 'sections': '6.5', 'pages': '111-112'}
    ]
    
    def add_alignment_env(name: str, syntax: str, description: str) -> None:
        registry.add_entry(name, EnvironmentDefinition(
            name=name, syntax=syntax, environment_type=EnvironmentType.ALIGNMENT,
            robustness=EnvironmentRobustness.ROBUST, modes=[EnvironmentMode.PARAGRAPH, EnvironmentMode.LEFT_RIGHT],
            description=description, references=references
        ))
    
    # Alignment environments
    add_alignment_env('center', '\\begin{center}', 
                     'centers text lines within the environment')
    add_alignment_env('flushleft', '\\begin{flushleft}', 
                     'left-aligns text lines within the environment, leaving right margin ragged')
    add_alignment_env('flushright', '\\begin{flushright}', 
                     'right-aligns text lines within the environment, leaving left margin ragged')


def register_document_section_environments(registry: EnvironmentDefinitionRegistry) -> None:
    """
    Register document section environments in the environment definition registry.
    
    :param registry: EnvironmentDefinitionRegistry, the registry to populate
    """
    
    # Abstract environment
    registry.add_entry('abstract', EnvironmentDefinition(
        name='abstract', 
        syntax='\\begin{abstract}', 
        environment_type=EnvironmentType.DOCUMENT_SECTION,
        robustness=EnvironmentRobustness.ROBUST, 
        modes=[EnvironmentMode.PARAGRAPH],
        description='document abstract environment for typesetting the abstract section',
        references=[
            {'ref_id': 'lamport_1994', 'sections': '6.1.3, C.5.4', 'pages': '90, 181-183'}
        ]
    ))


def register_bibliography_environments(registry: EnvironmentDefinitionRegistry) -> None:
    """
    Register bibliography environments in the environment definition registry.
    
    :param registry: EnvironmentDefinitionRegistry, the registry to populate
    """
    
    # Bibliography environment
    registry.add_entry('thebibliography', EnvironmentDefinition(
        name='thebibliography', 
        syntax='\\begin{thebibliography}{widest_label}', 
        environment_type=EnvironmentType.BIBLIOGRAPHY,
        robustness=EnvironmentRobustness.ROBUST, 
        modes=[EnvironmentMode.PARAGRAPH],
        description='bibliography environment for manually creating bibliography lists with \\bibitem entries',
        references=[
            {'ref_id': 'lamport_1994', 'sections': '4.3, C.11.3', 'pages': '69-72, 209-210'}
        ]
    ))


def register_latex_environments(registry: EnvironmentDefinitionRegistry) -> None:
    """
    Register LaTeX environments in the environment definition registry.

    :param registry: EnvironmentDefinitionRegistry, the registry to populate
    """
    
    register_tabular_environments(registry)
    register_math_environments(registry)
    register_equation_environments(registry)
    register_float_environments(registry)
    register_alignment_environments(registry)
    register_document_section_environments(registry)
    register_bibliography_environments(registry)
