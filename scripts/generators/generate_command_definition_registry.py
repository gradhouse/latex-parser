# File: generate_command_definition_registry.py
# Description: Generate the command_definition_registry.json file
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import sys
import os

project_name = "latex_parser"

def get_python_include_directory(project_name: str) -> str:
    """
    Find the Python include directory for the given project.
    
    :param project_name: Name of the project to search for
    :return: Path to the src directory containing the project
    :raises RuntimeError: If the project directory cannot be found
    """
    current_dir = os.getcwd()
    
    # Find the project directory containing the project_name
    while current_dir != os.path.dirname(current_dir):  # Stop at filesystem root
        src_path = os.path.join(current_dir, 'src')
        if os.path.exists(src_path) and project_name in os.listdir(src_path):
            return src_path
        current_dir = os.path.dirname(current_dir)
    
    raise RuntimeError(f"Could not find project directory containing '{project_name}'")

# Add the src directory to the Python path for imports

python_include_path = get_python_include_directory(project_name)
sys.path.insert(0, python_include_path)

from latex_parser.latex.definitions.command_definition_registry import CommandDefinitionRegistry
from latex_parser.latex.definitions.register.register_command_definitions import register_latex_commands


def generate_command_definition_registry(file_path: str) -> None:
    """
    Generate the command_definition_registry.json file with LaTeX command definitions.
    
    :param file_path: Path where the JSON file should be saved
    """
    registry = CommandDefinitionRegistry()
    
    register_latex_commands(registry) 
    
    registry.save_to_json(file_path)


def main() -> None:
    """
    Main function to generate the command definition registry.
    """
    if len(sys.argv) != 2:
        print("Usage: python generate_command_definition_registry.py command_definition_registry.json")
        print("The project command definition registry should be moved to the data/latex directory.")
        sys.exit(1)
    
    output_path = sys.argv[1]
    
    # Make the path absolute and normalized
    output_path = os.path.abspath(output_path)
    
    print(f"Generating command definition registry at: {output_path}")
    
    try:
        generate_command_definition_registry(output_path)
        print("Command definition registry generated successfully!")
    except Exception as e:
        print(f"Error generating command definition registry: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()