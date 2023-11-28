#!/usr/bin/python
#-*- coding: utf-8 -*-

from numbers import Number
from ._const import ZERO
from ._msg import MSG_RAISE_ERROR, MSG_RAISE_ERROR_2

def is_a_number(number: Number) -> bool:
    return isinstance(number, Number)


def all_are_numbers(list_of_numbers: list) -> bool:
    return all(list(map(is_a_number,list_of_numbers)))


def raise_error_if_not_a_number(number):
    if not is_a_number(number):
        raise TypeError(MSG_RAISE_ERROR, type(number))


def raise_error_if_not_all_inputs_are_numbers(list_of_numbers: list):
    if not (all_are_numbers(list_of_numbers)):
        raise TypeError(MSG_RAISE_ERROR_2)
    

def number_is_positive(number: Number) -> bool:
    """
    Returns True if a given number is positive
    If input is not a number, raises error
    """

    raise_error_if_not_a_number(number)

    return number > ZERO


def number_is_negative(number: Number) -> bool:
    """
    Returns True if a given number is negative
    If input is not a number, raises error
    """

    raise_error_if_not_a_number(number)

    return number < ZERO
