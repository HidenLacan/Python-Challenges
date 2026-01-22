
"""
Statement of Exercise 9: 
Create a function that receives an array of numbers and calculates 
the sum of all even numbers in the array 

Examples: 
sumPairs([2, 13, 6, 15]); // Result: 8 
"""


number_list = [2, 13, 6, 15,30,40]

def calculate_eve_number(number_list: list) -> int:
    
    sum_number = 0 
    for number in number_list:
        if number % 2 == 0:
            sum_number += number
    
    return print (sum_number)

calculate_eve_number(number_list)