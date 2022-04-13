"""Test suite for pdb_fasta_splitter.py"""
import pytest

from pdb_fasta_splitter import get_fh


def test_get_fh_for_ioerror():
    """
    Checks to see if the get_fh function raises an IOError when appropriate
    """
    # does it raise IOError
    # this should exit
    with pytest.raises(IOError):
        get_fh("does_not_exist.txt", "r")


def test_get_fh_for_valueerror():
    """
    Checks to see if the get_fh function raises a ValueError when appropriate
    """
    # does it raise ValueError
    # this should exit
    with pytest.raises(ValueError):
        get_fh("ss.txt", "rrr")
