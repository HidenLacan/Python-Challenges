


'''
Statement of Exercise 7: 
Given an array of integers, detect if that list 
of numbers is a permutation from 1 to the last number in the array. 

In this case, a permutation is a sequence of numbers 
in order without any missing among them. 

Return the largest missing number. 

The array may be unsorted. 

Examples: 
permutation([1, 2, 3, 4, 5]) // Returns: 5 
permutation([1, 2, 3, 5])) // Returns: 4 

''' 


def max_missing_numbers(numbers: list):
    numbers = sorted(numbers)
    max_number = numbers[-1]
    
    for x in range(1,len(numbers) + 1):
        if x not in numbers:
            return x
    
    return max_number


print(max_missing_numbers([1, 2, 3,4, 5])) # 5 expected
print(max_missing_numbers([2, 3, 1, 5, 6, 4,8,9]))   # 7 expected
print(max_missing_numbers([1, 2, 3, 4, 5,8,9])) # 6 expected 