



'''
Statement of exercise 28:
Create a function that tells me if a number is an Armstrong number or not.
'''

natural_number = 371

def is_armstrong_number(number: int)-> bool: 

    list_numbers = [int(d) for d in str(number)]
    len_list_numbers = len(list_numbers)
    sum_total = 0
    
    for number in list_numbers:
        sum_total += number ** len_list_numbers    
    if sum_total == natural_number:
        return print(True)
    else:
        return print(False)

#is_armstrong_number(natural_number)


def is_armstrong_number_refactor(number: int)-> bool: 

    list_numbers = [int(d) for d in str(number)]
    len_list_numbers = len(list_numbers)
    
    ## Refactor using sum and generator expression
    sum_total = sum(number ** len_list_numbers for number in list_numbers)
    
    ## Refactor using ternary operator
    response = (True if sum_total == natural_number else False)
    return print(response)

is_armstrong_number_refactor(natural_number)