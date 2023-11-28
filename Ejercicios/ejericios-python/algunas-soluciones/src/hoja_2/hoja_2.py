#!/usr/bin/python
#-*- coding: utf-8 -*-

from .utils import *

def square_until_negative() -> None:
    while(True):
        number = float(input(MSG_INPUT_UNTIL_NEGATIVE + \
                              MSG_SQUARE_UNTIL_NEGATIVE))
        if(number < ZERO):
            print(MSG_NEGATIVE_INPUT_DETECTED)
            print(MSG_ENDING_PROGRAM)
            break
        else:
            print(MSG_NUMBER_SQUARED + str(number**TWO))


def is_positive_or_negative() -> None:
    while(True):
        number = float(input(MSG_INPUT_UNTIL_ZERO + \
                              MSG_IS_POSITIVE_OR_NEGATIVE))
        if(number == ZERO):
            print(MSG_ZERO_INPUT_DETECTED)
            print(MSG_ENDING_PROGRAM)
            break
        elif(number > ZERO):
            print(MSG_THE_NUMBER_IS + MSG_POSITIVE)
        else:
            print(MSG_THE_NUMBER_IS + MSG_NEGATIVE)
            


def is_even_or_odd() -> None:
    while(True):
        number = float(input(MSG_INPUT_UNTIL_ZERO + \
                             MSG_IS_EVEN_OR_ODD))
        if(number == ZERO):
            print(MSG_ZERO_INPUT_DETECTED)
            print(MSG_ENDING_PROGRAM)
            break
        elif((number % TWO) == ZERO):
            print(MSG_THE_NUMBER_IS + MSG_EVEN)
        else:
            print(MSG_THE_NUMBER_IS + MSG_ODD)


def how_many_numbers() -> None:
    number_of_inputs = ONE
    while(True):
        number = float(input(MSG_INPUT_UNTIL_NEGATIVE + \
                             MSG_HOW_MANY_NUMBERS))
        if(number < ZERO):
            print(MSG_NEGATIVE_INPUT_DETECTED)
            print(MSG_ENDING_PROGRAM)
            break
        else:
            number_of_inputs += 1
        
    print(MSG_NUMBER_OF_INPUTS + f"{number_of_inputs}")


def guess_the_number() -> None:
    number = ZERO
    while(number != NUMBER_TO_GUESS):
        number = float(input(MSG_GUESS_THE_NUMBER))
        if(number < NUMBER_TO_GUESS):
            print(MSG_THE_SECRET_NUMBER_IS + MSG_GREATER + MSG_THAN_YOUR_NUMBER)
        elif(number > NUMBER_TO_GUESS):
            print(MSG_THE_SECRET_NUMBER_IS + MSG_SMALLER + MSG_THAN_YOUR_NUMBER)
    print(MSG_YOU_GUESSED_THE_NUMBER)


def sum_until_zero() -> None:
    _sum = []
    while(True):
        number = float(input(MSG_INPUT_UNTIL_ZERO + \
                             MSG_SUM_UNTIL_ZERO))
        if(number == ZERO):
            print(MSG_ZERO_INPUT_DETECTED)
            print(MSG_ENDING_PROGRAM)
            break
        else:
            _sum.append(number)
    print(MSG_THE_SUM_IS + f"{sum(_sum)}")


def mean_until_zero() -> None:
    _mean = []
    while(True):
        number = float(input(MSG_INPUT_UNTIL_ZERO + \
                             MSG_MEAN_UNTIL_ZERO))
        if(number == ZERO):
            print(MSG_ZERO_INPUT_DETECTED)
            print(MSG_ENDING_PROGRAM)
            break
        else:
            _mean.append(number)
    print(MSG_THE_SUM_IS + f"{sum(_mean)/len(_mean)}")



def numbers_until_N() -> None:
    number = int(input(MSG_INPUT_POSITIVE_INTEGER))
    print(MSG_NUMBERS_UNTIL + f"{number}" + MSG_ARE + "\n")
    for i in range(ONE, number):
        print(i)


def numbers_until_100_7_by_7() -> None:
    for number in range(ZERO, ONE_HUNDRED, SEVEN):
        print(number)


def multiply_10_first_odds() -> None:
    mult = ONE
    for number in [x for x in range(TWENTY) if ((x % TWO) == ONE)]:
        mult += number
    print(MSG_MULTIPLY_10_FIRTS_ODD + f"{mult}")


def factorial(number: int) -> None:
    if(number > ONE):
        return number*factorial(number-ONE)
    else:
        return ONE
    

def wierd_stuff_1() -> None:
    numbers = []
    for i in range(TEN):
        numbers.append((float(input(MSG_INPUT_NUMBER))))
    positives = [number for number in numbers if number > ZERO]
    negatives = [number for number in numbers if number < ZERO]
    zeroes = [number for number in numbers if number == ZERO]
    print(MSG_MEAN_OF_POSITIVES + f"{sum(positives)/len(positives)}")
    print(MSG_MEAN_OF_NEGATIVES + f"{sum(negatives)/len(negatives)}")
    print(MSG_NUMBER_OF_ZEROES + f"{len(zeroes)}")


def extarct_max() -> None:
    number = int(input(MSG_INPUT_POSITIVE_INTEGER))
    numbers = []
    for i in range(number):
        numbers.append(int(input(MSG_INPUT_NUMBER)))

    print(MSG_MAX_IS + f"{max(numbers)}")


def any_multiple_of_3() -> None:
    numbers = []
    for i in range(FIVE):
        numbers.append(int(input(MSG_INPUT_NUMBER)))

    if (any([number for number in numbers if (number % THREE) == ZERO])):
        print(MSG_MULT_OF_3_EXISTS)
    else:
        print(MSG_MULT_OF_3_NOT_EXISTS)


