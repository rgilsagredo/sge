#!/usr/bin/python
#-*- coding: utf-8 -*-

import pytest
from hoja_1.utils.support import *
from constants import *

"""
Support functions tests
"""

def test_is_a_number_with_numeric_input():
    assert is_a_number(TWO) is True


def test_is_a_numebr_with_string_input():
    assert is_a_number(STRING) is False


def test_all_are_numbers_with_all_numbers_input():
    assert all_are_numbers([TWO,THREE_POINT_THREE]) is True


def test_all_are_numbers_with_string_input():
    assert all_are_numbers([STRING,TWO]) is False


def test_raise_error_if_not_a_number_with_number_input():
    try:
        raise_error_if_not_a_number(TWO)
    except TypeError:
        raise("raise_error_if_not_a_number raised TypeError unexpectedly!")
    

def test_raise_error_if_not_a_number_with_string_input():
    with pytest.raises(TypeError):
        raise_error_if_not_a_number(STRING)


def test_raise_error_if_not_all_inputs_are_numbers_with_number_input():
    try:
        raise_error_if_not_all_inputs_are_numbers([TWO,ZERO])
    except TypeError:
        raise("raise_error_if_not_all_inputs_are_numbers raised \
               TypeError unexpectedly!")
    

def test_raise_error_if_not_all_inputs_are_numbers_with_string_input():
    with pytest.raises(TypeError):
        raise_error_if_not_all_inputs_are_numbers([STRING, TWO])


"""
number_is_positive tests
"""
def test_number_is_positive_with_positive_number():
    assert number_is_positive(TWO) is True


def test_number_is_positive_with_zero_input():
    assert number_is_positive(ZERO) is False


def test_number_is_positive_with_negative_input():
    assert number_is_positive(-TWO) is False


def test_number_is_positive_raises_error():
    with pytest.raises(TypeError):
        number_is_positive(STRING)


"""
number_is_negative tests
"""
def test_number_is_negative_with_positive_number():
    assert number_is_negative(TWO) is False


def test_number_is_negative_with_zero_input():
    assert number_is_negative(ZERO) is False


def test_number_is_negative_with_negative_input():
    assert number_is_negative(-TWO) is True


def test_number_is_negative_raises_error():
    with pytest.raises(TypeError):
        number_is_negative(STRING)