#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) and roman_string is not None:
        count = len(roman_string)

        i = 0

        tmp = 0

        result = 0
        latin = list(roman_string)
        rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        while i < count:
            next_index = i + 1
            if next_index == count or rom[latin[i]] >= rom[latin[next_index]]:
                result += rom[latin[i]]
                i += 1
            elif count > 1 and rom[latin[i]] < rom[latin[next_index]]:
                tmp += rom[latin[next_index]] - rom[latin[i]]
                i += 2
        result = result + tmp
        return result
    else:
        return 0
