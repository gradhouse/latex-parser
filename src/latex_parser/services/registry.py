# File: registry.py
# Description: Generic base class for maintaining a registry of entries identified by unique keys
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import copy
import json
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, Union, Type, Any

T = TypeVar('T')

from latex_parser.file.file_system import FileSystem


class Registry(Generic[T], ABC):    
    """
    Abstract base class for maintaining a registry of entries identified by unique keys.
    
    This class is abstract and requires subclasses to specify their entry type.
    This eliminates the runtime type guessing issue by requiring explicit type declaration.
    
    JSON SERIALIZATION CONSTRAINTS:
    All registries enforce that entries must be JSON-serializable:
    1. Basic JSON types: str, int, float, bool, list, dict, None
    2. Custom classes with both as_dict() and from_dict() methods
    
    USAGE PATTERNS:
    
    1. Create a concrete registry class:
       class StringRegistry(Registry[str]):
           @classmethod 
           def get_entry_type(cls) -> Type[str]:
               return str
       
       registry = StringRegistry()
    
    2. Use the factory method for quick creation:
       StringRegistry = Registry.for_type(str)
       registry = StringRegistry()
    """

    @classmethod
    @abstractmethod
    def get_entry_type(cls) -> Type[T]:
        """
        Return the type that this registry accepts.
        
        Concrete subclasses MUST implement this method to specify their entry type.
        
        :return: The type class for entries.
        :raises NotImplementedError: If a concrete subclass does not implement this method.
        """
        raise NotImplementedError("Concrete subclasses must implement get_entry_type()")

    @classmethod
    def for_type(cls, entry_type: Type[T]) -> Type['Registry[T]']:
        """
        Create a Registry class that enforces a specific entry type.
        The entry type must be JSON serializable or provide as_dict/from_dict methods.
        
        :param entry_type: The type to enforce for all entries.
        :return: A Registry class configured for the specified type.
        :raises TypeError: If entry_type is not JSON serializable.
        
        Usage:
            MyRegistry = Registry.for_type(MyClass)
            registry = MyRegistry()
        """
        if not cls._is_type_allowed(entry_type):
            raise TypeError(f"Entry type {entry_type} is not allowed in Registry. "
                          f"Must be JSON-serializable or provide as_dict/from_dict methods.")
        
        class TypedRegistry(cls):
            def __init__(self, file_path: Optional[str] = None) -> None:
                super().__init__(file_path=file_path, enforce_constraints=True)
            
            @classmethod
            def get_entry_type(cls) -> Type[T]:
                return entry_type
        
        TypedRegistry.__name__ = f"Registry[{entry_type.__name__}]"
        TypedRegistry.__qualname__ = f"Registry[{entry_type.__name__}]"
        return TypedRegistry

    @staticmethod
    def _is_type_allowed(entry_type: Union[Type[Any], Any]) -> bool:
        """
        Internal method to check if the given type or instance is allowed for registry entries.
        Allowed: dict, list, str, int, float, bool, NoneType, or has as_dict/from_dict methods.
        """
        # Accept both type and instance
        allowed_types = (dict, list, str, int, float, bool, type(None))
        
        # If entry_type is a type, check directly
        if isinstance(entry_type, type):
            if entry_type in allowed_types:
                return True
            # Check if the type has both as_dict and from_dict methods
            if (hasattr(entry_type, 'as_dict') and hasattr(entry_type, 'from_dict') and
                callable(getattr(entry_type, 'as_dict', None)) and 
                callable(getattr(entry_type, 'from_dict', None))):
                return True
            return False
        
        # If entry_type is an instance, check its type and methods
        if isinstance(entry_type, allowed_types):
            return True
        
        # Check if instance has as_dict method and its class has from_dict
        if (hasattr(entry_type, 'as_dict') and callable(getattr(entry_type, 'as_dict', None)) and
            hasattr(entry_type.__class__, 'from_dict') and 
            callable(getattr(entry_type.__class__, 'from_dict', None))):
            return True
        
        return False

    @staticmethod
    def _is_json_serializable(obj: Any) -> bool:
        """
        Check if an object can be JSON serialized using the standard json module.
        """
        try:
            json.dumps(obj)
            return True
        except (TypeError, ValueError):
            return False
    
    def __init__(self, file_path: Optional[str] = None, enforce_constraints: bool = True) -> None:
        """
        Initializes the registry as an empty dictionary.
        
        The entry type is determined by the concrete subclass via get_entry_type().
        This eliminates the runtime type guessing issue.
        
        :param file_path: Optional path to load registry from.
        :param enforce_constraints: Whether to enforce JSON serialization constraints (default: True).
        :raises TypeError: If the class's entry type is not allowed and enforce_constraints is True.
        """
        self._enforce_constraints = enforce_constraints
        
        # Get the entry type from the concrete subclass
        entry_type = self.__class__.get_entry_type()
        
        if self._enforce_constraints and not self._is_type_allowed(entry_type):
            raise TypeError(f"Entry type {entry_type} is not allowed in Registry. Must be JSON-serializable or provide as_dict/from_dict.")
        
        self._registry: dict[str, T] = dict()
        
        if file_path is not None:
            self.load_from_json(file_path)

    def clear(self) -> None:
        """
        Clears the registry and resets it to its default state.
        """
        self._registry.clear()

    def is_key_present(self, hash_key: str) -> bool:
        """
        Determine if the given hash key is present in the registry.

        :param hash_key: str, the hash key to check.
        :return: bool, True if the hash key is present, False otherwise.
        """
        return hash_key in self._registry

    def get_entry(self, hash_key: str) -> T:
        """
        Retrieve the entry associated with the given hash key.

        :param hash_key: str, the hash key to look up.
        :return: the entry if found.
        :raises KeyError: If the hash key is not present in the registry.
        """

        if hash_key not in self._registry:
            raise KeyError(f"Hash key '{hash_key}' not found in registry.")
        return self._registry[hash_key]

    def add_entry(self, hash_key: str, entry: T) -> None:
        """
        Add a new entry to the registry.

        :param hash_key: str, the unique key for the entry.
        :param entry: T, the entry data.

        :raises KeyError: If the key already exists.
        :raises TypeError: If the entry is not JSON serializable and lacks as_dict/from_dict methods.
        """
        if hash_key in self._registry:
            raise KeyError(f"Hash key '{hash_key}' already exists in registry.")

        # Enforce serialization constraints if enabled
        if self._enforce_constraints and not self._is_type_allowed(entry):
            raise TypeError(f"Entry is not JSON-serializable and does not provide as_dict/from_dict methods. "
                          f"Entry type: {type(entry)}")

        self._registry[hash_key] = copy.deepcopy(entry)

    def update_entry(self, hash_key: str, entry: T) -> None:
        """
        Update an existing entry in the registry.

        :param hash_key: str, the unique key for the entry.
        :param entry: T, the new entry data.
        :raises KeyError: If the key does not exist.
        :raises TypeError: If the entry is not JSON serializable and lacks as_dict/from_dict methods.
        """
        if hash_key not in self._registry:
            raise KeyError(f"Hash key '{hash_key}' not found in registry.")

        # Enforce serialization constraints if enabled
        if self._enforce_constraints and not self._is_type_allowed(entry):
            raise TypeError(f"Entry is not JSON-serializable and does not provide as_dict/from_dict methods. "
                          f"Entry type: {type(entry)}")

        self._registry[hash_key] = copy.deepcopy(entry)

    def delete_entry(self, hash_key: str) -> None:
        """
        Delete an entry from the registry.

        :param hash_key: str, the unique key for the entry.

        :raises KeyError: If the key does not exist.
        """
        if hash_key not in self._registry:
            raise KeyError(f"Hash key '{hash_key}' not found in registry.")

        del self._registry[hash_key]

    def list_keys(self) -> list[str]:
        """
        Return a list of all keys in the registry.
        """
        return list(self._registry.keys())

    def __len__(self):
        """
        Return the number of entries in the registry.
        """
        return len(self._registry)

    def validate_all_entries(self) -> dict[str, bool]:
        """
        Validate that all entries in the registry meet JSON serialization constraints.
        
        :return: Dictionary mapping keys to validation results (True if valid, False if invalid).
        """
        validation_results = {}
        for key, entry in self._registry.items():
            validation_results[key] = self._is_type_allowed(entry)
        return validation_results

    def save_to_json(self, file_path: str) -> None:
        """
        Save the registry to a JSON file. Entries must be JSON-serializable or provide an as_dict() method.

        :param file_path: str, the path to the output JSON file.
        :raises TypeError: If an entry is not serializable.
        """
        default_indent = 2
        entry_type = self.__class__.get_entry_type()

        # Create typed registry format
        serializable_registry = {
            "metadata": {
                "registry_type": entry_type.__name__,
                "registry_module": entry_type.__module__
            },
            "entries": {}
        }
        
        for k, v in self._registry.items():
            if self._is_json_serializable(v):
                serializable_registry["entries"][k] = v
            elif hasattr(v, 'as_dict') and callable(getattr(v, 'as_dict')):
                as_dict_method = getattr(v, 'as_dict')
                serializable_registry["entries"][k] = as_dict_method()
            else:
                raise TypeError(f"Entry for key '{k}' is not JSON-serializable and does not provide as_dict().")
        
        with open(file_path, 'w', encoding='utf-8') as file_handle:
            json.dump(serializable_registry, file_handle, indent=default_indent)

    def load_from_json(self, file_path: str) -> None:
        """
        Load the registry from a JSON file created by this typed registry system.
        
        The registry type is determined from the concrete subclass and used for deserialization.

        :param file_path: str, the path to the input JSON file.
        :raises FileNotFoundError: If the file does not exist.
        :raises ValueError: If the file format is invalid or registry type mismatch.
        """
        self.clear()
        if not FileSystem.is_file(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")
        
        with open(file_path, 'r', encoding='utf-8') as file_handle:
            data = json.load(file_handle)
            
            # Validate typed registry format
            if not isinstance(data, dict) or "metadata" not in data:
                raise ValueError(f"Invalid registry file format. Expected typed registry format with metadata.")
            
            metadata = data["metadata"]
            if not isinstance(metadata, dict) or "registry_type" not in metadata:
                raise ValueError(f"Invalid registry metadata format.")
            
            # Verify registry type matches
            expected_type = self.__class__.get_entry_type()
            file_type_name = metadata["registry_type"]
            file_module_name = metadata.get("registry_module", "")
            
            if expected_type.__name__ != file_type_name or expected_type.__module__ != file_module_name:
                raise ValueError(f"Registry type mismatch. Expected {expected_type.__module__}.{expected_type.__name__}, "
                               f"but file contains {file_module_name}.{file_type_name}")
            
            # Load entries
            entries = data["entries"]
            self._registry = {}
            
            if hasattr(expected_type, 'from_dict') and callable(getattr(expected_type, 'from_dict')):
                # Custom objects with from_dict method
                from_dict_method = getattr(expected_type, 'from_dict')
                for k, v in entries.items():
                    if isinstance(v, dict):
                        self._registry[k] = from_dict_method(v)
                    else:
                        # Basic JSON type - keep as-is  
                        self._registry[k] = v
            else:
                # Basic JSON types - no deserialization needed
                self._registry = entries
