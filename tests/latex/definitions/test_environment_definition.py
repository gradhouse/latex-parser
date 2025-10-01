# File: test_environment_definition.py
# Description: Unit tests for EnvironmentDefinition class and related enums
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import pytest
import copy
from typing import Dict, List, Any

from latex_parser.latex.definitions.environment_definition import (
    EnvironmentDefinition, EnvironmentMode, EnvironmentRobustness, EnvironmentType
)


class TestEnvironmentMode:
    """Test EnvironmentMode enum."""

    def test_all_environment_modes_exist(self):
        """Test that all expected environment modes are defined."""
        expected_modes = {
            'UNKNOWN', 'LEFT_RIGHT', 'PREAMBLE', 'PARAGRAPH', 'MATH_INLINE', 'MATH_DISPLAY'
        }
        actual_modes = {mode.name for mode in EnvironmentMode}
        assert actual_modes == expected_modes

    def test_environment_mode_values(self):
        """Test environment mode enum values."""
        assert EnvironmentMode.UNKNOWN.value == 'unknown'
        assert EnvironmentMode.LEFT_RIGHT.value == 'left_right'
        assert EnvironmentMode.PREAMBLE.value == 'preamble'
        assert EnvironmentMode.PARAGRAPH.value == 'paragraph'
        assert EnvironmentMode.MATH_INLINE.value == 'math_inline'
        assert EnvironmentMode.MATH_DISPLAY.value == 'math_display'

    def test_environment_mode_from_value(self):
        """Test creating environment modes from values."""
        assert EnvironmentMode('unknown') == EnvironmentMode.UNKNOWN
        assert EnvironmentMode('left_right') == EnvironmentMode.LEFT_RIGHT
        assert EnvironmentMode('preamble') == EnvironmentMode.PREAMBLE
        assert EnvironmentMode('paragraph') == EnvironmentMode.PARAGRAPH
        assert EnvironmentMode('math_inline') == EnvironmentMode.MATH_INLINE
        assert EnvironmentMode('math_display') == EnvironmentMode.MATH_DISPLAY

    def test_invalid_environment_mode_raises_error(self):
        """Test that invalid environment mode values raise ValueError."""
        with pytest.raises(ValueError):
            EnvironmentMode('invalid_mode')


class TestEnvironmentRobustness:
    """Test EnvironmentRobustness enum."""

    def test_all_environment_robustness_exist(self):
        """Test that all expected robustness values are defined."""
        expected_robustness = {'UNKNOWN', 'ROBUST', 'FRAGILE'}
        actual_robustness = {robustness.name for robustness in EnvironmentRobustness}
        assert actual_robustness == expected_robustness

    def test_environment_robustness_values(self):
        """Test environment robustness enum values."""
        assert EnvironmentRobustness.UNKNOWN.value == 'unknown'
        assert EnvironmentRobustness.ROBUST.value == 'robust'
        assert EnvironmentRobustness.FRAGILE.value == 'fragile'

    def test_environment_robustness_from_value(self):
        """Test creating environment robustness from values."""
        assert EnvironmentRobustness('unknown') == EnvironmentRobustness.UNKNOWN
        assert EnvironmentRobustness('robust') == EnvironmentRobustness.ROBUST
        assert EnvironmentRobustness('fragile') == EnvironmentRobustness.FRAGILE

    def test_invalid_environment_robustness_raises_error(self):
        """Test that invalid robustness values raise ValueError."""
        with pytest.raises(ValueError):
            EnvironmentRobustness('invalid_robustness')


class TestEnvironmentType:
    """Test EnvironmentType enum."""

    def test_all_environment_types_exist(self):
        """Test that all expected environment types are defined."""
        expected_types = {
            'UNKNOWN', 'DOCUMENT', 'DOCUMENT_SECTION', 'BIBLIOGRAPHY', 
            'FLOAT', 'ALIGNMENT', 'TABULAR', 'MATH_INLINE', 'MATH_DISPLAY'
        }
        actual_types = {env_type.name for env_type in EnvironmentType}
        assert actual_types == expected_types

    def test_environment_type_values(self):
        """Test environment type enum values."""
        assert EnvironmentType.UNKNOWN.value == 'unknown'
        assert EnvironmentType.TABULAR.value == 'tabular'
        assert EnvironmentType.MATH_DISPLAY.value == 'math_display'

    def test_environment_type_from_value(self):
        """Test creating environment types from values."""
        assert EnvironmentType('unknown') == EnvironmentType.UNKNOWN
        assert EnvironmentType('tabular') == EnvironmentType.TABULAR
        assert EnvironmentType('math_display') == EnvironmentType.MATH_DISPLAY

    def test_invalid_environment_type_raises_error(self):
        """Test that invalid environment type values raise ValueError."""
        with pytest.raises(ValueError):
            EnvironmentType('invalid_type')


class TestEnvironmentDefinition:
    """Test EnvironmentDefinition class."""

    def test_default_initialization(self):
        """Test initialization with default values."""
        env_def = EnvironmentDefinition()
        
        assert env_def._environment_definition['name'] == ""
        assert env_def._environment_definition['syntax'] == ""
        assert env_def._environment_definition['environment_type'] == EnvironmentType.UNKNOWN
        assert env_def._environment_definition['robustness'] == EnvironmentRobustness.UNKNOWN
        assert env_def._environment_definition['modes'] == []
        assert env_def._environment_definition['description'] == ""
        assert env_def._environment_definition['references'] == []

    def test_full_initialization(self):
        """Test initialization with all parameters provided."""
        modes = [EnvironmentMode.PARAGRAPH, EnvironmentMode.MATH_DISPLAY]
        references = [{'ref_id': 'lamport_1994', 'sections': '3.6', 'pages': '62-70'}]
        
        env_def = EnvironmentDefinition(
            name="tabular",
            syntax="\\begin{tabular}[pos]{cols}",
            environment_type=EnvironmentType.TABULAR,
            robustness=EnvironmentRobustness.ROBUST,
            modes=modes,
            description="Table environment with column specifications",
            references=references
        )
        
        assert env_def._environment_definition['name'] == "tabular"
        assert env_def._environment_definition['syntax'] == "\\begin{tabular}[pos]{cols}"
        assert env_def._environment_definition['environment_type'] == EnvironmentType.TABULAR
        assert env_def._environment_definition['robustness'] == EnvironmentRobustness.ROBUST
        assert env_def._environment_definition['modes'] == modes
        assert env_def._environment_definition['description'] == "Table environment with column specifications"
        assert env_def._environment_definition['references'] == references

    def test_partial_initialization_raises_error(self):
        """Test that partial parameter initialization raises ValueError."""
        # Test with only some parameters provided
        with pytest.raises(ValueError) as excinfo:
            EnvironmentDefinition(name="itemize")
        assert "Either all parameters must be None, or all must be provided" in str(excinfo.value)
        
        with pytest.raises(ValueError) as excinfo:
            EnvironmentDefinition(
                name="itemize",
                syntax="\\begin{itemize}",
                environment_type=EnvironmentType.UNKNOWN
            )
        assert "Either all parameters must be None, or all must be provided" in str(excinfo.value)

    def test_clear_method(self):
        """Test that clear method resets to default values."""
        # Start with a fully initialized environment
        env_def = EnvironmentDefinition(
            name="equation",
            syntax="\\begin{equation}",
            environment_type=EnvironmentType.MATH_DISPLAY,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Display math environment",
            references=[{'ref_id': 'test', 'sections': '1', 'pages': '1'}]
        )
        
        # Clear it
        env_def.clear()
        
        # Check that it's back to defaults
        assert env_def._environment_definition['name'] == ""
        assert env_def._environment_definition['syntax'] == ""
        assert env_def._environment_definition['environment_type'] == EnvironmentType.UNKNOWN
        assert env_def._environment_definition['robustness'] == EnvironmentRobustness.UNKNOWN
        assert env_def._environment_definition['modes'] == []
        assert env_def._environment_definition['description'] == ""
        assert env_def._environment_definition['references'] == []

    def test_as_dict_method(self):
        """Test conversion to dictionary for JSON serialization."""
        modes = [EnvironmentMode.PARAGRAPH, EnvironmentMode.LEFT_RIGHT]
        references = [
            {'ref_id': 'lamport_1994', 'sections': '3.6', 'pages': '62-70'},
            {'ref_id': 'companion', 'sections': '5.1', 'pages': '245-250'}
        ]
        
        env_def = EnvironmentDefinition(
            name="center",
            syntax="\\begin{center}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=modes,
            description="Center alignment environment",
            references=references
        )
        
        result_dict = env_def.as_dict()
        
        expected_dict = {
            'name': "center",
            'syntax': "\\begin{center}",
            'environment_type': 'unknown',
            'robustness': 'robust',
            'modes': ['paragraph', 'left_right'],
            'description': "Center alignment environment",
            'references': [
                {'ref_id': 'lamport_1994', 'sections': '3.6', 'pages': '62-70'},
                {'ref_id': 'companion', 'sections': '5.1', 'pages': '245-250'}
            ]
        }
        
        assert result_dict == expected_dict

    def test_as_dict_deep_copy_references(self):
        """Test that as_dict creates deep copy of references."""
        original_ref = {'ref_id': 'test', 'sections': '1', 'pages': '1'}
        
        env_def = EnvironmentDefinition(
            name="test",
            syntax="\\begin{test}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Test environment",
            references=[original_ref]
        )
        
        result_dict = env_def.as_dict()
        
        # Modify the original reference
        original_ref['new_key'] = 'new_value'
        
        # The dictionary should not be affected
        assert 'new_key' not in result_dict['references'][0]

    def test_from_dict_valid_data(self):
        """Test creating EnvironmentDefinition from valid dictionary."""
        data = {
            'name': "align",
            'syntax': "\\begin{align}",
            'environment_type': 'math_display',
            'robustness': 'fragile',
            'modes': ['paragraph', 'math_display'],
            'description': "Multi-line equation environment with alignment",
            'references': [{'ref_id': 'amsmath', 'sections': '2.1', 'pages': '8-10'}]
        }
        
        env_def = EnvironmentDefinition.from_dict(data)
        
        assert env_def._environment_definition['name'] == "align"
        assert env_def._environment_definition['syntax'] == "\\begin{align}"
        assert env_def._environment_definition['environment_type'] == EnvironmentType.MATH_DISPLAY
        assert env_def._environment_definition['robustness'] == EnvironmentRobustness.FRAGILE
        assert env_def._environment_definition['modes'] == [EnvironmentMode.PARAGRAPH, EnvironmentMode.MATH_DISPLAY]
        assert env_def._environment_definition['description'] == "Multi-line equation environment with alignment"
        assert env_def._environment_definition['references'] == [{'ref_id': 'amsmath', 'sections': '2.1', 'pages': '8-10'}]

    def test_from_dict_missing_fields_raises_error(self):
        """Test that from_dict raises ValueError for missing required fields."""
        incomplete_data = {
            'name': "test",
            'syntax': "\\begin{test}",
            # Missing other required fields
        }
        
        with pytest.raises(ValueError) as excinfo:
            EnvironmentDefinition.from_dict(incomplete_data)
        assert "Input dictionary is missing required fields" in str(excinfo.value)

    def test_from_dict_invalid_environment_type_raises_error(self):
        """Test that from_dict raises ValueError for invalid environment type."""
        data = {
            'name': "test",
            'syntax': "\\begin{test}",
            'environment_type': 'invalid_type',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': "Test environment",
            'references': []
        }
        
        with pytest.raises(ValueError) as excinfo:
            EnvironmentDefinition.from_dict(data)
        assert "Invalid environment_type value: invalid_type" in str(excinfo.value)

    def test_from_dict_invalid_robustness_raises_error(self):
        """Test that from_dict raises ValueError for invalid robustness."""
        data = {
            'name': "test",
            'syntax': "\\begin{test}",
            'environment_type': 'unknown',
            'robustness': 'invalid_robustness',
            'modes': ['paragraph'],
            'description': "Test environment",
            'references': []
        }
        
        with pytest.raises(ValueError) as excinfo:
            EnvironmentDefinition.from_dict(data)
        assert "Invalid robustness value: invalid_robustness" in str(excinfo.value)

    def test_from_dict_invalid_mode_raises_error(self):
        """Test that from_dict raises ValueError for invalid mode."""
        data = {
            'name': "test",
            'syntax': "\\begin{test}",
            'environment_type': 'unknown',
            'robustness': 'robust',
            'modes': ['paragraph', 'invalid_mode'],
            'description': "Test environment",
            'references': []
        }
        
        with pytest.raises(ValueError) as excinfo:
            EnvironmentDefinition.from_dict(data)
        assert "Invalid mode value in modes list" in str(excinfo.value)

    def test_from_dict_deep_copy_references(self):
        """Test that from_dict creates deep copy of references."""
        original_references = [{'ref_id': 'test', 'sections': '1', 'pages': '1'}]
        data = {
            'name': "test",
            'syntax': "\\begin{test}",
            'environment_type': 'unknown',
            'robustness': 'robust',
            'modes': ['paragraph'],
            'description': "Test environment",
            'references': original_references
        }
        
        env_def = EnvironmentDefinition.from_dict(data)
        
        # Modify the original references
        original_references[0]['new_key'] = 'new_value'
        
        # The environment definition should not be affected
        assert 'new_key' not in env_def._environment_definition['references'][0]

    def test_roundtrip_serialization(self):
        """Test that as_dict and from_dict are inverse operations."""
        original_env = EnvironmentDefinition(
            name="verbatim",
            syntax="\\begin{verbatim}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH, EnvironmentMode.LEFT_RIGHT],
            description="Verbatim text environment",
            references=[
                {'ref_id': 'lamport_1994', 'sections': '3.4.2', 'pages': '51-52'},
                {'ref_id': 'companion', 'sections': '3.4', 'pages': '98-102'}
            ]
        )
        
        # Convert to dict and back
        as_dict = original_env.as_dict()
        reconstructed_env = EnvironmentDefinition.from_dict(as_dict)
        
        # Compare all fields
        assert reconstructed_env._environment_definition['name'] == original_env._environment_definition['name']
        assert reconstructed_env._environment_definition['syntax'] == original_env._environment_definition['syntax']
        assert reconstructed_env._environment_definition['environment_type'] == original_env._environment_definition['environment_type']
        assert reconstructed_env._environment_definition['robustness'] == original_env._environment_definition['robustness']
        assert reconstructed_env._environment_definition['modes'] == original_env._environment_definition['modes']
        assert reconstructed_env._environment_definition['description'] == original_env._environment_definition['description']
        assert reconstructed_env._environment_definition['references'] == original_env._environment_definition['references']

    def test_multiple_modes(self):
        """Test environment definition with multiple modes."""
        modes = [
            EnvironmentMode.PARAGRAPH, 
            EnvironmentMode.LEFT_RIGHT, 
            EnvironmentMode.MATH_INLINE, 
            EnvironmentMode.MATH_DISPLAY
        ]
        
        env_def = EnvironmentDefinition(
            name="minipage",
            syntax="\\begin{minipage}[pos][height][inner-pos]{width}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=modes,
            description="Minipage environment for creating boxes",
            references=[]
        )
        
        assert len(env_def._environment_definition['modes']) == 4
        for mode in modes:
            assert mode in env_def._environment_definition['modes']

    def test_empty_modes_list(self):
        """Test environment definition with empty modes list."""
        env_def = EnvironmentDefinition(
            name="test",
            syntax="\\begin{test}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[],
            description="Test environment",
            references=[]
        )
        
        assert env_def._environment_definition['modes'] == []

    def test_empty_references_list(self):
        """Test environment definition with empty references list."""
        env_def = EnvironmentDefinition(
            name="test",
            syntax="\\begin{test}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Test environment",
            references=[]
        )
        
        assert env_def._environment_definition['references'] == []

    def test_complex_syntax_with_arguments(self):
        """Test environment definition with complex syntax containing arguments."""
        complex_syntax = "\\begin{longtable}[align]{column_spec}"
        
        env_def = EnvironmentDefinition(
            name="longtable",
            syntax=complex_syntax,
            environment_type=EnvironmentType.TABULAR,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Multi-page table environment",
            references=[{'ref_id': 'longtable', 'sections': '1', 'pages': '1-10'}]
        )
        
        assert env_def._environment_definition['syntax'] == complex_syntax
        assert "[align]" in env_def._environment_definition['syntax']
        assert "{column_spec}" in env_def._environment_definition['syntax']

    def test_special_characters_in_name(self):
        """Test environment definition with special characters in name."""
        env_def = EnvironmentDefinition(
            name="equation*",
            syntax="\\begin{equation*}",
            environment_type=EnvironmentType.MATH_DISPLAY,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Unnumbered equation environment",
            references=[]
        )
        
        assert env_def._environment_definition['name'] == "equation*"
        assert "*" in env_def._environment_definition['name']

    def test_different_environment_types(self):
        """Test environment definitions with different types."""
        # Math display environment
        math_env = EnvironmentDefinition(
            name="gather",
            syntax="\\begin{gather}",
            environment_type=EnvironmentType.MATH_DISPLAY,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Gather math environment",
            references=[]
        )
        
        # Tabular environment
        tabular_env = EnvironmentDefinition(
            name="array",
            syntax="\\begin{array}[pos]{cols}",
            environment_type=EnvironmentType.TABULAR,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.MATH_DISPLAY],
            description="Array environment for math mode",
            references=[]
        )
        
        # Unknown type environment
        unknown_env = EnvironmentDefinition(
            name="quote",
            syntax="\\begin{quote}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Quote environment",
            references=[]
        )
        
        assert math_env._environment_definition['environment_type'] == EnvironmentType.MATH_DISPLAY
        assert tabular_env._environment_definition['environment_type'] == EnvironmentType.TABULAR
        assert unknown_env._environment_definition['environment_type'] == EnvironmentType.UNKNOWN

    def test_different_robustness_values(self):
        """Test environment definitions with different robustness values."""
        # Robust environment
        robust_env = EnvironmentDefinition(
            name="itemize",
            syntax="\\begin{itemize}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Unordered list environment",
            references=[]
        )
        
        # Fragile environment
        fragile_env = EnvironmentDefinition(
            name="verbatim",
            syntax="\\begin{verbatim}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Verbatim environment",
            references=[]
        )
        
        # Unknown robustness
        unknown_env = EnvironmentDefinition(
            name="test",
            syntax="\\begin{test}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.UNKNOWN,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Test environment",
            references=[]
        )
        
        assert robust_env._environment_definition['robustness'] == EnvironmentRobustness.ROBUST
        assert fragile_env._environment_definition['robustness'] == EnvironmentRobustness.FRAGILE
        assert unknown_env._environment_definition['robustness'] == EnvironmentRobustness.UNKNOWN