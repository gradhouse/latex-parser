# File: register_command_definitions.py
# Description: Register LaTeX command definitions
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

from latex_parser.latex.definitions.command_definition import CommandDefinition, CommandType, CommandRobustness, CommandMode
from latex_parser.latex.definitions.command_definition_registry import CommandDefinitionRegistry

def register_document_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register LaTeX document commands in the command definition registry.

    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for document commands
    references = [{'ref_id': 'lamport_1994', 'sections': '2.2.2, C.5.1, C.5.2, C.5.4', 'pages': '19-21, 176-179, 181-183'}]
    
    def add_doc_cmd(name: str, syntax: str, description: str) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.DOCUMENT,
            robustness=CommandRobustness.ROBUST, modes=[CommandMode.PREAMBLE],
            description=description, references=references
        ))
    
    # Register document commands
    add_doc_cmd('\\documentclass', '\\documentclass[options]{class}', 
                'Specifies the overall layout of the document by selecting a document class and optional parameters')
    add_doc_cmd('\\documentstyle', '\\documentstyle[options]{style}',
                'Specifies the overall layout of the document by selecting a document style and optional parameters. This command is for LaTeX 2.09 and deprecated in favor of \\documentclass.')
    add_doc_cmd('\\usepackage', '\\usepackage[options]{packages}',
                'Loads a LaTeX package with optional parameters')
    add_doc_cmd('\\maketitle', '\\maketitle',
                'Generates the title block using information from \\title, \\author, \\date, and \\thanks')
    add_doc_cmd('\\title', '\\title{title}',
                'Defines the document title to be typeset by \\maketitle')
    add_doc_cmd('\\author', '\\author{authors}',
                'Defines the document author(s) to be typeset by \\maketitle')
    add_doc_cmd('\\date', '\\date{date}',
                'Defines the document date to be typeset by \\maketitle')
    add_doc_cmd('\\thanks', '\\thanks{text}',
                'Provides a footnote for the title, author, or date in the title block')


def register_sectioning_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register LaTeX sectioning commands in the command definition registry.
    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    # Common attributes for sectioning commands
    references = [{'ref_id': 'lamport_1994', 'sections': '2.2.3, C.4.1', 'pages': '21-22, 174'}]
    
    def add_sect_cmd(name: str, syntax: str, description: str) -> None:
        registry.add_entry(name, CommandDefinition(
            name=name, syntax=syntax, command_type=CommandType.SECTIONING,
            robustness=CommandRobustness.ROBUST, modes=[CommandMode.PARAGRAPH],
            description=description, references=references
        ))
    
    # Register sectioning commands
    add_sect_cmd('\\part', '\\part[toc_entry]{heading}',
                 'Starts a major sectional division at the part level; typically used in book classes; optionally adds an entry to the table of contents')
    add_sect_cmd('\\part*', '\\part*{heading}',
                 'Starts a major sectional division at the part level without adding an entry to the table of contents')
    add_sect_cmd('\\chapter', '\\chapter[toc_entry]{heading}',
                 'Starts a major sectional division at the chapter level; typically used in book and report classes; optionally adds an entry to the table of contents')
    add_sect_cmd('\\chapter*', '\\chapter*{heading}',
                 'Starts a major sectional division at the chapter level without adding an entry to the table of contents')
    add_sect_cmd('\\section', '\\section[toc_entry]{heading}',
                 'Starts a major sectional division at the section level; typically used in articles, books, and reports; optionally adds an entry to the table of contents')
    add_sect_cmd('\\section*', '\\section*{heading}',
                 'Starts a major sectional division at the section level without adding an entry to the table of contents')
    add_sect_cmd('\\subsection', '\\subsection[toc_entry]{heading}',
                 'Starts a sectional division at the subsection level; optionally adds an entry to the table of contents')
    add_sect_cmd('\\subsection*', '\\subsection*{heading}',
                 'Starts a sectional division at the subsection level without adding an entry to the table of contents')
    add_sect_cmd('\\subsubsection', '\\subsubsection[toc_entry]{heading}',
                 'Starts a sectional division at the subsubsection level; optionally adds an entry to the table of contents')
    add_sect_cmd('\\subsubsection*', '\\subsubsection*{heading}',
                 'Starts a sectional division at the subsubsection level without adding an entry to the table of contents')
    add_sect_cmd('\\paragraph', '\\paragraph[toc_entry]{heading}',
                 'Starts a sectional division at the paragraph level; optionally adds an entry to the table of contents')
    add_sect_cmd('\\paragraph*', '\\paragraph*{heading}',
                 'Starts a sectional division at the paragraph level without adding an entry to the table of contents')
    add_sect_cmd('\\subparagraph', '\\subparagraph[toc_entry]{heading}',
                 'Starts a sectional division at the subparagraph level; optionally adds an entry to the table of contents')
    add_sect_cmd('\\subparagraph*', '\\subparagraph*{heading}',
                 'Starts a sectional division at the subparagraph level without adding an entry to the table of contents')
        
def register_latex_commands(registry: CommandDefinitionRegistry) -> None:
    """
    Register LaTeX commands in the command definition registry.

    :param registry: CommandDefinitionRegistry, the registry to populate
    """
    
    register_document_commands(registry)
    register_sectioning_commands(registry)
