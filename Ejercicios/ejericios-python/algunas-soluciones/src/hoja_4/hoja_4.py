#!/usr/bin/python
#-*- coding: utf-8 -*-

def count_in_list() -> None:
    STRING = "Una string cualquiera"
    CHAR = 'a'
    print(f"{CHAR} appears {STRING.count(CHAR)} times in {STRING}")


def count_vowels() -> None:
    VOWELS = "aeiou"
    STRING = "Una strIng cualquiEra"
    STRING = STRING.lower()
    count = {vowel: STRING.count(vowel) for vowel in VOWELS}
    for vowel in count.keys():
        print(f"The vowel {vowel} appears {count[vowel]} times in {STRING}")


def all_caps_all_lowercase() -> None:
    STRING = "Una strIng cualquiEra"
    print(f"all caps: {STRING.upper()}")
    print(f"all lowercase: {STRING.lower()}")


def change_to_upper() -> None:
    STRING = "Una strIng cualquiEra"
    CHAR = "q"
    new_string = ''.join(char if char != CHAR else CHAR.upper() \
                         for char in STRING)
    
    print(new_string)