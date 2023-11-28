#!/usr/bin/python
#-*- coding: utf-8 -*-

def invert_list() -> None:
    some_list = [1,2,3,4,5]
    print(some_list[::-1])


def mix_lists() -> None:
    list_1 = [1,2,3]
    list_2 = ["a","b","c"]
    mix_list = []
    for x,y in zip(list_1,list_2):
        mix_list.append(x)
        mix_list.append(y)

    print(mix_list)


def insert_list_into_list() -> None:
    list_1 = [1,2,3,4,5]
    list_to_insert = ["a","b","c"]
    position_to_insert = 3
    list_1[position_to_insert:position_to_insert] = list_to_insert
    print(list_1)


def modify_element_of_list() -> None:
    list_1 = [1,2,3,4,5]
    position_to_modify = 3
    list_1[position_to_modify] = 123456
    print(list_1)


def find_index_of_element() -> None:
    list_1 = [1,2,3,4,5]
    print(f"index of 5 is {list_1.index(5)}")
    # print(f"index of 55 is {list_1.index(55)}") TRY CATCH THIS


def classic_matrix_exercise() -> None:
    matrix = [[1 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            matrix[i][j] = i+j+1

    for row in matrix:
        print(row)