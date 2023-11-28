#!/usr/bin/python
#-*- coding: utf-8 -*-

from .utils import *
from numbers import Number
from math import sqrt, pi as PI

def hello_world() -> None:
    """Prints hello world"""
    print(MSG_HELLO_WORLD)


def square_number(number: Number) -> Number:
    """
    Squares a number.
    If input is invalid, raises TypeError
    """
    
    return number**2


def solve_quadratic_equation(a: Number, b: Number, c: Number) -> str:
    """
    Tries to solve a 2º degree equation. If no real solution exists, 
    the user is informed.
    If any of the coefficients is not a number, a TypeError is raised
    """
    
    discriminant_squared =  b**TWO - FOUR*a*c

    if discriminant_squared < ZERO:
        return MSG_NO_REAL_ROOTS
    else:
        root_1 = (-b + sqrt(discriminant_squared))/(TWO*a)
        root_2 = (-b - sqrt(discriminant_squared))/(TWO*a)
        return MSG_REAL_ROOTS + f"{root_1}, {root_2}"


def circle_area(radius: float) -> float:
    """
    Computes area of circle given the radius.
    If input is not a number, raises error
    """

    return PI*(radius**2)


def circle_length(radius: float) -> float:
    """
    Computes length of circle given the radius.
    If input is not a number, raises error
    """

    return PI*radius*TWO


def two_numbers_are_equal(number_1: Number, number_2: Number) -> bool:
    """
    Returns True if both numbers are equal.
    If any input is not a number, raises error
    """

    raise_error_if_not_all_inputs_are_numbers([number_1, number_2])

    return number_1 == number_2


def number_is_positive_negative_zero(number: Number) -> int:
    """
    Returns 1 if number is positive, -1 if number is negative, 
    0 if number if zero.
    Raises error if input is not a number
    """

    if(number_is_positive(number)):
        return ONE
    elif(number_is_negative(number)):
        return -ONE
    else:
        return ZERO
    


def multiple_of_the_other(number_1: Number, number_2: Number) -> bool:
    """
    Given 2 numbers, returns True if one is multiple of the other
    Raises error if any input is not a number
    """

    if (ZERO in [number_1, number_2]):
        return True
    else:
        return (number_1 % number_2 == ZERO) or (number_2 % number_1 == ZERO)
    

def swap_inputs(number_1: Number, number_2: Number) -> (Number, Number):
    """
    orders the inputs so the first returned is bigger
    raises type error if any input is not a number
    """

    if (number_1 <= number_2):
        return number_2, number_1
    else:
        return number_1, number_2
    

def number_of_digits(number: Number) -> int:
    """
    Given a number between 0 and 9999 returns the number
    of digits os the number.
    If the number if not in range, raises ValueError
    If input is not a number, raises ValueError
    """

    raise_error_if_not_a_number(number)

    if number not in range(ZERO, TEN_THOUSAND):
        raise ValueError(MSG_INVALID_RANGE)

    number_of_digits = ONE

    while(int(number / TEN) > ZERO):
        number = int(number / TEN)
        number_of_digits += ONE

    return number_of_digits


def number_backwards(number: Number) -> Number:
    """
    Given a number, it is turned backwards.
    If inpus is not a number, raise TypeError
    NOTE: Too lazy to consider cases where input is no int
    """

    raise_error_if_not_a_number(number)

    return int(str(number)[::-1])


def number_is_capicua(number: Number) -> bool:
    """
    Given a number, returns True is is capicua
    If input is not a number, raises TypeError
    """

    return number == number_backwards(number)


def numeric_grade_to_words(grade: Number) -> str:
    """
    Given a numeric grade between 0 and 10, it
    is converted to "suspenso", "aprobado"...
    If grade is out of valid range, a ValueError is
    raised. 
    If input is not numeric, TypeError is raised
    """

    raise_error_if_not_a_number(grade)

    if grade not in range(ZERO, TEN+ONE):
        raise ValueError(MSG_INVALID_RANGE_2)    
    
    if(grade < FIVE):
        return MSG_SUSPENSO
    elif(grade < SEVEN):
        return MSG_APROBADO
    elif(grade < 9):
        return MSG_NOTABLE
    else:
        return MSG_SOBRESALIENTE

