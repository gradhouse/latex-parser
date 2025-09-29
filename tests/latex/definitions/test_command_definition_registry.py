# File: test_command_definition_registry.py
# Description: Unit tests for the CommandDefinitionRegistry class
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import json
import os
import tempfile
from typing import Type
import pytest

from latex_parser.latex.definitions.command_definition_registry import CommandDefinitionRegistry
from latex_parser.latex.definitions.command_definition import CommandDefinition, CommandMode, CommandRobustness, CommandType


class TestCommandDefinitionRegistryBasicBehavior:
    """Test basic behavior of CommandDefinitionRegistry."""
    
    def test_registry_creation(self):
        """CommandDefinitionRegistry can be created successfully."""
        registry = CommandDefinitionRegistry()
        
        assert registry.get_entry_type() == CommandDefinition
        assert len(registry) == 0
    
    def test_get_entry_type_returns_command_definition(self):
        """get_entry_type returns CommandDefinition class."""
        assert CommandDefinitionRegistry.get_entry_type() == CommandDefinition
    
    def test_for_type_raises_type_error(self):
        """for_type method raises TypeError to prevent specialization."""
        with pytest.raises(TypeError, match="CommandDefinitionRegistry can only store CommandDefinition objects"):
            CommandDefinitionRegistry.for_type(str)
    
    def test_initialization_with_enforce_constraints_true(self):
        """Registry is initialized with enforce_constraints=True by default."""
        registry = CommandDefinitionRegistry()
        assert registry._enforce_constraints is True


class TestCommandDefinitionRegistryOperations:
    """Test CRUD operations with CommandDefinition objects."""
    
    def create_sample_command_definition(self, name="\\textbf") -> CommandDefinition:
        """Helper method to create a sample CommandDefinition."""
        return CommandDefinition(
            name=name,
            syntax=f"{name}{{text}}",
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.ROBUST,
            modes=[CommandMode.PARAGRAPH],
            description=f"Makes text bold using {name}",
            references=[{"ref_id": "latex2e", "sections": "3.1", "pages": "45"}]
        )
    
    def test_add_command_definition(self):
        """Can add a CommandDefinition to the registry."""
        registry = CommandDefinitionRegistry()
        cmd_def = self.create_sample_command_definition()
        
        registry.add_entry("\\textbf", cmd_def)
        
        assert len(registry) == 1
        assert registry.is_key_present("\\textbf")
        
        retrieved = registry.get_entry("\\textbf")
        assert retrieved.as_dict() == cmd_def.as_dict()
    
    def test_add_multiple_command_definitions(self):
        """Can add multiple CommandDefinitions to the registry."""
        registry = CommandDefinitionRegistry()
        
        cmd1 = self.create_sample_command_definition("\\textbf")
        cmd2 = self.create_sample_command_definition("\\textit")
        
        registry.add_entry("\\textbf", cmd1)
        registry.add_entry("\\textit", cmd2)
        
        assert len(registry) == 2
        assert set(registry.list_keys()) == {"\\textbf", "\\textit"}
    
    def test_update_command_definition(self):
        """Can update an existing CommandDefinition."""
        registry = CommandDefinitionRegistry()
        original_cmd = self.create_sample_command_definition()
        registry.add_entry("\\textbf", original_cmd)
        
        # Create updated version
        updated_cmd = CommandDefinition(
            name="\\textbf",
            syntax="\\textbf{text}",
            command_type=CommandType.SECTIONING,  # Changed
            robustness=CommandRobustness.FRAGILE,  # Changed
            modes=[CommandMode.MATH],  # Changed
            description="Updated description",  # Changed
            references=[{"ref_id": "updated", "sections": "4.2", "pages": "99"}]  # Changed
        )
        
        registry.update_entry("\\textbf", updated_cmd)
        
        retrieved = registry.get_entry("\\textbf")
        assert retrieved.as_dict() == updated_cmd.as_dict()
        assert retrieved.as_dict() != original_cmd.as_dict()
    
    def test_delete_command_definition(self):
        """Can delete a CommandDefinition from the registry."""
        registry = CommandDefinitionRegistry()
        cmd_def = self.create_sample_command_definition()
        registry.add_entry("\\textbf", cmd_def)
        
        registry.delete_entry("\\textbf")
        
        assert len(registry) == 0
        assert not registry.is_key_present("\\textbf")
        
        with pytest.raises(KeyError):
            registry.get_entry("\\textbf")
    
    def test_clear_registry(self):
        """Can clear all CommandDefinitions from the registry."""
        registry = CommandDefinitionRegistry()
        
        registry.add_entry("\\textbf", self.create_sample_command_definition("\\textbf"))
        registry.add_entry("\\textit", self.create_sample_command_definition("\\textit"))
        
        registry.clear()
        
        assert len(registry) == 0
        assert registry.list_keys() == []


class TestCommandDefinitionRegistryErrorHandling:
    """Test error handling in CommandDefinitionRegistry."""
    
    def test_add_duplicate_key_raises_error(self):
        """Adding a duplicate key raises KeyError."""
        registry = CommandDefinitionRegistry()
        cmd_def = CommandDefinition(
            name="\\textbf",
            syntax="\\textbf{text}",
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.ROBUST,
            modes=[CommandMode.PARAGRAPH],
            description="Bold text",
            references=[]
        )
        
        registry.add_entry("\\textbf", cmd_def)
        
        with pytest.raises(KeyError, match="Hash key '\\\\\\\\textbf' already exists in registry"):
            registry.add_entry("\\textbf", cmd_def)
    
    def test_get_missing_key_raises_error(self):
        """Getting a missing key raises KeyError."""
        registry = CommandDefinitionRegistry()
        
        with pytest.raises(KeyError, match="Hash key '\\\\\\\\missing' not found in registry"):
            registry.get_entry("\\missing")
    
    def test_update_missing_key_raises_error(self):
        """Updating a missing key raises KeyError."""
        registry = CommandDefinitionRegistry()
        cmd_def = CommandDefinition(
            name="\\textbf",
            syntax="\\textbf{text}",
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.ROBUST,
            modes=[CommandMode.PARAGRAPH],
            description="Bold text",
            references=[]
        )
        
        with pytest.raises(KeyError, match="Hash key '\\\\\\\\missing' not found in registry"):
            registry.update_entry("\\missing", cmd_def)
    
    def test_delete_missing_key_raises_error(self):
        """Deleting a missing key raises KeyError."""
        registry = CommandDefinitionRegistry()
        
        with pytest.raises(KeyError, match="Hash key '\\\\\\\\missing' not found in registry"):
            registry.delete_entry("\\missing")


class TestCommandDefinitionRegistrySerialization:
    """Test JSON serialization and deserialization."""
    
    def create_complex_command_definition(self) -> CommandDefinition:
        """Helper to create a complex CommandDefinition for testing."""
        return CommandDefinition(
            name="\\documentclass",
            syntax="\\documentclass[options]{class}",
            command_type=CommandType.SECTIONING,
            robustness=CommandRobustness.ROBUST,
            modes=[CommandMode.PREAMBLE, CommandMode.PARAGRAPH],
            description="Declares the document class",
            references=[
                {"ref_id": "latex2e", "sections": "2.1", "pages": "12-15"},
                {"ref_id": "companion", "sections": "4.3", "pages": "89"}
            ]
        )
    
    def test_save_and_load_registry(self):
        """Can save and load registry to/from JSON file."""
        registry = CommandDefinitionRegistry()
        
        cmd1 = self.create_complex_command_definition()
        cmd2 = CommandDefinition(
            name="\\textbf",
            syntax="\\textbf{text}",
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.FRAGILE,
            modes=[CommandMode.MATH, CommandMode.PARAGRAPH],
            description="Bold text formatting",
            references=[]
        )
        
        registry.add_entry("\\documentclass", cmd1)
        registry.add_entry("\\textbf", cmd2)
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            temp_path = tmp_file.name
        
        try:
            # Save registry
            registry.save_to_json(temp_path)
            
            # Load into new registry
            new_registry = CommandDefinitionRegistry()
            new_registry.load_from_json(temp_path)
            
            # Verify contents
            assert len(new_registry) == 2
            assert set(new_registry.list_keys()) == {"\\documentclass", "\\textbf"}
            
            loaded_cmd1 = new_registry.get_entry("\\documentclass")
            loaded_cmd2 = new_registry.get_entry("\\textbf")
            
            assert loaded_cmd1.as_dict() == cmd1.as_dict()
            assert loaded_cmd2.as_dict() == cmd2.as_dict()
            
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_save_empty_registry(self):
        """Can save and load an empty registry."""
        registry = CommandDefinitionRegistry()
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            temp_path = tmp_file.name
        
        try:
            registry.save_to_json(temp_path)
            
            new_registry = CommandDefinitionRegistry()
            new_registry.load_from_json(temp_path)
            
            assert len(new_registry) == 0
            
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_initialization_with_file_path(self):
        """Can initialize registry with a file path."""
        # Create and save a registry
        registry = CommandDefinitionRegistry()
        cmd_def = self.create_complex_command_definition()
        registry.add_entry("\\documentclass", cmd_def)
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            temp_path = tmp_file.name
        
        try:
            registry.save_to_json(temp_path)
            
            # Initialize new registry with file path
            loaded_registry = CommandDefinitionRegistry(file_path=temp_path)
            
            assert len(loaded_registry) == 1
            assert loaded_registry.is_key_present("\\documentclass")
            
            loaded_cmd = loaded_registry.get_entry("\\documentclass")
            assert loaded_cmd.as_dict() == cmd_def.as_dict()
            
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_load_nonexistent_file_raises_error(self):
        """Loading from nonexistent file raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            CommandDefinitionRegistry(file_path="/nonexistent/path.json")
    
    def test_load_invalid_json_format_raises_error(self):
        """Loading invalid JSON format raises ValueError."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            json.dump({"invalid": "format"}, tmp_file)
            temp_path = tmp_file.name
        
        try:
            with pytest.raises(ValueError, match="Invalid registry file format"):
                CommandDefinitionRegistry(file_path=temp_path)
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_load_wrong_registry_type_raises_error(self):
        """Loading file with wrong registry type raises ValueError."""
        # Create a file with wrong registry type
        wrong_data = {
            "metadata": {
                "registry_type": "str",
                "registry_module": "builtins"
            },
            "entries": {"key": "value"}
        }
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            json.dump(wrong_data, tmp_file)
            temp_path = tmp_file.name
        
        try:
            with pytest.raises(ValueError, match="Registry type mismatch"):
                CommandDefinitionRegistry(file_path=temp_path)
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)


class TestCommandDefinitionRegistryValidation:
    """Test validation methods."""
    
    def test_validate_all_entries(self):
        """validate_all_entries returns True for valid CommandDefinitions."""
        registry = CommandDefinitionRegistry()
        
        cmd1 = CommandDefinition(
            name="\\textbf",
            syntax="\\textbf{text}",
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.ROBUST,
            modes=[CommandMode.PARAGRAPH],
            description="Bold text",
            references=[]
        )
        
        cmd2 = CommandDefinition(
            name="\\textit",
            syntax="\\textit{text}",
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.FRAGILE,
            modes=[CommandMode.PARAGRAPH, CommandMode.MATH],
            description="Italic text",
            references=[{"ref_id": "test", "sections": "1", "pages": "1"}]
        )
        
        registry.add_entry("\\textbf", cmd1)
        registry.add_entry("\\textit", cmd2)
        
        validation_results = registry.validate_all_entries()
        
        assert validation_results == {"\\textbf": True, "\\textit": True}


class TestCommandDefinitionRegistryEdgeCases:
    """Test edge cases and special scenarios."""
    
    def test_deep_copy_behavior(self):
        """Registry creates deep copies to prevent external modifications."""
        registry = CommandDefinitionRegistry()
        
        original_cmd = CommandDefinition(
            name="\\test",
            syntax="\\test{text}",
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.ROBUST,
            modes=[CommandMode.PARAGRAPH],
            description="Test command",
            references=[{"ref_id": "test", "sections": "1", "pages": "1"}]
        )
        
        registry.add_entry("\\test", original_cmd)
        
        # Get the command and modify the original
        retrieved_cmd = registry.get_entry("\\test")
        original_dict = original_cmd.as_dict()
        original_dict["description"] = "Modified description"
        
        # Retrieved command should be unaffected
        assert retrieved_cmd.as_dict()["description"] == "Test command"
    
    def test_key_with_special_characters(self):
        """Can handle keys with special characters."""
        registry = CommandDefinitionRegistry()
        
        # Test various special command names
        special_keys = ["\\@startsection", "\\c@section", "\\p@enumii"]
        
        for key in special_keys:
            cmd_def = CommandDefinition(
                name=key,
                syntax=f"{key}{{args}}",
                command_type=CommandType.UNKNOWN,
                robustness=CommandRobustness.UNKNOWN,
                modes=[CommandMode.UNKNOWN],
                description=f"Special command {key}",
                references=[]
            )
            
            registry.add_entry(key, cmd_def)
        
        assert len(registry) == len(special_keys)
        for key in special_keys:
            assert registry.is_key_present(key)
            retrieved = registry.get_entry(key)
            assert retrieved.as_dict()["name"] == key
    
    def test_command_definition_with_empty_references(self):
        """Can handle CommandDefinitions with empty references list."""
        registry = CommandDefinitionRegistry()
        
        cmd_def = CommandDefinition(
            name="\\test",
            syntax="\\test",
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.UNKNOWN,
            modes=[],
            description="",
            references=[]
        )
        
        registry.add_entry("\\test", cmd_def)
        
        retrieved = registry.get_entry("\\test")
        assert retrieved.as_dict()["references"] == []
        assert retrieved.as_dict()["modes"] == []
    
    def test_command_definition_with_all_enum_values(self):
        """Can handle CommandDefinitions with all possible enum values."""
        registry = CommandDefinitionRegistry()
        
        # Test all CommandType values
        for cmd_type in CommandType:
            cmd_def = CommandDefinition(
                name=f"\\test_{cmd_type.value}",
                syntax=f"\\test_{cmd_type.value}",
                command_type=cmd_type,
                robustness=CommandRobustness.UNKNOWN,
                modes=[CommandMode.UNKNOWN],
                description=f"Test for {cmd_type.value}",
                references=[]
            )
            registry.add_entry(f"\\test_{cmd_type.value}", cmd_def)
        
        # Test all CommandRobustness values
        for robustness in CommandRobustness:
            cmd_def = CommandDefinition(
                name=f"\\robust_{robustness.value}",
                syntax=f"\\robust_{robustness.value}",
                command_type=CommandType.UNKNOWN,
                robustness=robustness,
                modes=[CommandMode.UNKNOWN],
                description=f"Test for {robustness.value}",
                references=[]
            )
            registry.add_entry(f"\\robust_{robustness.value}", cmd_def)
        
        # Test all CommandMode values
        for mode in CommandMode:
            cmd_def = CommandDefinition(
                name=f"\\mode_{mode.value}",
                syntax=f"\\mode_{mode.value}",
                command_type=CommandType.UNKNOWN,
                robustness=CommandRobustness.UNKNOWN,
                modes=[mode],
                description=f"Test for {mode.value}",
                references=[]
            )
            registry.add_entry(f"\\mode_{mode.value}", cmd_def)
        
        total_expected = len(CommandType) + len(CommandRobustness) + len(CommandMode)
        assert len(registry) == total_expected
    
    def test_large_registry_performance(self):
        """Can handle a reasonably large number of entries."""
        registry = CommandDefinitionRegistry()
        
        # Add 100 command definitions
        for i in range(100):
            cmd_def = CommandDefinition(
                name=f"\\testcmd{i:03d}",
                syntax=f"\\testcmd{i:03d}{{arg}}",
                command_type=CommandType.UNKNOWN,
                robustness=CommandRobustness.ROBUST,
                modes=[CommandMode.PARAGRAPH],
                description=f"Test command number {i}",
                references=[{"ref_id": f"ref{i}", "sections": str(i), "pages": str(i)}]
            )
            registry.add_entry(f"\\testcmd{i:03d}", cmd_def)
        
        assert len(registry) == 100
        
        # Test that we can retrieve all entries
        for i in range(100):
            key = f"\\testcmd{i:03d}"
            assert registry.is_key_present(key)
            cmd = registry.get_entry(key)
            assert cmd.as_dict()["name"] == key
        
        # Test list_keys returns all keys
        keys = registry.list_keys()
        assert len(keys) == 100
        assert all(f"\\testcmd{i:03d}" in keys for i in range(100))