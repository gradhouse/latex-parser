# File: environment_definition.py
# Description: Definition class for LaTeX environments
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import copy
from typing import Dict, List, Optional, Any
from enum import Enum


class EnvironmentMode(Enum):
    """
    Enumeration for LaTeX environment mode categories.
    """
    UNKNOWN = 'unknown'            # Mode is not specified or not applicable
    LEFT_RIGHT = 'left_right'      # Left-Right mode: unbreakable horizontal boxes (e.g., \mbox, \hbox)
    PREAMBLE = 'preamble'          # Preamble mode: only valid before \begin{document}
    PARAGRAPH = 'paragraph'        # Paragraph mode: normal text mode for running text and most document content
    MATH_INLINE = 'math_inline'    # Inline math mode: for inline mathematical expressions
    MATH_DISPLAY = 'math_display'  # Display math mode: for displayed mathematical expressions


class EnvironmentRobustness(Enum):
    """
    Enumeration for LaTeX environment robustness.
    """
    UNKNOWN = 'unknown'   # Robustness is not specified or not applicable
    ROBUST = 'robust'     # Environment is safe in moving arguments (e.g., section titles, captions)
    FRAGILE = 'fragile'   # Environment may break or cause errors in moving arguments unless protected


class EnvironmentType(Enum):
    """
    Enumeration for LaTeX environment type categories.
    """
    UNKNOWN = 'unknown'                                       # Type is not specified or not applicable
    TABULAR = 'tabular'                                       # tabular, tabular*, array
    MATH_DISPLAY = 'math_display'                             # equation, align, gather


class EnvironmentDefinition:
    """
    Class representing a LaTeX environment definition.

    This class stores information about LaTeX environments in a single dictionary.
    """
    
    def __init__(self, 
                 name: Optional[str] = None,
                 syntax: Optional[str] = None,
                 environment_type: Optional[EnvironmentType] = None,
                 robustness: Optional[EnvironmentRobustness] = None,
                 modes: Optional[List[EnvironmentMode]] = None,
                 description: Optional[str] = None,
                 references: Optional[List[Dict[str, str]]] = None) -> None:
        """
        Initialize a EnvironmentDefinition object.

        When no parameters are provided, initializes with default values.
        When any parameter is provided, all parameters must be provided.

        :param name: str, environment name (e.g., 'tabular')
        :param syntax: str, environment syntax with placeholders (e.g., '\\begin{tabular}[pos]{cols}')
        :param environment_type: EnvironmentType, type of environment (e.g. EnvironmentType.TABULAR)
        :param robustness: EnvironmentRobustness, environment robustness (e.g. EnvironmentRobustness.ROBUST)
        :param modes: List[EnvironmentMode], list of modes where environment is valid (e.g. EnvironmentMode.PARAGRAPH, EnvironmentMode.MATH_DISPLAY)
        :param description: str, Description of the environment's purpose and behavior
        :param references: List[Dict[str, str]], list of references with keys like 'ref_id', 'sections', 'pages'
       
        :raises ValueError: If only some parameters are provided (not all or none).
        """

        self._environment_definition: Dict[str, Any] = {}

        non_default_params = [name, syntax, environment_type, robustness, modes, description, references]

        # Check that either all parameters are None or all are not None
        is_all_parameters_none = all(param is None for param in non_default_params)
        is_all_parameters_nontrivial = all(param is not None for param in non_default_params)
        
        if not (is_all_parameters_none or is_all_parameters_nontrivial):
            raise ValueError("Either all parameters must be None, or all must be provided (not None).")

        if is_all_parameters_nontrivial:
            self._environment_definition['name'] = name
            self._environment_definition['syntax'] = syntax
            self._environment_definition['environment_type'] = environment_type
            self._environment_definition['robustness'] = robustness
            self._environment_definition['modes'] = modes
            self._environment_definition['description'] = description
            self._environment_definition['references'] = references
        else:
            # No parameters provided, use defaults
            self._set_defaults()
            
    def clear(self) -> None:
        """
        Clear all fields in the environment definition, resetting to default values.
        """
        self._environment_definition.clear()
        self._set_defaults()

    def _set_defaults(self) -> None:
        """
        Set default values for all fields in the environment definition.
        """
        self._environment_definition = {
            'name': "",
            'syntax': "",
            'environment_type': EnvironmentType.UNKNOWN,
            'robustness': EnvironmentRobustness.UNKNOWN,
            'modes': [],
            'description': "",
            'references': []
        }
                                
    def as_dict(self) -> Dict[str, Any]:
        """
        Convert this EnvironmentDefinition to a dictionary for JSON serialization.

        :return: Dictionary representation of the environment definition
        """

        return {
            'name': self._environment_definition['name'],
            'syntax': self._environment_definition['syntax'],
            'environment_type': self._environment_definition['environment_type'].value,
            'robustness': self._environment_definition['robustness'].value,
            'modes': [mode.value for mode in self._environment_definition['modes']],
            'description': self._environment_definition['description'],
            'references': copy.deepcopy(self._environment_definition['references']),
        }
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'EnvironmentDefinition':
        """
        Create a EnvironmentDefinition from a dictionary (deserialization from JSON).

        :param data: dict[str, Any], dictionary with environment definition data
            The dictionary does not contain the enums but instead their values as strings.
        :return: EnvironmentDefinition, a new EnvironmentDefinition instance

        :raises ValueError: If required fields are missing in the input dictionary.  
        :raises ValueError: If the EnvironmentType enum values are invalid.     
        :raises ValueError: If the EnvironmentRobustness enum values are invalid. 
        :raises ValueError: If the EnvironmentMode enum values are invalid.
        """

        # ensure all fields are present
        required_fields = ['name', 'syntax', 'environment_type', 'robustness', 'modes', 'description', 'references']
        if not all(field in data for field in required_fields):
            raise ValueError("Input dictionary is missing required fields for EnvironmentDefinition.")

        name = data['name']
        syntax = data['syntax']

        try:
            environment_type = EnvironmentType(data['environment_type'])
        except ValueError:
            raise ValueError(f"Invalid environment_type value: {data['environment_type']}")  # not a valid enum value

        try:
            robustness = EnvironmentRobustness(data['robustness'])
        except ValueError:
            raise ValueError(f"Invalid robustness value: {data['robustness']}")  # not a valid enum value
        
        try:
            modes = [EnvironmentMode(mode_str) for mode_str in data['modes']]
        except ValueError as e:
            raise ValueError(f"Invalid mode value in modes list: {e}")  # not a valid enum value
        
        description = data['description']
        references = copy.deepcopy(data['references']) # list of dicts

        return cls(
            name=name,
            syntax=syntax,
            environment_type=environment_type,
            robustness=robustness,
            modes=modes,
            description=description,
            references=references
        )   
