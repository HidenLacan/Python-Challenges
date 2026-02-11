'''
Statement of Exercise 23: 
Create a function that takes some numbers in an array and decodes them. 
the message taking into account that each letter has an assigned number. 

The letters of the alphabet from A to Z have a number 
For example, A is number 1 and Z is number 26 

Examples: 
decodeMessage([8, 15, 12, 1]); 

Returns: 
HELLO 
'''

alphabet_dict = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z'
}


numbers = [8, 15, 12, 1]

def decode_message(numbers:list) -> str:
    message = "" 
    for number in numbers:
        if number in alphabet_dict:
            message += alphabet_dict[number]

    return message.upper()

print(decode_message(numbers))