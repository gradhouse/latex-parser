# File: test_command_definition.py
# Description: Unit tests for the CommandDefinition class
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import copy
import pytest
from typing import Dict, List, Any
from latex_parser.latex.definitions.command_definition import CommandDefinition, CommandMode, CommandRobustness, CommandType


class TestCommandDefinitionEnums:
    """Test the enum classes used by CommandDefinition."""
    
    def test_command_mode_enum_values(self):
        """CommandMode enum has all expected values."""
        expected_values = {
            'unknown': CommandMode.UNKNOWN,
            'left_right': CommandMode.LEFT_RIGHT,
            'preamble': CommandMode.PREAMBLE,
            'paragraph': CommandMode.PARAGRAPH,
            'math': CommandMode.MATH
        }
        
        for value_str, enum_value in expected_values.items():
            assert enum_value.value == value_str
    
    def test_command_robustness_enum_values(self):
        """CommandRobustness enum has all expected values."""
        expected_values = {
            'unknown': CommandRobustness.UNKNOWN,
            'robust': CommandRobustness.ROBUST,
            'fragile': CommandRobustness.FRAGILE
        }
        
        for value_str, enum_value in expected_values.items():
            assert enum_value.value == value_str
    
    def test_command_type_enum_values(self):
        """CommandType enum has all expected values."""
        expected_values = {
            'unknown': CommandType.UNKNOWN,
            'document': CommandType.DOCUMENT,
            'sectioning': CommandType.SECTIONING,
            'alignment': CommandType.ALIGNMENT,
            'math_symbol_greek_letter': CommandType.MATH_SYMBOL_GREEK_LETTER,
            'math_symbol_binary_op': CommandType.MATH_SYMBOL_BINARY_OP,
            'math_symbol_relation': CommandType.MATH_SYMBOL_RELATION,
            'math_symbol_arrow': CommandType.MATH_SYMBOL_ARROW,
            'math_symbol_misc': CommandType.MATH_SYMBOL_MISC,
            'math_symbol_variable_sized': CommandType.MATH_SYMBOL_VARIABLE_SIZED,
            'math_function_log_like': CommandType.MATH_FUNCTION_LOG_LIKE,
            'math_accent': CommandType.MATH_ACCENT,
            'math_enclosure': CommandType.MATH_ENCLOSURE,
            'text_accent': CommandType.TEXT_ACCENT,
            'text_symbol': CommandType.TEXT_SYMBOL,
            'text_spacing': CommandType.TEXT_SPACING,
            'delimiter': CommandType.DELIMITER,
            'bibliography': CommandType.BIBLIOGRAPHY,
            'font_declaration': CommandType.FONT_DECLARATION,
            'command_definition': CommandType.COMMAND_DEFINITION,
            'environment_definition': CommandType.ENVIRONMENT_DEFINITION,
            'file_inclusion': CommandType.FILE_INCLUSION,
            'tex_command_definition': CommandType.TEX_COMMAND_DEFINITION
        }
        
        for value_str, enum_value in expected_values.items():
            assert enum_value.value == value_str


class TestCommandDefinitionDefaultInitialization:
    """Test CommandDefinition initialization with default values."""
    
    def test_default_initialization_no_params(self):
        """CommandDefinition can be created with no parameters (defaults)."""
        cmd = CommandDefinition()
        
        # Verify all fields have default values
        assert hasattr(cmd, '_command_definition')
        assert isinstance(cmd._command_definition, dict)
        
        # Check default values through as_dict
        data = cmd.as_dict()
        assert data['name'] == ""
        assert data['syntax'] == ""
        assert data['command_type'] == CommandType.UNKNOWN.value
        assert data['robustness'] == CommandRobustness.UNKNOWN.value
        assert data['modes'] == []
        assert data['description'] == ""
        assert data['references'] == []


class TestCommandDefinitionFullInitialization:
    """Test CommandDefinition initialization with all parameters."""
    
    def test_full_initialization_all_params(self):
        """CommandDefinition can be created with all parameters provided."""
        name = "\\documentclass"
        syntax = "\\documentclass[options]{class}"
        command_type = CommandType.SECTIONING
        robustness = CommandRobustness.ROBUST
        modes = [CommandMode.PREAMBLE, CommandMode.PARAGRAPH]
        description = "Declares the document class"
        references = [
            {"ref_id": "latex2e", "sections": "2.1", "pages": "12-15"},
            {"ref_id": "companion", "sections": "4.3", "pages": "89"}
        ]
        
        cmd = CommandDefinition(
            name=name,
            syntax=syntax,
            command_type=command_type,
            robustness=robustness,
            modes=modes,
            description=description,
            references=references
        )
        
        # Verify all fields are set correctly
        data = cmd.as_dict()
        assert data['name'] == name
        assert data['syntax'] == syntax
        assert data['command_type'] == command_type.value
        assert data['robustness'] == robustness.value
        assert data['modes'] == [mode.value for mode in modes]
        assert data['description'] == description
        assert data['references'] == references
    
    def test_single_mode_initialization(self):
        """CommandDefinition works with single mode in list."""
        cmd = CommandDefinition(
            name="\\textbf",
            syntax="\\textbf{text}",
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.ROBUST,
            modes=[CommandMode.PARAGRAPH],
            description="Bold text formatting",
            references=[]
        )
        
        data = cmd.as_dict()
        assert data['modes'] == [CommandMode.PARAGRAPH.value]
    
    def test_empty_modes_and_references(self):
        """CommandDefinition works with empty modes and references lists."""
        cmd = CommandDefinition(
            name="\\test",
            syntax="\\test",
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.UNKNOWN,
            modes=[],
            description="Test command",
            references=[]
        )
        
        data = cmd.as_dict()
        assert data['modes'] == []
        assert data['references'] == []


class TestCommandDefinitionPartialInitialization:
    """Test CommandDefinition initialization error handling."""
    
    def test_partial_initialization_raises_error(self):
        """Providing only some parameters raises ValueError."""
        # Test providing only name
        with pytest.raises(ValueError, match="Either all parameters must be None, or all must be provided"):
            CommandDefinition(name="\\test")
        
        # Test providing name and syntax but not others
        with pytest.raises(ValueError, match="Either all parameters must be None, or all must be provided"):
            CommandDefinition(name="\\test", syntax="\\test{arg}")
        
        # Test providing all but one parameter
        with pytest.raises(ValueError, match="Either all parameters must be None, or all must be provided"):
            CommandDefinition(
                name="\\test",
                syntax="\\test{arg}",
                command_type=CommandType.UNKNOWN,
                robustness=CommandRobustness.UNKNOWN,
                modes=[CommandMode.PARAGRAPH],
                description="Test command"
                # Missing references parameter
            )


class TestCommandDefinitionClearMethod:
    """Test the clear method functionality."""
    
    def test_clear_resets_to_defaults(self):
        """clear() method resets all fields to default values."""
        # Create a fully initialized command
        cmd = CommandDefinition(
            name="\\section",
            syntax="\\section{title}",
            command_type=CommandType.SECTIONING,
            robustness=CommandRobustness.ROBUST,
            modes=[CommandMode.PARAGRAPH],
            description="Creates a section heading",
            references=[{"ref_id": "latex2e", "sections": "6.1", "pages": "25"}]
        )
        
        # Verify it's initialized
        data = cmd.as_dict()
        assert data['name'] == "\\section"
        assert data['description'] == "Creates a section heading"
        
        # Clear and verify defaults
        cmd.clear()
        
        data = cmd.as_dict()
        assert data['name'] == ""
        assert data['syntax'] == ""
        assert data['command_type'] == CommandType.UNKNOWN.value
        assert data['robustness'] == CommandRobustness.UNKNOWN.value
        assert data['modes'] == []
        assert data['description'] == ""
        assert data['references'] == []
    
    def test_clear_on_default_command(self):
        """clear() works on already default-initialized command."""
        cmd = CommandDefinition()
        
        # Should already be defaults
        data_before = cmd.as_dict()
        
        cmd.clear()
        
        data_after = cmd.as_dict()
        assert data_before == data_after


class TestCommandDefinitionSerialization:
    """Test as_dict method for JSON serialization."""
    
    def test_as_dict_complete_command(self):
        """as_dict returns correct dictionary representation."""
        name = "\\usepackage"
        syntax = "\\usepackage[options]{package}"
        command_type = CommandType.UNKNOWN
        robustness = CommandRobustness.FRAGILE
        modes = [CommandMode.PREAMBLE, CommandMode.PARAGRAPH]
        description = "Loads a LaTeX package"
        references = [
            {"ref_id": "latex2e", "sections": "2.3", "pages": "18-20"},
            {"ref_id": "guide", "sections": "1.4", "pages": "5"}
        ]
        
        cmd = CommandDefinition(
            name=name,
            syntax=syntax,
            command_type=command_type,
            robustness=robustness,
            modes=modes,
            description=description,
            references=references
        )
        
        result = cmd.as_dict()
        
        # Verify structure and content
        expected = {
            'name': name,
            'syntax': syntax,
            'command_type': command_type.value,
            'robustness': robustness.value,
            'modes': [mode.value for mode in modes],
            'description': description,
            'references': references
        }
        
        assert result == expected
        assert isinstance(result, dict)
    
    def test_as_dict_default_command(self):
        """as_dict works correctly with default values."""
        cmd = CommandDefinition()
        result = cmd.as_dict()
        
        expected = {
            'name': "",
            'syntax': "",
            'command_type': CommandType.UNKNOWN.value,
            'robustness': CommandRobustness.UNKNOWN.value,
            'modes': [],
            'description': "",
            'references': []
        }
        
        assert result == expected
    
    def test_as_dict_creates_deep_copy(self):
        """as_dict creates deep copies of mutable references."""
        original_refs = [{"ref_id": "test", "sections": "1", "pages": "1"}]
        cmd = CommandDefinition(
            name="\\test",
            syntax="\\test",
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.UNKNOWN,
            modes=[CommandMode.PARAGRAPH],
            description="Test",
            references=original_refs
        )
        
        result = cmd.as_dict()
        
        # Modify original references
        original_refs[0]["ref_id"] = "modified"
        
        # Result should be unchanged (deep copy)
        assert result['references'][0]["ref_id"] == "test"


class TestCommandDefinitionDeserialization:
    """Test from_dict class method for JSON deserialization."""
    
    def test_from_dict_complete_data(self):
        """from_dict correctly creates CommandDefinition from complete data."""
        data = {
            'name': '\\chapter',
            'syntax': '\\chapter{title}',
            'command_type': 'sectioning',
            'robustness': 'robust',
            'modes': ['paragraph', 'preamble'],
            'description': 'Creates a chapter heading',
            'references': [
                {'ref_id': 'latex2e', 'sections': '6.2', 'pages': '28-30'},
                {'ref_id': 'guide', 'sections': '2.1', 'pages': '15'}
            ]
        }
        
        cmd = CommandDefinition.from_dict(data)
        
        # Verify the command was created correctly
        result = cmd.as_dict()
        assert result['name'] == data['name']
        assert result['syntax'] == data['syntax']
        assert result['command_type'] == data['command_type']
        assert result['robustness'] == data['robustness']
        assert result['modes'] == data['modes']
        assert result['description'] == data['description']
        assert result['references'] == data['references']
    
    def test_from_dict_minimal_data(self):
        """from_dict works with minimal required data."""
        data = {
            'name': '\\test',
            'syntax': '\\test',
            'command_type': 'unknown',
            'robustness': 'unknown',
            'modes': [],
            'description': '',
            'references': []
        }
        
        cmd = CommandDefinition.from_dict(data)
        result = cmd.as_dict()
        
        assert result == data
    
    def test_from_dict_missing_required_fields_raises_error(self):
        """from_dict raises ValueError when required fields are missing."""
        # Missing 'name' field
        incomplete_data = {
            'syntax': '\\test',
            'command_type': 'unknown',
            'robustness': 'unknown',
            'modes': [],
            'description': 'Test',
            'references': []
        }
        
        with pytest.raises(ValueError, match="Input dictionary is missing required fields"):
            CommandDefinition.from_dict(incomplete_data)
        
        # Missing multiple fields
        very_incomplete_data = {
            'name': '\\test'
        }
        
        with pytest.raises(ValueError, match="Input dictionary is missing required fields"):
            CommandDefinition.from_dict(very_incomplete_data)
    
    def test_from_dict_invalid_command_type_raises_error(self):
        """from_dict raises ValueError for invalid command_type values."""
        data = {
            'name': '\\test',
            'syntax': '\\test',
            'command_type': 'invalid_type',  # Invalid enum value
            'robustness': 'unknown',
            'modes': [],
            'description': 'Test',
            'references': []
        }
        
        with pytest.raises(ValueError, match="Invalid command_type value: invalid_type"):
            CommandDefinition.from_dict(data)
    
    def test_from_dict_invalid_robustness_raises_error(self):
        """from_dict raises ValueError for invalid robustness values."""
        data = {
            'name': '\\test',
            'syntax': '\\test',
            'command_type': 'unknown',
            'robustness': 'invalid_robustness',  # Invalid enum value
            'modes': [],
            'description': 'Test',
            'references': []
        }
        
        with pytest.raises(ValueError, match="Invalid robustness value: invalid_robustness"):
            CommandDefinition.from_dict(data)
    
    def test_from_dict_invalid_mode_raises_error(self):
        """from_dict raises ValueError for invalid mode values."""
        data = {
            'name': '\\test',
            'syntax': '\\test',
            'command_type': 'unknown',
            'robustness': 'unknown',
            'modes': ['paragraph', 'invalid_mode'],  # Invalid enum value in list
            'description': 'Test',
            'references': []
        }
        
        with pytest.raises(ValueError, match="Invalid mode value in modes list"):
            CommandDefinition.from_dict(data)
    
    def test_from_dict_creates_deep_copy(self):
        """from_dict creates deep copies of mutable data."""
        original_refs = [{"ref_id": "test", "sections": "1", "pages": "1"}]
        data = {
            'name': '\\test',
            'syntax': '\\test',
            'command_type': 'unknown',
            'robustness': 'unknown',
            'modes': [],
            'description': 'Test',
            'references': original_refs
        }
        
        cmd = CommandDefinition.from_dict(data)
        
        # Modify original data
        original_refs[0]["ref_id"] = "modified"
        
        # Command should be unchanged (deep copy)
        result = cmd.as_dict()
        assert result['references'][0]["ref_id"] == "test"


class TestCommandDefinitionRoundTripSerialization:
    """Test serialization and deserialization round trips."""
    
    def test_serialization_round_trip(self):
        """Serialize and deserialize maintains data integrity."""
        original_cmd = CommandDefinition(
            name="\\subsection",
            syntax="\\subsection{title}",
            command_type=CommandType.SECTIONING,
            robustness=CommandRobustness.ROBUST,
            modes=[CommandMode.PARAGRAPH, CommandMode.LEFT_RIGHT],
            description="Creates a subsection heading",
            references=[
                {"ref_id": "latex2e", "sections": "6.3", "pages": "31-32"},
                {"ref_id": "art", "sections": "3.2", "pages": "45"}
            ]
        )
        
        # Serialize to dict
        data = original_cmd.as_dict()
        
        # Deserialize from dict
        restored_cmd = CommandDefinition.from_dict(data)
        
        # Verify they're equivalent
        assert restored_cmd.as_dict() == original_cmd.as_dict()
    
    def test_multiple_round_trips(self):
        """Multiple serialization round trips maintain data integrity."""
        original_cmd = CommandDefinition(
            name="\\textit",
            syntax="\\textit{text}",
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.FRAGILE,
            modes=[CommandMode.PARAGRAPH, CommandMode.MATH],
            description="Italic text formatting",
            references=[]
        )
        
        # Perform multiple round trips
        current_cmd = original_cmd
        for i in range(3):
            data = current_cmd.as_dict()
            current_cmd = CommandDefinition.from_dict(data)
        
        # Should still be identical
        assert current_cmd.as_dict() == original_cmd.as_dict()


class TestCommandDefinitionEdgeCases:
    """Test edge cases and special scenarios."""
    
    def test_all_enum_combinations(self):
        """CommandDefinition works with all enum value combinations."""
        # Test all CommandType values
        for cmd_type in CommandType:
            cmd = CommandDefinition(
                name=f"\\test_{cmd_type.value}",
                syntax=f"\\test_{cmd_type.value}",
                command_type=cmd_type,
                robustness=CommandRobustness.UNKNOWN,
                modes=[CommandMode.PARAGRAPH],
                description=f"Test for {cmd_type.value}",
                references=[]
            )
            
            data = cmd.as_dict()
            assert data['command_type'] == cmd_type.value
        
        # Test all CommandRobustness values
        for robustness in CommandRobustness:
            cmd = CommandDefinition(
                name=f"\\robust_{robustness.value}",
                syntax=f"\\robust_{robustness.value}",
                command_type=CommandType.UNKNOWN,
                robustness=robustness,
                modes=[CommandMode.PARAGRAPH],
                description=f"Test for {robustness.value}",
                references=[]
            )
            
            data = cmd.as_dict()
            assert data['robustness'] == robustness.value
        
        # Test all CommandMode values in various combinations
        for mode in CommandMode:
            cmd = CommandDefinition(
                name=f"\\mode_{mode.value}",
                syntax=f"\\mode_{mode.value}",
                command_type=CommandType.UNKNOWN,
                robustness=CommandRobustness.UNKNOWN,
                modes=[mode],
                description=f"Test for {mode.value}",
                references=[]
            )
            
            data = cmd.as_dict()
            assert data['modes'] == [mode.value]
    
    def test_complex_references_structure(self):
        """CommandDefinition handles complex references structures."""
        complex_refs = [
            {
                "ref_id": "latex2e",
                "sections": "2.1, 2.3-2.5, A.1",
                "pages": "12-15, 18-25, 180-190"
            },
            {
                "ref_id": "companion", 
                "sections": "4.3.1",
                "pages": "89"
            },
            {
                "ref_id": "guide",
                "sections": "1",
                "pages": "1-50"
            }
        ]
        
        cmd = CommandDefinition(
            name="\\complex",
            syntax="\\complex[opt1][opt2]{arg1}{arg2}",
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.FRAGILE,
            modes=[CommandMode.PARAGRAPH, CommandMode.MATH, CommandMode.LEFT_RIGHT],
            description="Complex command with multiple references",
            references=complex_refs
        )
        
        data = cmd.as_dict()
        assert data['references'] == complex_refs
        assert len(data['references']) == 3
        assert data['modes'] == ['paragraph', 'math', 'left_right']
    
    def test_special_characters_in_strings(self):
        """CommandDefinition handles special characters in string fields."""
        cmd = CommandDefinition(
            name="\\@startsection",
            syntax="\\@startsection{name}{level}{indent}{beforeskip}{afterskip}{style}",
            command_type=CommandType.SECTIONING,
            robustness=CommandRobustness.FRAGILE,
            modes=[CommandMode.PARAGRAPH],
            description="Internal LaTeX command for defining sectioning commands. Uses @ symbol.",
            references=[
                {
                    "ref_id": "source2e",
                    "sections": "ltclass.dtx § 2.3",
                    "pages": "N/A"
                }
            ]
        )
        
        data = cmd.as_dict()
        assert "@" in data['name']
        assert "@" in data['syntax']
        assert "§" in data['references'][0]['sections']
    
    def test_unicode_characters(self):
        """CommandDefinition handles Unicode characters properly."""
        cmd = CommandDefinition(
            name="\\textrm",
            syntax="\\textrm{text}",
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.ROBUST,
            modes=[CommandMode.PARAGRAPH],
            description="Roman text: αβγ, ñ, 中文, 🔤",
            references=[
                {
                    "ref_id": "unicode",
                    "sections": "§ 1.2",
                    "pages": "π ≈ 3.14"
                }
            ]
        )
        
        data = cmd.as_dict()
        assert "αβγ" in data['description']
        assert "ñ" in data['description']
        assert "中文" in data['description']
        assert "🔤" in data['description']
        assert "π ≈ 3.14" in data['references'][0]['pages']
    
    def test_empty_strings_and_lists(self):
        """CommandDefinition handles empty strings and lists correctly."""
        cmd = CommandDefinition(
            name="",
            syntax="",
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.UNKNOWN,
            modes=[],
            description="",
            references=[]
        )
        
        data = cmd.as_dict()
        assert data['name'] == ""
        assert data['syntax'] == ""
        assert data['modes'] == []
        assert data['description'] == ""
        assert data['references'] == []
        
        # Should serialize and deserialize correctly
        restored = CommandDefinition.from_dict(data)
        assert restored.as_dict() == data
    
    def test_very_long_strings(self):
        """CommandDefinition handles very long strings."""
        long_description = "A" * 1000  # 1000 character string
        long_syntax = "\\command" + "{arg}" * 50  # Very complex syntax
        
        cmd = CommandDefinition(
            name="\\longcommand",
            syntax=long_syntax,
            command_type=CommandType.UNKNOWN,
            robustness=CommandRobustness.UNKNOWN,
            modes=[CommandMode.PARAGRAPH],
            description=long_description,
            references=[]
        )
        
        data = cmd.as_dict()
        assert len(data['description']) == 1000
        assert data['syntax'] == long_syntax
        
        # Should round-trip correctly
        restored = CommandDefinition.from_dict(data)
        assert restored.as_dict() == data

