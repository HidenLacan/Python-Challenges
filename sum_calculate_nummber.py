'''
Statement of Exercise 11: 
Create a function that takes an array of numbers as an input. 
and a number that will be the result of the sum of two of the values 

Examples: 
addTwo([3, 7, 8, 2], 10) // [3, 7] (both add up to 10) 
sumarDos([4, 5, 9, 1], 10) // [9, 1] 
sumarDos([1, 2, 3, 4], 5) // [2, 3] 
'''
# ------- ------- Simple Version ------- ------- #
input_number = [1, 2, 3, 4]
find_sum_result = 5

def easy_version(input_list_number: list,result : int) -> list:

    numbers = [] 
    for i in input_list_number:

        y = result - i

        if y in input_list_number:
            numbers.append(y)
            numbers.append(i)
            break
    
    return print(numbers)
            

### ------------------- Total Version ------------------- ###

def total_version(input_list_number: list,result : int) -> list:

    numbers = []
    for i in input_list_number:
            
            y = result - i
            
            for j in input_number:
                if y == j:
                    numbers.append(i)
                    numbers.append(j)
                    return print(numbers)

easy_version(input_number,find_sum_result)
total_version(input_number,find_sum_result)