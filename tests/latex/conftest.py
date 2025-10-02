# File: conftest.py
# Description: Unit test configurations for LaTeX methods.
#
# Copyright (c) 2025 Jason Stuber
# Licensed under the MIT License. See the LICENSE file for more details.

import os
import sys
import pytest

@pytest.fixture(scope="session")
def latex_test_fixtures_directory():
    """
    Find the 'tests' directory in the path hierarchy and return the path to its 'latex/fixtures' subdirectory.
    """
    path = os.path.abspath(os.path.dirname(__file__))
    while True:
        if os.path.basename(path) == "tests":
            return os.path.join(path, "latex/fixtures")
        new_path = os.path.dirname(path)
        if new_path == path:
            raise RuntimeError("Could not find 'tests' directory in path hierarchy.")
        path = new_path

# Add the project root to Python path for imports
def pytest_configure():
    """Configure pytest to add the project root to Python path."""
    # Find the project root (where pyproject.toml is located)
    path = os.path.abspath(os.path.dirname(__file__))
    while True:
        if os.path.exists(os.path.join(path, "pyproject.toml")):
            if path not in sys.path:
                sys.path.insert(0, path)
            # Also add the tests directory for relative imports
            tests_path = os.path.join(path, "tests")
            if tests_path not in sys.path:
                sys.path.insert(0, tests_path)
            break
        new_path = os.path.dirname(path)
        if new_path == path:
            break
        path = new_path