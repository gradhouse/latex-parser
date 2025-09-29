# File: command_definition_registry.py
# Description: Registry for LaTeX command definitions
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

from typing import Type, Optional, Any
from latex_parser.services.registry import Registry
from latex_parser.latex.definitions.command_definition import CommandDefinition


class CommandDefinitionRegistry(Registry[CommandDefinition]):
    """
    Registry for LaTeX command definitions.
    
    This class maintains a collection of CommandDefinition objects
    indexed by their command names. It inherits from the generic Registry
    class and specifies CommandDefinition as its entry type.
    
    USAGE:
        registry = CommandDefinitionRegistry()
        registry.add_entry("\\textbf", command_def)  # Add a command
        cmd = registry.get_entry("\\textbf")         # Retrieve a command
    """
    
    @classmethod
    def get_entry_type(cls) -> Type[CommandDefinition]:
        """
        Return CommandDefinition as the type for this registry.
        
        :return: CommandDefinition class
        """
        return CommandDefinition
        
    @classmethod
    def for_type(cls, entry_type: Type[Any]) -> Type['Registry[CommandDefinition]']:
        """
        Override to prevent creation of specialized CommandDefinitionRegistry subclasses.
        
        CommandDefinitionRegistry can only store CommandDefinition objects and should not
        be specialized for other types.
        
        :param entry_type: Ignored parameter.
        :raises TypeError: Always raises this error to prevent instantiation.
        """
        raise TypeError(f"CommandDefinitionRegistry can only store CommandDefinition objects. "
                      f"Specialization for {entry_type.__name__} is not supported.")
        
    def __init__(self, file_path: Optional[str] = None) -> None:
        """
        Initialize a new CommandDefinitionRegistry.
        
        :param file_path: Optional path to a JSON file containing command definitions.
                         If provided, commands will be loaded from this file.
        :raises FileNotFoundError: If the file does not exist.
        :raises ValueError: If the file format is invalid.
        :raises TypeError: If a command definition is not serializable.
        """
        # Initialize with enforcement of serialization constraints
        super().__init__(file_path=file_path, enforce_constraints=True)
