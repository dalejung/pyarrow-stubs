"""
This type stub file was generated by pyright.
"""

import pytest

groups = ...
defaults = ...
def pytest_ignore_collect(path, config): # -> bool:
    ...

@pytest.fixture(autouse=True)
def add_fs(doctest_namespace, request, tmp_path): # -> Generator[None, None, None]:
    ...
