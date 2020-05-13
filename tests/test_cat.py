import pytest

import cat


def test_get_info():
    assert cat.Cat.get_info() == 'cat - concatenate files and print on the standard output'
