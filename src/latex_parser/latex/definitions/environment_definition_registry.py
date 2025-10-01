# File: environment_definition_registry.py
# Description: Registry for LaTeX environment definitions
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

from typing import Type, Optional, Any
from latex_parser.services.registry import Registry
from latex_parser.latex.definitions.environment_definition import EnvironmentDefinition


class EnvironmentDefinitionRegistry(Registry[EnvironmentDefinition]):
    """
    Registry for LaTeX environment definitions.

    This class maintains a collection of EnvironmentDefinition objects
    indexed by their environment names. It inherits from the generic Registry
    class and specifies EnvironmentDefinition as its entry type.

    USAGE:
        registry = EnvironmentDefinitionRegistry()
        registry.add_entry("tabular", env_def)  # Add an environment
        env = registry.get_entry("tabular")     # Retrieve an environment
    """
    
    @classmethod
    def get_entry_type(cls) -> Type[EnvironmentDefinition]:
        """
        Return EnvironmentDefinition as the type for this registry.

        :return: EnvironmentDefinition class
        """
        return EnvironmentDefinition

    @classmethod
    def for_type(cls, entry_type: Type[Any]) -> Type['Registry[EnvironmentDefinition]']:
        """
        Override to prevent creation of specialized EnvironmentDefinitionRegistry subclasses.

        EnvironmentDefinitionRegistry can only store EnvironmentDefinition objects and should not
        be specialized for other types.
        
        :param entry_type: Ignored parameter.
        :raises TypeError: Always raises this error to prevent instantiation.
        """
        raise TypeError(f"EnvironmentDefinitionRegistry can only store EnvironmentDefinition objects. "
                      f"Specialization for {entry_type.__name__} is not supported.")
        
    def __init__(self, file_path: Optional[str] = None) -> None:
        """
        Initialize a new EnvironmentDefinitionRegistry.

        :param file_path: Optional path to a JSON file containing environment definitions.
                         If provided, environments will be loaded from this file.
        :raises FileNotFoundError: If the file does not exist.
        :raises ValueError: If the file format is invalid.
        :raises TypeError: If an environment definition is not serializable.
        """
        # Initialize with enforcement of serialization constraints
        super().__init__(file_path=file_path, enforce_constraints=True)
