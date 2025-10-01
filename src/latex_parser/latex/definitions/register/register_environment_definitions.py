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


def register_latex_environments(registry: EnvironmentDefinitionRegistry) -> None:
    """
    Register LaTeX environments in the environment definition registry.

    :param registry: EnvironmentDefinitionRegistry, the registry to populate
    """
    
    register_tabular_environments(registry)
