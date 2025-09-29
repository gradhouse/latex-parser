"""
Tests for the simplified typed-only Registry class.

This test suite focuses on the core functionality without mixed-type or legacy support.
"""

import json
import os
import tempfile
from typing import Dict, Any, Optional, Type
import pytest

from latex_parser.services.registry import Registry


class MockSerializableClass:
    """Mock class that supports JSON serialization via as_dict/from_dict."""
    
    def __init__(self, value: str, metadata: Optional[Dict[str, Any]] = None):
        self.value = value
        self.metadata = metadata or {}
    
    def as_dict(self) -> Dict[str, Any]:
        return {"value": self.value, "metadata": self.metadata}
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'MockSerializableClass':
        return cls(data["value"], data.get("metadata", {}))
    
    def __eq__(self, other):
        return (isinstance(other, MockSerializableClass) and 
                self.value == other.value and 
                self.metadata == other.metadata)
    
    def __repr__(self):
        return f"MockSerializableClass(value='{self.value}', metadata={self.metadata})"


class MockNonSerializableClass:
    """Mock class that does NOT support JSON serialization."""
    
    def __init__(self, name: str):
        self.name = name
    
    def __repr__(self):
        return f"MockNonSerializableClass(name='{self.name}')"


# Concrete registry implementations for testing
class StringRegistry(Registry[str]):
    @classmethod
    def get_entry_type(cls) -> Type[str]:
        return str


class MockRegistry(Registry[MockSerializableClass]):
    @classmethod
    def get_entry_type(cls) -> Type[MockSerializableClass]:
        return MockSerializableClass


class TestRegistryAbstractBehavior:
    """Test abstract base class behavior."""
    
    def test_cannot_instantiate_abstract_registry(self):
        """Registry is abstract and cannot be instantiated directly."""
        with pytest.raises(TypeError, match="Can't instantiate abstract class Registry"):
            Registry() # type: ignore # We're intentionally calling an abstract method

    def test_get_entry_type_abstract_method_raises(self):
        """The abstract get_entry_type method raises NotImplementedError when called directly."""
        # We need to access the class method directly without instantiation
        with pytest.raises(NotImplementedError, match="Concrete subclasses must implement get_entry_type"):
            Registry.get_entry_type()  # type: ignore # We're intentionally calling an abstract method


class TestConcreteRegistryImplementations:
    """Test concrete registry implementations."""
    
    def test_string_registry_creation(self):
        """StringRegistry can be created and configured correctly."""
        registry = StringRegistry()
        
        assert registry.get_entry_type() == str
        assert len(registry) == 0
    
    def test_mock_registry_creation(self):
        """MockRegistry can be created and configured correctly."""
        registry = MockRegistry()
        
        assert registry.get_entry_type() == MockSerializableClass
        assert len(registry) == 0
    
    def test_string_registry_add_valid_entry(self):
        """StringRegistry accepts string entries."""
        registry = StringRegistry()
        
        registry.add_entry("test", "hello world")
        assert registry.get_entry("test") == "hello world"
        
    def test_mock_registry_add_valid_entry(self):
        """MockRegistry accepts MockSerializableClass entries."""
        registry = MockRegistry()
        obj = MockSerializableClass("test", {"key": "value"})
        
        registry.add_entry("test", obj)
        retrieved = registry.get_entry("test")
        
        assert retrieved == obj
        assert retrieved.value == "test"
        assert retrieved.metadata == {"key": "value"}


class TestRegistryFactoryMethods:
    """Test factory methods for creating registries."""
    
    def test_for_type_with_json_serializable_type(self):
        """Registry.for_type works with basic JSON types."""
        StringRegistry = Registry.for_type(str)
        registry = StringRegistry()
        
        assert registry.get_entry_type() == str
        registry.add_entry("test", "hello")
        assert registry.get_entry("test") == "hello"
    
    def test_for_type_with_serializable_class(self):
        """Registry.for_type works with custom serializable classes."""
        MockRegistry = Registry.for_type(MockSerializableClass)
        registry = MockRegistry()
        
        assert registry.get_entry_type() == MockSerializableClass
        obj = MockSerializableClass("test")
        registry.add_entry("test", obj)
        assert registry.get_entry("test") == obj
    
    def test_for_type_rejects_non_serializable_class(self):
        """Registry.for_type rejects non-serializable classes."""
        with pytest.raises(TypeError, match="Entry type .* is not allowed in Registry"):
            Registry.for_type(MockNonSerializableClass)


class TestRegistryBasicOperations:
    """Test basic CRUD operations."""
    
    def test_add_entry_duplicate_key(self):
        """Adding duplicate key raises KeyError."""
        registry = StringRegistry()
        registry.add_entry("test", "first")
        
        with pytest.raises(KeyError, match="Hash key 'test' already exists"):
            registry.add_entry("test", "second")
    
    def test_get_entry_missing_key(self):
        """Getting missing key raises KeyError."""
        registry = StringRegistry()
        
        with pytest.raises(KeyError, match="Hash key 'missing' not found"):
            registry.get_entry("missing")
    
    def test_update_entry(self):
        """Updating existing entry works correctly."""
        registry = StringRegistry()
        registry.add_entry("test", "original")
        
        registry.update_entry("test", "updated")
        assert registry.get_entry("test") == "updated"
    
    def test_update_entry_missing_key(self):
        """Updating missing key raises KeyError."""
        registry = StringRegistry()
        
        with pytest.raises(KeyError, match="Hash key 'missing' not found"):
            registry.update_entry("missing", "value")
    
    def test_delete_entry(self):
        """Deleting entry works correctly."""
        registry = StringRegistry()
        registry.add_entry("test", "value")
        
        registry.delete_entry("test")
        assert len(registry) == 0
        
        with pytest.raises(KeyError):
            registry.get_entry("test")
    
    def test_delete_entry_missing_key(self):
        """Deleting missing key raises KeyError."""
        registry = StringRegistry()
        
        with pytest.raises(KeyError, match="Hash key 'missing' not found"):
            registry.delete_entry("missing")
    
    def test_clear(self):
        """Clear removes all entries."""
        registry = StringRegistry()
        registry.add_entry("test1", "value1")
        registry.add_entry("test2", "value2")
        
        registry.clear()
        assert len(registry) == 0
        assert list(registry.list_keys()) == []
    
    def test_list_keys(self):
        """list_keys returns all keys."""
        registry = StringRegistry()
        registry.add_entry("key1", "value1")
        registry.add_entry("key2", "value2")
        
        keys = list(registry.list_keys())
        assert set(keys) == {"key1", "key2"}
        
    def test_is_key_present(self):
        """is_key_present correctly identifies if a key exists."""
        registry = StringRegistry()
        registry.add_entry("existing", "value")
        
        # Test for existing key
        assert registry.is_key_present("existing") is True
        
        # Test for non-existing key
        assert registry.is_key_present("nonexistent") is False


class TestConstraintEnforcement:
    """Test JSON serialization constraint enforcement."""
    
    def test_constraint_enforcement_enabled_by_default(self):
        """Constraint enforcement is enabled by default."""
        registry = StringRegistry()
        assert registry._enforce_constraints is True
    
    def test_disable_constraint_enforcement(self):
        """Constraint enforcement can be disabled."""
        registry = StringRegistry(enforce_constraints=False)
        assert registry._enforce_constraints is False
    
    def test_serialization_constraint_in_add_entry(self):
        """add_entry enforces serialization constraints."""
        registry = MockRegistry()
        
        # This should work - MockSerializableClass has as_dict/from_dict
        obj = MockSerializableClass("test")
        registry.add_entry("valid", obj)
        
        # This should fail - MockNonSerializableClass lacks serialization methods
        non_serializable = MockNonSerializableClass("bad")
        with pytest.raises(TypeError, match="Entry is not JSON-serializable"):
            # We have to bypass type checking to test this
            registry._registry["bad"] = non_serializable  # type: ignore # Testing error path
            registry.add_entry("invalid", non_serializable)  # type: ignore # Testing error path
    
    def test_serialization_constraint_in_update_entry(self):
        """update_entry enforces serialization constraints."""
        registry = MockRegistry()
        registry.add_entry("test", MockSerializableClass("original"))
        
        # This should work
        new_obj = MockSerializableClass("updated")
        registry.update_entry("test", new_obj)
        
        # This should fail - non-serializable
        non_serializable = MockNonSerializableClass("bad")
        with pytest.raises(TypeError, match="Entry is not JSON-serializable"):
            # Bypass type checking to test constraint enforcement
            registry.update_entry("test", non_serializable)  # type: ignore # Testing error path


class TestTypeValidation:
    """Test type validation methods."""
    
    def test_is_type_allowed_with_basic_types(self):
        """is_type_allowed accepts basic JSON types."""
        assert Registry._is_type_allowed(str)
        assert Registry._is_type_allowed(int)
        assert Registry._is_type_allowed(float)
        assert Registry._is_type_allowed(bool)
        assert Registry._is_type_allowed(dict)
        assert Registry._is_type_allowed(list)
        assert Registry._is_type_allowed(type(None))
    
    def test_is_type_allowed_with_instances(self):
        """is_type_allowed works with instances too."""
        assert Registry._is_type_allowed("hello")
        assert Registry._is_type_allowed(42)
        assert Registry._is_type_allowed({"key": "value"})
        assert Registry._is_type_allowed([1, 2, 3])
    
    def test_is_type_allowed_with_serializable_class(self):
        """is_type_allowed accepts classes with as_dict/from_dict."""
        assert Registry._is_type_allowed(MockSerializableClass)
        
        obj = MockSerializableClass("test")
        assert Registry._is_type_allowed(obj)
    
    def test_is_type_allowed_rejects_non_serializable(self):
        """is_type_allowed rejects classes without serialization methods."""
        assert not Registry._is_type_allowed(MockNonSerializableClass)
        
        obj = MockNonSerializableClass("test")
        assert not Registry._is_type_allowed(obj)
    
    def test_validate_all_entries(self):
        """validate_all_entries checks all entries."""
        registry = StringRegistry()
        registry.add_entry("valid1", "hello")
        registry.add_entry("valid2", "world")
        
        # All entries should be valid
        result = registry.validate_all_entries()
        assert result == {"valid1": True, "valid2": True}


class TestSaveLoadFunctionality:
    """Test save and load functionality."""
    
    def test_save_and_load_typed_registry(self):
        """Save and load works for typed registries."""
        registry = MockRegistry()
        obj1 = MockSerializableClass("test1", {"key1": "value1"})
        obj2 = MockSerializableClass("test2", {"key2": "value2"})
        
        registry.add_entry("obj1", obj1)
        registry.add_entry("obj2", obj2)
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            temp_path = tmp_file.name
        
        try:
            # Save
            registry.save_to_json(temp_path)
            
            # Load into new registry
            new_registry = MockRegistry()
            new_registry.load_from_json(temp_path)

            # Verify
            assert len(new_registry) == 2
            assert new_registry.get_entry("obj1") == obj1
            assert new_registry.get_entry("obj2") == obj2
            
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_save_basic_json_types(self):
        """Save and load works for basic JSON types."""
        registry = StringRegistry()
        registry.add_entry("str1", "hello")
        registry.add_entry("str2", "world")
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            temp_path = tmp_file.name
        
        try:
            # Save
            registry.save_to_json(temp_path)
            
            # Load into new registry
            new_registry = StringRegistry()
            new_registry.load_from_json(temp_path)

            # Verify
            assert len(new_registry) == 2
            assert new_registry.get_entry("str1") == "hello"
            assert new_registry.get_entry("str2") == "world"
            
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_load_file_not_found(self):
        """Loading non-existent file raises FileNotFoundError."""
        registry = StringRegistry()
        
        with pytest.raises(FileNotFoundError, match="File '/nonexistent/path.json' not found"):
            registry.load_from_json("/nonexistent/path.json")
    
    def test_load_invalid_format(self):
        """Loading invalid format raises ValueError."""
        registry = StringRegistry()
        
        # Create invalid JSON file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            json.dump({"invalid": "format"}, tmp_file)  # Missing required fields
            temp_path = tmp_file.name
        
        try:
            with pytest.raises(ValueError, match="Invalid registry file format"):
                registry.load_from_json(temp_path)
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_load_type_mismatch(self):
        """Loading registry with wrong type raises ValueError."""
        # Create file for MockSerializableClass registry
        mock_registry = MockRegistry()
        mock_registry.add_entry("test", MockSerializableClass("test"))
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            temp_path = tmp_file.name
        
        try:
            mock_registry.save_to_json(temp_path)
            
            # Try to load into StringRegistry (type mismatch)
            string_registry = StringRegistry()
            with pytest.raises(ValueError, match="Registry type mismatch"):
                string_registry.load_from_json(temp_path)
                
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)


class TestRegistryWithFileSystem:
    """Test registry initialization with file paths."""
    
    def test_init_with_file_path(self):
        """Registry can be initialized with a file to load."""
        # Create a registry file first
        registry = StringRegistry()
        registry.add_entry("test", "value")
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            temp_path = tmp_file.name
        
        try:
            registry.save_to_json(temp_path)
            
            # Create new registry loading from file
            new_registry = StringRegistry(file_path=temp_path)
            
            assert len(new_registry) == 1
            assert new_registry.get_entry("test") == "value"
            
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)


class TestEdgeCases:
    """Test edge cases and error conditions."""
        
    def test_class_equality_fallback_type_check(self):
        """Test the class equality fallback in type validation."""
        # Create a subclass that will trigger the secondary type check
        class SubMockSerializable(MockSerializableClass):
            pass
        
        registry = MockRegistry()
        
        # This should trigger the class equality check on lines 202-205, 227-228
        obj = SubMockSerializable("test", {"key": "value"})
        registry.add_entry("test", obj)
        
        # Now test update_entry which has the same check
        new_obj = SubMockSerializable("updated", {"new": "data"})
        registry.update_entry("test", new_obj)
        
        assert len(registry) == 1
    
    def test_save_non_serializable_entry_error(self):
        """Test save method with non-serializable entry (line 350)."""
        registry = MockRegistry(enforce_constraints=False)  # Disable constraints
        
        # Manually add a non-serializable entry by bypassing validation
        class NonSerializable:
            def __init__(self):
                self.data = "test"
                # No as_dict method
        
        # This is a bit of a hack to test the error path
        registry._registry["bad"] = NonSerializable()  # type: ignore # Testing error path
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            temp_path = tmp_file.name
        
        try:
            # This should trigger the TypeError on line 350
            with pytest.raises(TypeError, match="Entry for key 'bad' is not JSON-serializable"):
                registry.save_to_json(temp_path)
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_load_invalid_metadata_format(self):
        """Test loading file with invalid metadata format (lines 289-294)."""
        # Create file with missing registry_type in metadata
        invalid_data = {
            "metadata": {
                "registry_module": "builtins"
                # Missing registry_type
            },
            "entries": {"key1": "value1"}
        }
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            json.dump(invalid_data, tmp_file)
            temp_path = tmp_file.name
        
        try:
            registry = StringRegistry()
            with pytest.raises(ValueError, match="Invalid registry metadata format"):
                registry.load_from_json(temp_path)
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_load_with_basic_json_entries_mixed_with_dicts(self):
        """Test loading when entries contain both dicts and basic types (line 322)."""
        # Create a custom class registry with mixed entry types
        typed_data = {
            "metadata": {
                "registry_type": "MockSerializableClass",
                "registry_module": "test_registry"  # Match the actual module
            },
            "entries": {
                "serialized_obj": {"value": "test1", "metadata": {"key": "value"}},
                "basic_string": "just_a_string"  # This will trigger line 322
            }
        }
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            json.dump(typed_data, tmp_file)
            temp_path = tmp_file.name
        
        try:
            registry = MockRegistry()
            registry.load_from_json(temp_path)
            
            # Verify both entries loaded correctly
            assert len(registry) == 2
            
            # The dict should be deserialized to MockSerializableClass
            obj = registry.get_entry("serialized_obj")
            assert isinstance(obj, MockSerializableClass)
            assert obj.value == "test1"
            
            # The string should remain as-is (line 322)
            basic = registry.get_entry("basic_string")
            assert basic == "just_a_string"
            
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_load_basic_json_type_registry(self):
        """Test loading basic JSON type registry (line 373)."""
        # Create data for a string registry (basic JSON type)
        typed_data = {
            "metadata": {
                "registry_type": "str",
                "registry_module": "builtins"
            },
            "entries": {
                "key1": "value1",
                "key2": "value2"
            }
        }
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            json.dump(typed_data, tmp_file)
            temp_path = tmp_file.name
        
        try:
            registry = StringRegistry()
            registry.load_from_json(temp_path)
            
            # This should hit line 373 (basic JSON types - no deserialization)
            assert len(registry) == 2
            assert registry.get_entry("key1") == "value1"
            assert registry.get_entry("key2") == "value2"
            
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_deep_copy_behavior(self):
        """Registry creates deep copies of entries."""
        registry = MockRegistry()
        original = MockSerializableClass("test", {"nested": {"key": "value"}})
        
        registry.add_entry("obj", original)
        retrieved = registry.get_entry("obj")
        
        # Modify original
        original.metadata["nested"]["key"] = "modified"
        
        # Retrieved should be unchanged (deep copy)
        assert retrieved.metadata["nested"]["key"] == "value"
    
    def test_registry_type_name_generation(self):
        """Factory-created registries have proper names."""
        StringRegistry = Registry.for_type(str)
        assert "Registry[str]" in StringRegistry.__name__
        
        MockRegistry = Registry.for_type(MockSerializableClass)
        assert "Registry[MockSerializableClass]" in MockRegistry.__name__
    
    def test_constructor_validates_entry_type(self):
        """Constructor validates entry type from get_entry_type()."""
        # Create a registry with non-serializable type to test validation
        class BadRegistry(Registry[object]):
            @classmethod
            def get_entry_type(cls) -> Type[object]:
                return object  # Not JSON serializable
        
        with pytest.raises(TypeError, match="Entry type .* is not allowed in Registry"):
            BadRegistry()
    
    def test_type_check_with_subclasses(self):
        """Test type checking works with subclasses."""
        # Create a subclass of MockSerializableClass
        class SubclassSerializable(MockSerializableClass):
            def __init__(self, value, metadata=None, extra=None):
                super().__init__(value, metadata)
                self.extra = extra
        
        # Create registry for the parent type
        registry = MockRegistry()
        
        # This should work because SubclassSerializable is a subclass of MockSerializableClass
        obj = SubclassSerializable("test", {"key": "value"}, "extra_data")
        registry.add_entry("test", obj)
        
        retrieved = registry.get_entry("test")
        assert isinstance(retrieved, MockSerializableClass)
        assert retrieved.value == "test"