# File: test_register_environment_definitions.py
# Description: Unit tests for register_environment_definitions module
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import pytest
from typing import Set

from latex_parser.latex.definitions.environment_definition_registry import EnvironmentDefinitionRegistry
from latex_parser.latex.definitions.environment_definition import (
    EnvironmentDefinition, EnvironmentType, EnvironmentMode, EnvironmentRobustness
)
from latex_parser.latex.definitions.register.register_environment_definitions import (
    register_tabular_environments, 
    register_latex_environments,
    register_document_section_environments,
    register_bibliography_environments
)


class TestRegisterTabularEnvironments:
    """Test register_tabular_environments function."""

    def test_registers_expected_tabular_environments(self):
        """Test that all expected tabular environments are registered and only those."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        expected_environments = {'array', 'tabular', 'tabular*'}
        registered_keys = set(registry.list_keys())
        
        assert registered_keys == expected_environments

    def test_array_environment_properties(self):
        """Test that array environment is registered with correct properties."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        array_env = registry.get_entry('array')
        
        assert array_env._environment_definition['name'] == 'array'
        assert array_env._environment_definition['syntax'] == '\\begin{array}[pos]{cols}'
        assert array_env._environment_definition['environment_type'] == EnvironmentType.TABULAR
        assert array_env._environment_definition['robustness'] == EnvironmentRobustness.ROBUST
        assert array_env._environment_definition['modes'] == [EnvironmentMode.MATH_INLINE, EnvironmentMode.MATH_DISPLAY]
        assert array_env._environment_definition['description'] == 'tabular environment for math mode with column alignment specification'
        assert len(array_env._environment_definition['references']) == 1

    def test_tabular_environment_properties(self):
        """Test that tabular environment is registered with correct properties."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        tabular_env = registry.get_entry('tabular')
        
        assert tabular_env._environment_definition['name'] == 'tabular'
        assert tabular_env._environment_definition['syntax'] == '\\begin{tabular}[pos]{cols}'
        assert tabular_env._environment_definition['environment_type'] == EnvironmentType.TABULAR
        assert tabular_env._environment_definition['robustness'] == EnvironmentRobustness.ROBUST
        expected_modes = [EnvironmentMode.PARAGRAPH, EnvironmentMode.LEFT_RIGHT, 
                         EnvironmentMode.MATH_INLINE, EnvironmentMode.MATH_DISPLAY]
        assert tabular_env._environment_definition['modes'] == expected_modes
        assert tabular_env._environment_definition['description'] == 'tabular environment for creating tables with column alignment specification'

    def test_tabular_star_environment_properties(self):
        """Test that tabular* environment is registered with correct properties."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        tabular_star_env = registry.get_entry('tabular*')
        
        assert tabular_star_env._environment_definition['name'] == 'tabular*'
        assert tabular_star_env._environment_definition['syntax'] == '\\begin{tabular*}{width}[pos]{cols}'
        assert tabular_star_env._environment_definition['environment_type'] == EnvironmentType.TABULAR
        assert tabular_star_env._environment_definition['robustness'] == EnvironmentRobustness.ROBUST
        expected_modes = [EnvironmentMode.PARAGRAPH, EnvironmentMode.LEFT_RIGHT, 
                         EnvironmentMode.MATH_INLINE, EnvironmentMode.MATH_DISPLAY]
        assert tabular_star_env._environment_definition['modes'] == expected_modes
        assert tabular_star_env._environment_definition['description'] == 'tabular environment with specified total width for creating tables'

    def test_all_tabular_environments_have_tabular_type(self):
        """Test that all tabular environments have TABULAR type."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        for env_name in ['array', 'tabular', 'tabular*']:
            env = registry.get_entry(env_name)
            assert env._environment_definition['environment_type'] == EnvironmentType.TABULAR

    def test_all_tabular_environments_are_robust(self):
        """Test that all tabular environments are robust."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        for env_name in ['array', 'tabular', 'tabular*']:
            env = registry.get_entry(env_name)
            assert env._environment_definition['robustness'] == EnvironmentRobustness.ROBUST

    def test_tabular_environments_have_references(self):
        """Test that all tabular environments have proper references."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        expected_references = [{'ref_id': 'latex_companion_2004', 'sections': 'C.10.2', 'pages': '204-207'}]
        
        for env_name in ['array', 'tabular', 'tabular*']:
            env = registry.get_entry(env_name)
            assert env._environment_definition['references'] == expected_references

    def test_array_has_math_modes_only(self):
        """Test that array environment only works in math modes."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        array_env = registry.get_entry('array')
        modes = array_env._environment_definition['modes']
        
        assert EnvironmentMode.MATH_INLINE in modes
        assert EnvironmentMode.MATH_DISPLAY in modes
        assert EnvironmentMode.PARAGRAPH not in modes
        assert EnvironmentMode.LEFT_RIGHT not in modes
        assert EnvironmentMode.PREAMBLE not in modes

    def test_tabular_and_tabular_star_have_same_modes(self):
        """Test that tabular and tabular* have the same mode restrictions."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        tabular_modes = set(mode.value for mode in registry.get_entry('tabular')._environment_definition['modes'])
        tabular_star_modes = set(mode.value for mode in registry.get_entry('tabular*')._environment_definition['modes'])
        
        assert tabular_modes == tabular_star_modes

    def test_tabular_environments_exclude_unknown_and_preamble(self):
        """Test that tabular and tabular* exclude UNKNOWN and PREAMBLE modes."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        for env_name in ['tabular', 'tabular*']:
            env = registry.get_entry(env_name)
            modes = env._environment_definition['modes']
            
            assert EnvironmentMode.UNKNOWN not in modes
            assert EnvironmentMode.PREAMBLE not in modes

    def test_different_syntax_patterns(self):
        """Test that environments have different syntax patterns as expected."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        array_syntax = registry.get_entry('array')._environment_definition['syntax']
        tabular_syntax = registry.get_entry('tabular')._environment_definition['syntax']
        tabular_star_syntax = registry.get_entry('tabular*')._environment_definition['syntax']
        
        # Array and tabular have same syntax pattern
        assert array_syntax == '\\begin{array}[pos]{cols}'
        assert tabular_syntax == '\\begin{tabular}[pos]{cols}'
        
        # Tabular* has width parameter
        assert '{width}' in tabular_star_syntax
        assert '[pos]' in tabular_star_syntax
        assert '{cols}' in tabular_star_syntax

    def test_registry_initially_empty(self):
        """Test that the registry is initially empty before registration."""
        registry = EnvironmentDefinitionRegistry()
        assert len(registry.list_keys()) == 0
        
        register_tabular_environments(registry)
        assert len(registry.list_keys()) == 3

    def test_multiple_registrations_dont_duplicate(self):
        """Test that calling register_tabular_environments multiple times raises error for duplicates."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        # Should raise error when trying to register again
        with pytest.raises(KeyError):
            register_tabular_environments(registry)

    def test_environment_descriptions_are_descriptive(self):
        """Test that environment descriptions contain meaningful information."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        array_desc = registry.get_entry('array')._environment_definition['description']
        tabular_desc = registry.get_entry('tabular')._environment_definition['description']
        tabular_star_desc = registry.get_entry('tabular*')._environment_definition['description']
        
        # Check that descriptions contain key terms
        assert 'math mode' in array_desc.lower()
        assert 'column' in array_desc.lower()
        
        assert 'table' in tabular_desc.lower()
        assert 'column' in tabular_desc.lower()
        
        assert 'width' in tabular_star_desc.lower()
        assert 'table' in tabular_star_desc.lower()


class TestRegisterFloatEnvironments:
    """Test register_float_environments function."""

    def test_registers_expected_float_environments(self):
        """Test that all expected float environments are registered."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_float_environments
        register_float_environments(registry)
        
        expected_environments = {'figure', 'figure*', 'table', 'table*'}
        registered_keys = set(registry.list_keys())
        
        assert registered_keys == expected_environments

    def test_all_float_environments_have_float_type(self):
        """Test that all float environments have FLOAT type."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_float_environments
        register_float_environments(registry)
        
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            assert env._environment_definition['environment_type'] == EnvironmentType.FLOAT

    def test_all_float_environments_work_in_paragraph_mode(self):
        """Test that all float environments work in paragraph mode."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_float_environments
        register_float_environments(registry)
        
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            modes = env._environment_definition['modes']
            assert EnvironmentMode.PARAGRAPH in modes
            assert len(modes) == 1  # Should only work in paragraph mode

    def test_all_float_environments_are_fragile(self):
        """Test that all float environments are fragile."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_float_environments
        register_float_environments(registry)
        
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            assert env._environment_definition['robustness'] == EnvironmentRobustness.FRAGILE

    def test_float_environments_have_proper_references(self):
        """Test that all float environments have proper references."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_float_environments
        register_float_environments(registry)
        
        expected_references = [
            {'ref_id': 'lamport_1994', 'sections': '3.5.1, C.9.1', 'pages': '58-59, 197-200'}
        ]
        
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            assert env._environment_definition['references'] == expected_references

    def test_specific_float_environment_properties(self):
        """Test specific properties of float environments."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_float_environments
        register_float_environments(registry)
        
        # Test figure environment
        figure_env = registry.get_entry('figure')
        assert figure_env._environment_definition['name'] == 'figure'
        assert figure_env._environment_definition['syntax'] == '\\begin{figure}[loc]'
        assert 'floating environment for figures' in figure_env._environment_definition['description']
        
        # Test figure* environment
        figure_star_env = registry.get_entry('figure*')
        assert figure_star_env._environment_definition['name'] == 'figure*'
        assert 'two-column' in figure_star_env._environment_definition['description']
        assert 'spanning both columns' in figure_star_env._environment_definition['description']
        
        # Test table environment
        table_env = registry.get_entry('table')
        assert table_env._environment_definition['name'] == 'table'
        assert table_env._environment_definition['syntax'] == '\\begin{table}[loc]'
        assert 'floating environment for tables' in table_env._environment_definition['description']
        
        # Test table* environment
        table_star_env = registry.get_entry('table*')
        assert table_star_env._environment_definition['name'] == 'table*'
        assert 'two-column' in table_star_env._environment_definition['description']

    def test_float_environments_have_location_parameter(self):
        """Test that float environments include location parameter in syntax."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_float_environments
        register_float_environments(registry)
        
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            syntax = env._environment_definition['syntax']
            assert '[loc]' in syntax, f"Environment {env_name} should have [loc] parameter"


class TestRegisterMathEnvironments:
    """Test register_math_environments function."""

    def test_registers_expected_math_environments(self):
        """Test that all expected basic math environments are registered."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_math_environments
        register_math_environments(registry)
        
        expected_environments = {'math', 'displaymath'}
        registered_keys = set(registry.list_keys())
        
        assert registered_keys == expected_environments

    def test_math_environment_properties(self):
        """Test that math environment has correct properties."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_math_environments
        register_math_environments(registry)
        
        math_env = registry.get_entry('math')
        
        assert math_env._environment_definition['name'] == 'math'
        assert math_env._environment_definition['syntax'] == '\\begin{math}'
        assert math_env._environment_definition['environment_type'] == EnvironmentType.MATH_INLINE
        assert math_env._environment_definition['robustness'] == EnvironmentRobustness.ROBUST
        expected_modes = [EnvironmentMode.PARAGRAPH, EnvironmentMode.LEFT_RIGHT]
        assert math_env._environment_definition['modes'] == expected_modes
        assert 'inline math' in math_env._environment_definition['description']
        assert '\\(...\\)' in math_env._environment_definition['description']

    def test_displaymath_environment_properties(self):
        """Test that displaymath environment has correct properties."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_math_environments
        register_math_environments(registry)
        
        displaymath_env = registry.get_entry('displaymath')
        
        assert displaymath_env._environment_definition['name'] == 'displaymath'
        assert displaymath_env._environment_definition['syntax'] == '\\begin{displaymath}'
        assert displaymath_env._environment_definition['environment_type'] == EnvironmentType.MATH_DISPLAY
        assert displaymath_env._environment_definition['robustness'] == EnvironmentRobustness.ROBUST
        assert displaymath_env._environment_definition['modes'] == [EnvironmentMode.PARAGRAPH]
        assert 'display math' in displaymath_env._environment_definition['description']
        assert '\\[...\\]' in displaymath_env._environment_definition['description']

    def test_math_environments_have_proper_references(self):
        """Test that basic math environments have proper references."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_math_environments
        register_math_environments(registry)
        
        expected_references = [
            {'ref_id': 'lamport_1994', 'sections': 'C.7.1', 'pages': '187-189'}
        ]
        
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            assert env._environment_definition['references'] == expected_references


class TestRegisterEquationEnvironments:
    """Test register_equation_environments function."""

    def test_registers_expected_equation_environments(self):
        """Test that all expected equation environments are registered and only those."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_equation_environments
        register_equation_environments(registry)
        
        expected_environments = {
            'equation', 'equation*', 'multline', 'multline*', 'gather', 'gather*',
            'align', 'align*', 'flalign', 'flalign*', 'split', 'gathered', 'aligned', 'eqnarray'
        }
        registered_keys = set(registry.list_keys())
        
        assert registered_keys == expected_environments

    def test_all_equation_environments_have_math_display_type(self):
        """Test that all equation environments have MATH_DISPLAY type."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_equation_environments
        register_equation_environments(registry)
        
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            assert env._environment_definition['environment_type'] == EnvironmentType.MATH_DISPLAY

    def test_all_equation_environments_work_in_paragraph_mode(self):
        """Test that all equation environments work in paragraph mode."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_equation_environments
        register_equation_environments(registry)
        
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            modes = env._environment_definition['modes']
            assert EnvironmentMode.PARAGRAPH in modes
            assert len(modes) == 1  # Should only work in paragraph mode

    def test_robust_vs_fragile_equation_environments(self):
        """Test the distribution of robust vs fragile equation environments."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_equation_environments
        register_equation_environments(registry)
        
        robust_envs = []
        fragile_envs = []
        
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            robustness = env._environment_definition['robustness']
            
            if robustness == EnvironmentRobustness.ROBUST:
                robust_envs.append(env_name)
            elif robustness == EnvironmentRobustness.FRAGILE:
                fragile_envs.append(env_name)
        
        # Main environments should be robust
        expected_robust = {
            'equation', 'equation*', 'multline', 'multline*', 'gather', 'gather*',
            'align', 'align*', 'flalign', 'flalign*'
        }
        # Subsidiary environments and legacy should be fragile
        expected_fragile = {'split', 'gathered', 'aligned', 'eqnarray'}
        
        assert set(robust_envs) == expected_robust
        assert set(fragile_envs) == expected_fragile

    def test_equation_environments_have_proper_references(self):
        """Test that all equation environments have proper references."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_equation_environments
        register_equation_environments(registry)
        
        expected_references = [
            {'ref_id': 'latex_companion_2004', 'sections': '8.2, 8.2.1', 'pages': '468-471'},
            {'ref_id': 'lamport_1994', 'sections': 'C.7.1', 'pages': '187-189'}
        ]
        
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            assert env._environment_definition['references'] == expected_references

    def test_specific_equation_environment_properties(self):
        """Test specific properties of key equation environments."""
        registry = EnvironmentDefinitionRegistry()
        from latex_parser.latex.definitions.register.register_environment_definitions import register_equation_environments
        register_equation_environments(registry)
        
        # Test equation environment
        equation_env = registry.get_entry('equation')
        assert equation_env._environment_definition['name'] == 'equation'
        assert equation_env._environment_definition['syntax'] == '\\begin{equation}'
        assert 'numbered displayed equation' in equation_env._environment_definition['description']
        
        # Test equation* environment
        equation_star_env = registry.get_entry('equation*')
        assert equation_star_env._environment_definition['name'] == 'equation*'
        assert 'unnumbered displayed equation' in equation_star_env._environment_definition['description']
        
        # Test align environment
        align_env = registry.get_entry('align')
        assert 'aligning multiple equations' in align_env._environment_definition['description']
        
        # Test eqnarray environment (legacy)
        eqnarray_env = registry.get_entry('eqnarray')
        assert 'legacy' in eqnarray_env._environment_definition['description']
        assert 'deprecated' in eqnarray_env._environment_definition['description']


class TestRegisterDocumentSectionEnvironments:
    """Test register_document_section_environments function."""

    def test_registers_expected_document_section_environments(self):
        """Test that all expected document section environments are registered and only those."""
        registry = EnvironmentDefinitionRegistry()
        register_document_section_environments(registry)

        expected_environments = {'abstract'}
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected environments are present
        assert registered_keys == expected_environments, f"Expected {expected_environments}, got {registered_keys}"

    def test_document_section_environments_have_correct_type(self):
        """Test that document section environments have correct environment type."""
        registry = EnvironmentDefinitionRegistry()
        register_document_section_environments(registry)

        # Check that the document section environments have correct environment_type
        for env_name in ['abstract']:
            assert registry.get_entry(env_name)._environment_definition['environment_type'] == EnvironmentType.DOCUMENT_SECTION


class TestRegisterBibliographyEnvironments:
    """Test register_bibliography_environments function."""

    def test_registers_expected_bibliography_environments(self):
        """Test that all expected bibliography environments are registered and only those."""
        registry = EnvironmentDefinitionRegistry()
        register_bibliography_environments(registry)

        expected_environments = {'thebibliography'}
        
        registered_keys = set(registry.list_keys())
        
        # Check that exactly the expected environments are present
        assert registered_keys == expected_environments, f"Expected {expected_environments}, got {registered_keys}"

    def test_bibliography_environments_have_correct_type(self):
        """Test that bibliography environments have correct environment type."""
        registry = EnvironmentDefinitionRegistry()
        register_bibliography_environments(registry)

        # Check that the bibliography environments have correct environment_type
        for env_name in ['thebibliography']:
            assert registry.get_entry(env_name)._environment_definition['environment_type'] == EnvironmentType.BIBLIOGRAPHY


class TestRegisterLatexEnvironments:
    """Test register_latex_environments function."""

    def test_calls_tabular_registration(self):
        """Test that register_latex_environments calls tabular registration."""
        registry = EnvironmentDefinitionRegistry()
        register_latex_environments(registry)
        
        # Should have tabular environments registered
        expected_tabular_environments = {'array', 'tabular', 'tabular*'}
        registered_keys = set(registry.list_keys())
        
        # Check that all tabular environments are present
        assert expected_tabular_environments.issubset(registered_keys)
        
        # Should also have basic math environments
        expected_math_environments = {'math', 'displaymath'}
        assert expected_math_environments.issubset(registered_keys)

    def test_expected_total_environment_count(self):
        """Test that the total number of registered environments matches expectations."""
        registry = EnvironmentDefinitionRegistry()
        register_latex_environments(registry)
        
        # Currently tabular (3) + basic math (2) + equation (14) + float (4) + alignment (3) + document section (1) + bibliography (1) environments are registered
        expected_total = 28  # 3 tabular + 2 basic math + 14 equation + 4 float + 3 alignment + 1 document section + 1 bibliography environments
        actual_total = len(registry.list_keys())
        
        assert actual_total == expected_total

    def test_environment_consistency_across_runs(self):
        """Test that the same environments are registered consistently across multiple runs."""
        # First run
        registry1 = EnvironmentDefinitionRegistry()
        register_latex_environments(registry1)
        keys1 = set(registry1.list_keys())
        
        # Second run
        registry2 = EnvironmentDefinitionRegistry()
        register_latex_environments(registry2)
        keys2 = set(registry2.list_keys())
        
        # Should be identical
        assert keys1 == keys2

    def test_all_registered_environments_are_valid(self):
        """Test that all registered environments have valid definitions."""
        registry = EnvironmentDefinitionRegistry()
        register_latex_environments(registry)
        
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            
            # Check that all required fields are present and valid
            assert env._environment_definition['name'] != ""
            assert env._environment_definition['syntax'] != ""
            assert env._environment_definition['environment_type'] != EnvironmentType.UNKNOWN
            assert env._environment_definition['robustness'] in [EnvironmentRobustness.ROBUST, EnvironmentRobustness.FRAGILE]
            assert len(env._environment_definition['modes']) > 0
            assert env._environment_definition['description'] != ""
            assert isinstance(env._environment_definition['references'], list)

    def test_no_duplicate_environment_names(self):
        """Test that no environment names are duplicated."""
        registry = EnvironmentDefinitionRegistry()
        register_latex_environments(registry)
        
        keys = registry.list_keys()
        unique_keys = set(keys)
        
        # Number of keys should equal number of unique keys
        assert len(keys) == len(unique_keys)

    def test_environments_categorized_correctly(self):
        """Test that environments are categorized with appropriate types."""
        registry = EnvironmentDefinitionRegistry()
        register_latex_environments(registry)
        
        # Count environments by type
        type_counts = {}
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            env_type = env._environment_definition['environment_type']
            type_counts[env_type] = type_counts.get(env_type, 0) + 1
        
        # Currently should have tabular, math inline, math display, and float environments
        assert EnvironmentType.TABULAR in type_counts
        assert EnvironmentType.MATH_INLINE in type_counts
        assert EnvironmentType.MATH_DISPLAY in type_counts
        assert EnvironmentType.FLOAT in type_counts
        assert type_counts[EnvironmentType.TABULAR] == 3
        assert type_counts[EnvironmentType.MATH_INLINE] == 1
        assert type_counts[EnvironmentType.MATH_DISPLAY] == 15  # 14 equation + 1 displaymath
        assert type_counts[EnvironmentType.FLOAT] == 4

    def test_robustness_distribution(self):
        """Test the distribution of robust vs fragile environments."""
        registry = EnvironmentDefinitionRegistry()
        register_latex_environments(registry)
        
        robust_count = 0
        fragile_count = 0
        
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            robustness = env._environment_definition['robustness']
            
            if robustness == EnvironmentRobustness.ROBUST:
                robust_count += 1
            elif robustness == EnvironmentRobustness.FRAGILE:
                fragile_count += 1
        
        # Currently tabular environments (3) are robust, basic math (2) are robust, equation environments (10) are robust, subsidiary (4) are fragile, float (4) are fragile, alignment (3) are robust, document section (1) are robust, bibliography (1) are robust
        assert robust_count == 20
        assert fragile_count == 8

    def test_mode_distribution(self):
        """Test that environments have appropriate mode distributions."""
        registry = EnvironmentDefinitionRegistry()
        register_latex_environments(registry)
        
        mode_usage = {}
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            for mode in env._environment_definition['modes']:
                mode_usage[mode] = mode_usage.get(mode, 0) + 1
        
        # Check expected mode usage patterns
        assert EnvironmentMode.MATH_DISPLAY in mode_usage  # All tabular environments support this
        assert EnvironmentMode.MATH_INLINE in mode_usage   # All tabular environments support this
        assert EnvironmentMode.PARAGRAPH in mode_usage     # tabular and tabular* support this
        assert EnvironmentMode.LEFT_RIGHT in mode_usage    # tabular and tabular* support this
        
        # UNKNOWN and PREAMBLE should not be used
        assert EnvironmentMode.UNKNOWN not in mode_usage
        assert EnvironmentMode.PREAMBLE not in mode_usage

    def test_all_environments_have_references(self):
        """Test that all registered environments have reference documentation."""
        registry = EnvironmentDefinitionRegistry()
        register_latex_environments(registry)
        
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            references = env._environment_definition['references']
            
            assert isinstance(references, list)
            assert len(references) > 0
            
            # Check reference structure
            for ref in references:
                assert isinstance(ref, dict)
                assert 'ref_id' in ref
                assert 'sections' in ref
                assert 'pages' in ref

    def test_registry_serialization_compatibility(self):
        """Test that registered environments are compatible with serialization."""
        registry = EnvironmentDefinitionRegistry()
        register_latex_environments(registry)
        
        # Test that all environments can be serialized
        for env_name in registry.list_keys():
            env = registry.get_entry(env_name)
            serialized = env.as_dict()
            
            # Check serialized structure
            assert isinstance(serialized, dict)
            assert 'name' in serialized
            assert 'syntax' in serialized
            assert 'environment_type' in serialized
            assert 'robustness' in serialized
            assert 'modes' in serialized
            assert 'description' in serialized
            assert 'references' in serialized
            
            # Test roundtrip
            reconstructed = EnvironmentDefinition.from_dict(serialized)
            assert reconstructed._environment_definition['name'] == env._environment_definition['name']


class TestTabularEnvironmentIntegration:
    """Integration tests for tabular environment registration."""

    def test_array_math_mode_usage(self):
        """Test that array environment is properly configured for math mode usage."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        array_env = registry.get_entry('array')
        modes = array_env._environment_definition['modes']
        
        # Should work in both inline and display math
        assert EnvironmentMode.MATH_INLINE in modes
        assert EnvironmentMode.MATH_DISPLAY in modes
        
        # Should NOT work in text modes
        assert EnvironmentMode.PARAGRAPH not in modes
        assert EnvironmentMode.LEFT_RIGHT not in modes

    def test_tabular_versatile_usage(self):
        """Test that tabular environments are configured for versatile usage."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        for env_name in ['tabular', 'tabular*']:
            env = registry.get_entry(env_name)
            modes = env._environment_definition['modes']
            
            # Should work in most modes except unknown and preamble
            assert EnvironmentMode.PARAGRAPH in modes
            assert EnvironmentMode.LEFT_RIGHT in modes
            assert EnvironmentMode.MATH_INLINE in modes
            assert EnvironmentMode.MATH_DISPLAY in modes
            
            # Should NOT work in these modes
            assert EnvironmentMode.UNKNOWN not in modes
            assert EnvironmentMode.PREAMBLE not in modes

    def test_syntax_differences_reflect_usage(self):
        """Test that syntax differences reflect intended usage patterns."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        array_syntax = registry.get_entry('array')._environment_definition['syntax']
        tabular_syntax = registry.get_entry('tabular')._environment_definition['syntax']
        tabular_star_syntax = registry.get_entry('tabular*')._environment_definition['syntax']
        
        # All should have column specification
        for syntax in [array_syntax, tabular_syntax, tabular_star_syntax]:
            assert '{cols}' in syntax
            assert '[pos]' in syntax
        
        # Only tabular* should have width specification
        assert '{width}' not in array_syntax
        assert '{width}' not in tabular_syntax
        assert '{width}' in tabular_star_syntax

    def test_consistent_tabular_type_assignment(self):
        """Test that all table-like environments get TABULAR type."""
        registry = EnvironmentDefinitionRegistry()
        register_tabular_environments(registry)
        
        tabular_environments = ['array', 'tabular', 'tabular*']
        
        for env_name in tabular_environments:
            env = registry.get_entry(env_name)
            assert env._environment_definition['environment_type'] == EnvironmentType.TABULAR