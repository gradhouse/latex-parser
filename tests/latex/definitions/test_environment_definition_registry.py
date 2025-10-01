# File: test_environment_definition_registry.py
# Description: Unit tests for EnvironmentDefinitionRegistry class
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import pytest
import tempfile
import os
from typing import Type

from latex_parser.latex.definitions.environment_definition_registry import EnvironmentDefinitionRegistry
from latex_parser.latex.definitions.environment_definition import (
    EnvironmentDefinition, EnvironmentType, EnvironmentRobustness, EnvironmentMode
)
from latex_parser.services.registry import Registry


class TestEnvironmentDefinitionRegistry:
    """Test EnvironmentDefinitionRegistry class."""

    def test_initialization_without_file(self):
        """Test that registry initializes correctly without a file path."""
        registry = EnvironmentDefinitionRegistry()
        assert isinstance(registry, EnvironmentDefinitionRegistry)
        assert len(registry.list_keys()) == 0

    def test_initialization_with_nonexistent_file(self):
        """Test that registry raises FileNotFoundError for nonexistent file."""
        with pytest.raises(FileNotFoundError):
            EnvironmentDefinitionRegistry("/nonexistent/path/file.json")

    def test_get_entry_type(self):
        """Test that get_entry_type returns EnvironmentDefinition."""
        registry = EnvironmentDefinitionRegistry()
        assert registry.get_entry_type() == EnvironmentDefinition

    def test_for_type_raises_error(self):
        """Test that for_type raises TypeError to prevent specialization."""
        with pytest.raises(TypeError) as excinfo:
            EnvironmentDefinitionRegistry.for_type(str)
        assert "EnvironmentDefinitionRegistry can only store EnvironmentDefinition objects" in str(excinfo.value)
        assert "str" in str(excinfo.value)

    def test_add_and_get_entry(self):
        """Test adding and retrieving environment definitions."""
        registry = EnvironmentDefinitionRegistry()
        
        # Create a test environment definition
        env_def = EnvironmentDefinition(
            name="itemize",
            syntax="\\begin{itemize}[options]",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Unordered list environment",
            references=[{'ref_id': 'lamport_1994', 'sections': '3.3', 'pages': '45-46'}]
        )
        
        # Add and retrieve
        registry.add_entry("itemize", env_def)
        retrieved = registry.get_entry("itemize")
        
        assert retrieved is not None
        assert retrieved._environment_definition['name'] == "itemize"
        assert retrieved._environment_definition['syntax'] == "\\begin{itemize}[options]"
        assert retrieved._environment_definition['environment_type'] == EnvironmentType.UNKNOWN
        assert retrieved._environment_definition['robustness'] == EnvironmentRobustness.ROBUST
        assert retrieved._environment_definition['modes'] == [EnvironmentMode.PARAGRAPH]
        assert retrieved._environment_definition['description'] == "Unordered list environment"

    def test_add_duplicate_key_raises_error(self):
        """Test that adding duplicate keys raises KeyError."""
        registry = EnvironmentDefinitionRegistry()
        
        env_def1 = EnvironmentDefinition(
            name="equation",
            syntax="\\begin{equation}",
            environment_type=EnvironmentType.MATH_DISPLAY,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Display math environment",
            references=[]
        )
        
        env_def2 = EnvironmentDefinition(
            name="equation",
            syntax="\\begin{equation}",
            environment_type=EnvironmentType.MATH_DISPLAY,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Another equation environment",
            references=[]
        )
        
        registry.add_entry("equation", env_def1)
        
        with pytest.raises(KeyError):
            registry.add_entry("equation", env_def2)

    def test_get_nonexistent_entry_raises_error(self):
        """Test that getting nonexistent entry raises KeyError."""
        registry = EnvironmentDefinitionRegistry()
        
        with pytest.raises(KeyError):
            registry.get_entry("nonexistent")

    def test_is_key_present(self):
        """Test key presence checking."""
        registry = EnvironmentDefinitionRegistry()
        
        env_def = EnvironmentDefinition(
            name="center",
            syntax="\\begin{center}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Center alignment environment",
            references=[]
        )
        
        assert not registry.is_key_present("center")
        registry.add_entry("center", env_def)
        assert registry.is_key_present("center")

    def test_list_keys(self):
        """Test listing all keys in registry."""
        registry = EnvironmentDefinitionRegistry()
        
        # Start with empty registry
        assert registry.list_keys() == []
        
        # Add some environments
        env_def1 = EnvironmentDefinition(
            name="itemize",
            syntax="\\begin{itemize}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Unordered list",
            references=[]
        )
        
        env_def2 = EnvironmentDefinition(
            name="equation",
            syntax="\\begin{equation}",
            environment_type=EnvironmentType.MATH_DISPLAY,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Display math",
            references=[]
        )
        
        registry.add_entry("itemize", env_def1)
        registry.add_entry("equation", env_def2)
        
        keys = registry.list_keys()
        assert len(keys) == 2
        assert "itemize" in keys
        assert "equation" in keys

    def test_update_entry(self):
        """Test updating existing entries."""
        registry = EnvironmentDefinitionRegistry()
        
        # Add initial entry
        env_def1 = EnvironmentDefinition(
            name="align",
            syntax="\\begin{align}",
            environment_type=EnvironmentType.MATH_DISPLAY,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Original description",
            references=[]
        )
        
        registry.add_entry("align", env_def1)
        
        # Update with new entry
        env_def2 = EnvironmentDefinition(
            name="align",
            syntax="\\begin{align}[placement]",
            environment_type=EnvironmentType.MATH_DISPLAY,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Updated description",
            references=[{'ref_id': 'amsmath', 'sections': '2.1', 'pages': '10'}]
        )
        
        registry.update_entry("align", env_def2)
        
        retrieved = registry.get_entry("align")
        assert retrieved._environment_definition['syntax'] == "\\begin{align}[placement]"
        assert retrieved._environment_definition['description'] == "Updated description"
        assert len(retrieved._environment_definition['references']) == 1

    def test_update_nonexistent_entry_raises_error(self):
        """Test that updating nonexistent entry raises KeyError."""
        registry = EnvironmentDefinitionRegistry()
        
        env_def = EnvironmentDefinition(
            name="gather",
            syntax="\\begin{gather}",
            environment_type=EnvironmentType.MATH_DISPLAY,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Gather environment",
            references=[]
        )
        
        with pytest.raises(KeyError):
            registry.update_entry("gather", env_def)

    def test_delete_entry(self):
        """Test deleting entries."""
        registry = EnvironmentDefinitionRegistry()
        
        env_def = EnvironmentDefinition(
            name="verbatim",
            syntax="\\begin{verbatim}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Verbatim text environment",
            references=[]
        )
        
        registry.add_entry("verbatim", env_def)
        assert registry.is_key_present("verbatim")
        
        registry.delete_entry("verbatim")
        assert not registry.is_key_present("verbatim")

    def test_delete_nonexistent_entry_raises_error(self):
        """Test that deleting nonexistent entry raises KeyError."""
        registry = EnvironmentDefinitionRegistry()
        
        with pytest.raises(KeyError):
            registry.delete_entry("nonexistent")

    def test_clear(self):
        """Test clearing all entries."""
        registry = EnvironmentDefinitionRegistry()
        
        # Add some entries
        env_def1 = EnvironmentDefinition(
            name="table",
            syntax="\\begin{table}[placement]",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Table float",
            references=[]
        )
        
        env_def2 = EnvironmentDefinition(
            name="figure",
            syntax="\\begin{figure}[placement]",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Figure float",
            references=[]
        )
        
        registry.add_entry("table", env_def1)
        registry.add_entry("figure", env_def2)
        assert len(registry.list_keys()) == 2
        
        registry.clear()
        assert len(registry.list_keys()) == 0

    def test_serialization_roundtrip(self):
        """Test saving to and loading from JSON file."""
        registry = EnvironmentDefinitionRegistry()
        
        # Add test environments
        env_def1 = EnvironmentDefinition(
            name="enumerate",
            syntax="\\begin{enumerate}[label]",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Ordered list environment",
            references=[{'ref_id': 'lamport_1994', 'sections': '3.3', 'pages': '47-48'}]
        )
        
        env_def2 = EnvironmentDefinition(
            name="multline",
            syntax="\\begin{multline}",
            environment_type=EnvironmentType.MATH_DISPLAY,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Multi-line equation environment",
            references=[{'ref_id': 'amsmath', 'sections': '3.2', 'pages': '15'}]
        )
        
        registry.add_entry("enumerate", env_def1)
        registry.add_entry("multline", env_def2)
        
        # Save to temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            tmp_path = tmp_file.name
        
        try:
            registry.save_to_json(tmp_path)
            
            # Load into new registry
            new_registry = EnvironmentDefinitionRegistry(tmp_path)
            
            # Verify contents
            assert len(new_registry.list_keys()) == 2
            assert new_registry.is_key_present("enumerate")
            assert new_registry.is_key_present("multline")
            
            # Check specific environment
            retrieved_enum = new_registry.get_entry("enumerate")
            assert retrieved_enum._environment_definition['name'] == "enumerate"
            assert retrieved_enum._environment_definition['syntax'] == "\\begin{enumerate}[label]"
            assert retrieved_enum._environment_definition['environment_type'] == EnvironmentType.UNKNOWN
            assert retrieved_enum._environment_definition['robustness'] == EnvironmentRobustness.ROBUST
            
            retrieved_multi = new_registry.get_entry("multline")
            assert retrieved_multi._environment_definition['environment_type'] == EnvironmentType.MATH_DISPLAY
            assert retrieved_multi._environment_definition['robustness'] == EnvironmentRobustness.FRAGILE
            
        finally:
            # Clean up
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)

    def test_validate_all_entries(self):
        """Test validating all entries in registry."""
        registry = EnvironmentDefinitionRegistry()
        
        # Add valid environment
        valid_env = EnvironmentDefinition(
            name="description",
            syntax="\\begin{description}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Description list environment",
            references=[]
        )
        
        registry.add_entry("description", valid_env)
        
        # Validate all entries
        validation_results = registry.validate_all_entries()
        assert isinstance(validation_results, dict)
        assert "description" in validation_results
        assert validation_results["description"] is True

    def test_inheritance_from_registry(self):
        """Test that EnvironmentDefinitionRegistry properly inherits from Registry."""
        registry = EnvironmentDefinitionRegistry()
        assert isinstance(registry, Registry)
        assert issubclass(EnvironmentDefinitionRegistry, Registry)

    def test_type_enforcement(self):
        """Test that registry enforces EnvironmentDefinition type."""
        registry = EnvironmentDefinitionRegistry()
        
        # This should work
        valid_env = EnvironmentDefinition(
            name="quote",
            syntax="\\begin{quote}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Quote environment",
            references=[]
        )
        
        registry.add_entry("quote", valid_env)
        assert registry.is_key_present("quote")

    def test_different_environment_types(self):
        """Test registry with different environment types."""
        registry = EnvironmentDefinitionRegistry()
        
        # Math environment
        math_env = EnvironmentDefinition(
            name="equation*",
            syntax="\\begin{equation*}",
            environment_type=EnvironmentType.MATH_DISPLAY,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Unnumbered equation environment",
            references=[]
        )
        
        # Text environment
        text_env = EnvironmentDefinition(
            name="flushleft",
            syntax="\\begin{flushleft}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Left-aligned text environment",
            references=[]
        )
        
        registry.add_entry("equation*", math_env)
        registry.add_entry("flushleft", text_env)
        
        # Verify they're stored correctly
        retrieved_math = registry.get_entry("equation*")
        retrieved_text = registry.get_entry("flushleft")
        
        assert retrieved_math._environment_definition['environment_type'] == EnvironmentType.MATH_DISPLAY
        assert retrieved_math._environment_definition['robustness'] == EnvironmentRobustness.FRAGILE
        
        assert retrieved_text._environment_definition['environment_type'] == EnvironmentType.UNKNOWN
        assert retrieved_text._environment_definition['robustness'] == EnvironmentRobustness.ROBUST

    def test_multiple_modes(self):
        """Test environment with multiple valid modes."""
        registry = EnvironmentDefinitionRegistry()
        
        # Environment valid in multiple modes
        multi_mode_env = EnvironmentDefinition(
            name="minipage",
            syntax="\\begin{minipage}[pos][height][inner-pos]{width}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH, EnvironmentMode.UNKNOWN],
            description="Minipage environment for boxes",
            references=[{'ref_id': 'lamport_1994', 'sections': '4.7', 'pages': '89-91'}]
        )
        
        registry.add_entry("minipage", multi_mode_env)
        retrieved = registry.get_entry("minipage")
        
        assert len(retrieved._environment_definition['modes']) == 2
        assert EnvironmentMode.PARAGRAPH in retrieved._environment_definition['modes']
        assert EnvironmentMode.UNKNOWN in retrieved._environment_definition['modes']

    def test_empty_references_list(self):
        """Test environment with empty references list."""
        registry = EnvironmentDefinitionRegistry()
        
        env_def = EnvironmentDefinition(
            name="abstract",
            syntax="\\begin{abstract}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Abstract environment",
            references=[]  # Empty references
        )
        
        registry.add_entry("abstract", env_def)
        retrieved = registry.get_entry("abstract")
        
        assert retrieved._environment_definition['references'] == []

    def test_complex_syntax_with_multiple_arguments(self):
        """Test environment with complex syntax containing multiple arguments."""
        registry = EnvironmentDefinitionRegistry()
        
        complex_env = EnvironmentDefinition(
            name="tabular",
            syntax="\\begin{tabular}[pos]{cols}",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.ROBUST,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Tabular environment for tables",
            references=[
                {'ref_id': 'lamport_1994', 'sections': '3.6', 'pages': '62-70'},
                {'ref_id': 'companion', 'sections': '5.1', 'pages': '245-250'}
            ]
        )
        
        registry.add_entry("tabular", complex_env)
        retrieved = registry.get_entry("tabular")
        
        assert "pos" in retrieved._environment_definition['syntax']
        assert "cols" in retrieved._environment_definition['syntax']
        assert len(retrieved._environment_definition['references']) == 2

    def test_registry_consistency_after_operations(self):
        """Test that registry maintains consistency after multiple operations."""
        registry = EnvironmentDefinitionRegistry()
        
        # Add multiple environments
        environments = [
            ("equation", EnvironmentType.MATH_DISPLAY, EnvironmentRobustness.FRAGILE),
            ("itemize", EnvironmentType.UNKNOWN, EnvironmentRobustness.ROBUST),
            ("verbatim", EnvironmentType.UNKNOWN, EnvironmentRobustness.FRAGILE),
            ("center", EnvironmentType.UNKNOWN, EnvironmentRobustness.ROBUST)
        ]
        
        for name, env_type, robustness in environments:
            env_def = EnvironmentDefinition(
                name=name,
                syntax=f"\\begin{{{name}}}",
                environment_type=env_type,
                robustness=robustness,
                modes=[EnvironmentMode.PARAGRAPH],
                description=f"{name.capitalize()} environment",
                references=[]
            )
            registry.add_entry(name, env_def)
        
        # Verify all are present
        assert len(registry.list_keys()) == 4
        
        # Delete one
        registry.delete_entry("verbatim")
        assert len(registry.list_keys()) == 3
        assert not registry.is_key_present("verbatim")
        
        # Update one
        updated_env = EnvironmentDefinition(
            name="equation",
            syntax="\\begin{equation}[placement]",
            environment_type=EnvironmentType.MATH_DISPLAY,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Updated equation environment",
            references=[{'ref_id': 'amsmath', 'sections': '2.1', 'pages': '8-10'}]
        )
        registry.update_entry("equation", updated_env)
        
        # Verify update
        retrieved = registry.get_entry("equation")
        assert "placement" in retrieved._environment_definition['syntax']
        assert "Updated" in retrieved._environment_definition['description']
        
        # Verify others unchanged
        itemize_env = registry.get_entry("itemize")
        assert itemize_env._environment_definition['robustness'] == EnvironmentRobustness.ROBUST

    def test_error_handling_edge_cases(self):
        """Test error handling for various edge cases."""
        registry = EnvironmentDefinitionRegistry()
        
        # Test with empty string key
        env_def = EnvironmentDefinition(
            name="",
            syntax="",
            environment_type=EnvironmentType.UNKNOWN,
            robustness=EnvironmentRobustness.UNKNOWN,
            modes=[],
            description="",
            references=[]
        )
        
        # This should work - empty strings are valid
        registry.add_entry("", env_def)
        assert registry.is_key_present("")
        
        # Test retrieving with empty key
        retrieved = registry.get_entry("")
        assert retrieved._environment_definition['name'] == ""

    def test_registry_with_special_characters_in_names(self):
        """Test registry handles environment names with special characters."""
        registry = EnvironmentDefinitionRegistry()
        
        # Environment with asterisk (common in LaTeX)
        starred_env = EnvironmentDefinition(
            name="equation*",
            syntax="\\begin{equation*}",
            environment_type=EnvironmentType.MATH_DISPLAY,
            robustness=EnvironmentRobustness.FRAGILE,
            modes=[EnvironmentMode.PARAGRAPH],
            description="Unnumbered equation",
            references=[]
        )
        
        registry.add_entry("equation*", starred_env)
        assert registry.is_key_present("equation*")
        
        retrieved = registry.get_entry("equation*")
        assert retrieved._environment_definition['name'] == "equation*"