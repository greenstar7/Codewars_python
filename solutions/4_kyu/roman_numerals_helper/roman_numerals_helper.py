"""Hrynevych Artemii
My solution for 4 kyu 'Roman Numerals Helper' kata
https://www.codewars.com/kata/roman-numerals-helper/python
"""

num_dict = {"M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1}
encode_num = ["M", "CM", "D", "CD", "C", "XC", "L",
                     "XL", "X", "IX", "V", "IV", "I"]

					 
class RomanNumerals:
    @staticmethod
    def to_roman(number):
        res = ''
        for numeral in encode_num:
            num_value = num_dict[numeral]
            while number >= num_value:
                res = ''.join((res, numeral))
                number -= num_value
        return res
    
    @staticmethod
    def from_roman(roman_num):
        roman_num = roman_num.upper().strip()
        values = [num_dict[x] for x in roman_num[::-1]]
        last = 0
        current = 0
        for i in range(len(values)):
            if last == 0:
                current += values[i]
            elif last > values[i]:
                current -= values[i]
            else:
                current += values[i]
            last = values[i]
        return current