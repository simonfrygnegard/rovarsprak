# -*- coding: utf-8 -*-
import pytest
from rovare import swede


def test_translate_one():
    """we should translate hohelollolo to hello"""
    assert swede('hohelollolo') == 'hello'

def test_translate_two():
    """we should handle whitespaces"""
    assert swede('cocododinongog isos fofunon') == 'coding is fun'


def test_translate_three():
    """we should handle unicode correct"""
    assert swede('dodetot äror lologogisoskoktot') == 'det är logiskt'


def test_number_is_string():
    """Number should be converted to string"""
    assert swede(8888) == '8888'

@pytest.mark.skip(reason='str is not a valid rovare text')
def test_everything_is_a_string():
    """even functions should be converted to string"""
    assert swede("str") == "<type 'str'>"


def test_do_not_pass_empty_values():
    """calling function without argument should raise TypeError"""
    with pytest.raises(TypeError):
        swede()

@pytest.mark.skip(reason='hardproblem')
def test_extra():
    assert swede('dodanonsosa momedod sosakoksosaror') == 'dansa med saxar'

