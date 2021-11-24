#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for key in a_dictionary:
        key *= 2
        return({k: a_dictionary[key]})
