#!/usr/bin/python
#-*- coding: utf-8 -*-

from collections import Counter
SPECIAL_CHARS = (" ", ",", ".", ";")

def list_of_tuples_to_dict() -> None:
    LIST_OF_TUPLES = [(1,"a","b"), (2,"c","d","e"),(3,"z","x",6)]
    result = {tupla[0]:tupla[1:] for tupla in LIST_OF_TUPLES}
    print(result)


def number_of_appearences() -> None:
    STRING = "esta string tiene palabras, palabras que tiene la string " + \
        " a veces se repiten como esta, a veces no se repiten"
    result = Counter(STRING.split(" "))
    print(result)


def count_char_appearences() -> None:
    STRING = "esta string tiene palabras, palabras que tiene la string " + \
        " a veces se repiten como esta, a veces no se repiten"
    # STRING = "aaaa bbb ddda"
    
    result = {char: STRING.count(char) for char in STRING}
    print(result)


def text_to_dict(text: str) -> dict:
    chars = set(text)
    chars.remove(' ')
    result = {char: max({word for word in set(text.split(' ')) if char in word}, \
                        key=len) for char in chars}
    return result
