# File: command_definition.py
# Description: Definition class for LaTeX commands
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import copy
from typing import Dict, List, Optional, Any
from enum import Enum


class CommandMode(Enum):
    """
    Enumeration for LaTeX command mode categories.
    """
    UNKNOWN = 'unknown'         # Mode is not specified or not applicable
    LEFT_RIGHT = 'left_right'   # Left-Right mode: unbreakable horizontal boxes (e.g., \mbox, \hbox)
    PREAMBLE = 'preamble'       # Preamble mode: only valid before \begin{document}
    PARAGRAPH = 'paragraph'     # Paragraph mode: normal text mode for running text and most document content
    MATH = 'math'               # Math mode: for inline and display mathematical expressions


class CommandRobustness(Enum):
    """
    Enumeration for LaTeX command robustness.
    """
    UNKNOWN = 'unknown'   # Robustness is not specified or not applicable
    ROBUST = 'robust'     # Command is safe in moving arguments (e.g., section titles, captions)
    FRAGILE = 'fragile'   # Command may break or cause errors in moving arguments unless protected


class CommandType(Enum):
    """
    Enumeration for LaTeX command type categories.
    """
    UNKNOWN = 'unknown'             # Type is not specified or not applicable
    SECTIONING = 'sectioning'       # Sectioning commands (e.g., \section, \chapter)


class CommandDefinition:
    """
    Class representing a LaTeX command definition.
    
    This class stores information about LaTeX commands in a single dictionary.
    """
    
    def __init__(self, 
                 name: Optional[str] = None,
                 syntax: Optional[str] = None,
                 command_type: Optional[CommandType] = None,
                 robustness: Optional[CommandRobustness] = None,
                 modes: Optional[List[CommandMode]] = None,
                 description: Optional[str] = None,
                 references: Optional[List[Dict[str, str]]] = None) -> None:
        """
        Initialize a CommandDefinition object.
        
        When no parameters are provided, initializes with default values.
        When any parameter is provided, all parameters must be provided.
        
        :param name: str, command name with leading backslash (e.g., '\\documentclass')
        :param syntax: str, command syntax with placeholders (e.g., '\\documentclass[options]{class}')
        :param command_type: CommandType, type of command (e.g. CommandType.SECTIONING)
        :param robustness: CommandRobustness, command robustness (e.g. CommandRobustness.ROBUST)
        :param modes: List[CommandMode], list of modes where command is valid (e.g. CommandMode.PREAMBLE)
        :param description: str, Description of the command's purpose and behavior
        :param references: List[Dict[str, str]], list of references with keys like 'ref_id', 'sections', 'pages'
       
        :raises ValueError: If only some parameters are provided (not all or none).
        """

        self._command_definition: Dict[str, Any] = {}
        
        non_default_params = [name, syntax, command_type, robustness, modes, description, references]

        # Check that either all parameters are None or all are not None
        is_all_parameters_none = all(param is None for param in non_default_params)
        is_all_parameters_nontrivial = all(param is not None for param in non_default_params)
        
        if not (is_all_parameters_none or is_all_parameters_nontrivial):
            raise ValueError("Either all parameters must be None, or all must be provided (not None).")

        if is_all_parameters_nontrivial:
            self._command_definition['name'] = name
            self._command_definition['syntax'] = syntax
            self._command_definition['command_type'] = command_type
            self._command_definition['robustness'] = robustness
            self._command_definition['modes'] = modes            
            self._command_definition['description'] = description
            self._command_definition['references'] = references
        else:
            # No parameters provided, use defaults
            self._set_defaults()
            
    def clear(self) -> None:
        """
        Clear all fields in the command definition, resetting to default values.
        """
        self._command_definition.clear()
        self._set_defaults()

    def _set_defaults(self) -> None:
        """
        Set default values for all fields in the command definition.
        """
        self._command_definition = {
            'name': "",
            'syntax': "",
            'command_type': CommandType.UNKNOWN,
            'robustness': CommandRobustness.UNKNOWN,
            'modes': [],
            'description': "",
            'references': []
        }
                                
    def as_dict(self) -> Dict[str, Any]:
        """
        Convert this CommandDefinition to a dictionary for JSON serialization.
        
        :return: Dictionary representation of the command definition
        """

        return {
            'name': self._command_definition['name'],
            'syntax': self._command_definition['syntax'],
            'command_type': self._command_definition['command_type'].value,
            'robustness': self._command_definition['robustness'].value,
            'modes': [mode.value for mode in self._command_definition['modes']],
            'description': self._command_definition['description'],
            'references': copy.deepcopy(self._command_definition['references']),
        }
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CommandDefinition':
        """
        Create a CommandDefinition from a dictionary (deserialization from JSON).
        
        :param data: dict[str, Any], dictionary with command definition data
            The dictionary does not contain the enums but instead their values as strings.
        :return: CommandDefinition, a new CommandDefinition instance

        :raises ValueError: If required fields are missing in the input dictionary.  
        :raises ValueError: If the CommandType enum values are invalid.     
        :raises ValueError: If the CommandRobustness enum values are invalid. 
        :raises ValueError: If the CommandMode enum values are invalid.
        """

        # ensure all fields are present
        required_fields = ['name', 'syntax', 'command_type', 'robustness', 'modes', 'description', 'references']
        if not all(field in data for field in required_fields):
            raise ValueError("Input dictionary is missing required fields for CommandDefinition.")

        name = data['name']
        syntax = data['syntax']

        try:
            command_type = CommandType(data['command_type'])
        except ValueError:
            raise ValueError(f"Invalid command_type value: {data['command_type']}")  # not a valid enum value

        try:
            robustness = CommandRobustness(data['robustness'])
        except ValueError:
            raise ValueError(f"Invalid robustness value: {data['robustness']}")  # not a valid enum value
        
        try:
            modes = [CommandMode(mode_str) for mode_str in data['modes']]
        except ValueError as e:
            raise ValueError(f"Invalid mode value in modes list: {e}")  # not a valid enum value
        
        description = data['description']
        references = copy.deepcopy(data['references']) # list of dicts

        return cls(
            name=data.get('name', ''),
            syntax=data.get('syntax', ''),
            command_type=command_type,
            robustness=robustness,
            modes=modes,
            description=description,
            references=references
        )   
