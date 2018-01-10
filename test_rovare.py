# -*- coding: utf-8 -*-
import pytest
from rovare import rovare


def test_translate_one():
    """we should translate bosse to bobosossose"""
    assert rovare('bosse') == 'bobosossose'

def test_translate_two():
    """we should handle whitespaces"""
    assert rovare('coding is fun') == 'cocododinongog isos fofunon'


def test_translate_three():
    """we should handle unicode correct"""
    assert rovare('hello börje') == 'hohelollolo bobörorjoje'


def test_number_is_string():
    """Number should be converted to string"""
    assert rovare(1337) == '1337'

def test_everything_is_a_string():
    """even functions should be converted to string"""
    assert rovare(len) == '<bobuiloltot-inon fofunoncoctotionon lolenon>'

def test_do_not_pass_empty_values():
    """calling function without argument should raise TypeError"""
    with pytest.raises(TypeError):
        rovare()

@pytest.mark.skip(reason='hardproblem')
def test_extra():
    assert rovare('sax') == 'sosakoksos'

