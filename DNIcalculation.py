
"""
It is a simple mathematical process that is based on obtaining the 
remainder of the integer division of the ID number and the number 23. 
And with the rest, the letter is obtained, using it as a position or index. 
within an array of letters. 

This would be the array of letters: 
const letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',  
                'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E', 'T']; 

Examples: 
generateDNILetter("25439343"); // Result: 25439343D 

"""

def calculate_DNI(number:str) -> str:
    letters_list = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 
                'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E', 'T']
    become_number = int(number)
    result = become_number % 23
    letter = letters_list[result]
    number += letter
    
    return print(number)



calculate_DNI("25439343")