"""MadLibs test file."""

import pytest
from madlibs import *


def test_setup_properly():
    """Test files are synced and welcome function eists."""
    assert welcome


def test_read_template_file():
    """Test template file can be read and returns content."""
    content = word_types('template.txt')
    assert len(content) > 0
    assert 'Adjective' in content
    assert isinstance('content', str)


def test_read_template_file_by_lines():
    """Test template file can be read by line."""
    lines = word_types('template.txt')
    assert len(lines) > 0
    assert isinstance('lines', list)


# def test():
#     """Test."""
#     pass


# def test():
#     """Test."""
#     pass


# def test():
#     """Test."""
#     pass
