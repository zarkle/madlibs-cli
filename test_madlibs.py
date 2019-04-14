"""MadLibs test file."""

import pytest
from madlibs import *


def test_setup_properly():
    """Test that files are synced and welcome function exists."""
    assert welcome


def test_read_template_file():
    """Test template file can be read and returns content."""
    content = word_types('template.txt')
    assert len(content) > 0
    assert 'Adjective' in content
    assert isinstance(content, list)


# def test_read_template_file_by_lines():
#     """Test template file can be read by line."""
#     lines = word_types('template.txt')
#     assert len(lines) > 0
#     assert isinstance(lines, list)
#     assert type(lines) == list


def test_template_file_doesnt_exit():
    """Test that template file exists."""
    with pytest.raises(FileNotFoundError):
        word_types('wrong_file.txt')


def test_output_instructions(capsys):
    """Test instructions output correctly."""
    user_input([])
    captured = capsys.readouterr()
    assert 'Enter' in captured.out


def test_write_file():
    """Test output file is written."""
    path = 'result.txt'
    populate_template


# def test():
#     """Test."""
#     pass


# def test():
#     """Test."""
#     pass
