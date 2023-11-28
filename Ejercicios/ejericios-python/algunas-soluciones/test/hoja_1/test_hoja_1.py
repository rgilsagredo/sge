#!/usr/bin/python
#-*- coding: utf-8 -*-

import pytest
from math import pi as PI
from constants import *
from hoja_1.hoja_1 import *
from hoja_1.utils._msg import MSG_NO_REAL_ROOTS, MSG_REAL_ROOTS

"""
square_number tests
"""

def test_square_number_with_int():
    assert square_number(TWO) == TWO**2


def test_square_number_with_float():
    assert square_number(THREE_POINT_THREE) == THREE_POINT_THREE**2


def test_square_number_raises_type_error():
    with pytest.raises(TypeError):
        square_number(STRING)


"""
solve_quadratic_equation test
"""
def test_solve_quadratic_equation_raises_type_error():
    with pytest.raises(TypeError):
        solve_quadratic_equation(STRING,TWO,TWO)


def test_solve_quadratic_equation_no_real_solutions():
    assert solve_quadratic_equation(ONE,ZERO,ONE) == MSG_NO_REAL_ROOTS


def test_solve_quadratic_equation_one_real_solution():
    assert solve_quadratic_equation(ONE,ZERO,ZERO) == \
        MSG_REAL_ROOTS + f"{float(ZERO)}, {float(ZERO)}"


def test_solve_quadratic_equation_two_real_solutions():
    assert solve_quadratic_equation(ONE,-TWO,ONE) == \
        MSG_REAL_ROOTS + f"{float(ONE)}, {float(ONE)}"


"""
circle_area tests
"""
def test_circle_area():
    assert circle_area(TWO) == (TWO**2)*PI


def test_circle_area_raises_error():
    with pytest.raises(TypeError):
        circle_area(STRING)


"""
circle_lenght tests
"""
def test_circle_length():
    assert circle_length(TWO) == TWO*2*PI


def test_circle_length_raises_error():
    with pytest.raises(TypeError):
        circle_length(STRING)


"""
two_numbers_are_equal tests
"""
def test_two_numbers_are_equal_equal_numbers():
    assert two_numbers_are_equal(ZERO, ZERO) is True


def test_two_numbers_are_equal_not_equal_input():
    assert two_numbers_are_equal(TWO, ZERO) is False


def test_two_numbers_are_equal_raises_error():
    with pytest.raises(TypeError):
        two_numbers_are_equal(STRING,ZERO)


"""
number_is_positive_negative_zero tests
"""
def test_number_is_positive_negative_zero_positive_input():
    assert number_is_positive_negative_zero(TWO) == ONE


def test_number_is_positive_negative_zero_negative_input():
    assert number_is_positive_negative_zero(-TWO) == -ONE


def test_number_is_positive_negative_zero_zero_input():
    assert number_is_positive_negative_zero(ZERO) == ZERO


def test_number_is_positive_negative_zero_raises_error():
    with pytest.raises(TypeError):
        number_is_positive_negative_zero(STRING)



"""
multiple_of_the_other test
# """
def test_multiple_of_the_other_raises_type_error():
    with pytest.raises(TypeError):
        multiple_of_the_other(STRING, TWO)


def test_multiple_of_the_other_detects_multiple_1():
    assert multiple_of_the_other(TWO, THREE*TWO) is True


def test_multiple_of_the_other_detects_multiple_2():
    assert multiple_of_the_other(TWO, -THREE*TWO) is True


def test_multiple_of_the_other_detects_multiple_3():
    assert multiple_of_the_other(-TWO, THREE*TWO) is True

def test_multiple_of_the_other_detects_not_multiple():
    assert multiple_of_the_other(TWO, THREE) is False


"""
swap_inputs tests
"""
def test_swap_inputs_swaps_correctly():
    out_1, out_2 = swap_inputs(-TWO, TWO)
    assert (out_1 == TWO) and (-TWO == out_2)


def test_swap_inputs_doesnt_swap_correctly():
    out_1, out_2 = swap_inputs(TWO, -TWO)
    assert (out_1 == TWO) and (-TWO == out_2)


def test_swap_inputs_raises_error():
    with pytest.raises(TypeError):
        swap_inputs(STRING, TWO)


"""
number_of_digits tests
"""
def test_number_of_digits_raises_type_error():
    with pytest.raises(TypeError):
        number_of_digits(STRING)

def test_number_of_digits_raises_value_error_1():
    with pytest.raises(ValueError):
        number_of_digits(-ONE)


def test_number_of_digits_raises_value_error_2():
    with pytest.raises(ValueError):
        number_of_digits(TEN_THOUSAND + ONE)


def test_number_of_digits_detects_1_digit():
    assert number_of_digits(ONE) == ONE


def test_number_of_digits_detects_2_digit():
    assert number_of_digits(TWENTY) == TWO


def test_number_of_digits_detects_3_digit():
    assert number_of_digits(FIVE_HUNDRED) == THREE


def test_number_of_digits_detects_2_digit():
    assert number_of_digits(SEVEN_THOUSAND) == FOUR


"""
number_backwards tests
"""
def test_number_backwards_raises_error():
    with pytest.raises(TypeError):
        number_backwards(STRING)


def test_number_backwards():
    assert number_backwards(ONE_TWO_THREE_FOUR) == FOUR_THREE_TWO_ONE


"""
number_is_capicua tests
"""
def test_number_is_capicua_raises_error():
    with pytest.raises(TypeError):
        number_is_capicua(STRING)


def test_number_is_capicua_recognizes_capicua():
    assert number_is_capicua(CAPICUA) is True


def test_number_is_capicua_recognizes_not_capicua():
    assert number_is_capicua(FIVE_HUNDRED) is False


"""
numeric_grade_to_words tests
"""
def test_numeric_grade_to_words_raises_value_error():
    with pytest.raises(ValueError):
        numeric_grade_to_words(-TWENTY)


def test_numeric_grade_to_words_raises_type_error():
    with pytest.raises(TypeError):
        numeric_grade_to_words(STRING)


def test_numeric_grade_to_words_suspeso():
    assert numeric_grade_to_words(TWO) == MSG_SUSPENSO


def test_numeric_grade_to_words_aprobado():
    assert numeric_grade_to_words(FIVE) == MSG_APROBADO


def test_numeric_grade_to_words_notable():
    assert numeric_grade_to_words(SEVEN) == MSG_NOTABLE


def test_numeric_grade_to_words_sobresaliente():
    assert numeric_grade_to_words(TEN) == MSG_SOBRESALIENTE