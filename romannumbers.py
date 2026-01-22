

"""
----- Roman Numerals Conversion----------------------

Statement of Exercise 8: 
Create an algorithm that takes an integer as an input. 
and convert it to Roman numerals. 

Examples: 
enteroARomano(100)); // Result: C 
integerToRoman(345)); // Result: CCCXLV 
"""

def number_to_roman(number:int) -> str:

    roman_map = [
        (1000, "M"),
        (900,  "CM"),
        (500,  "D"),
        (400,  "CD"),
        (100,  "C"),
        (90,   "XC"),
        (50,   "L"),
        (40,   "XL"),
        (10,   "X"),
        (9,    "IX"),
        (5,    "V"),
        (4,    "IV"),
        (1,    "I"),
    ]

    result = []

    for value,symbol in roman_map:
        if number == 0:
            break
        count = number // value
        
        # if count > 0:
        if count:
            result.append(symbol * count)
            number -= value * count

    print("".join(result))
    
number_to_roman(100)  # Expected: C
number_to_roman(345)  # Expected: CCCXLV