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


# def test():
#     """Test."""
#     pass


# def test():
#     """Test."""
#     pass


# def test():
#     """Test."""
#     pass


# def test():
#     """Test."""
#     pass
