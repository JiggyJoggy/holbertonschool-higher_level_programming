#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    high_value = None
    for key, value in a_dictionary.items():
        if high_value is None or value > high_value:
            high_value = value
            high_name = key
    return high_name
