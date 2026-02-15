
'''
Statement of Exercise 30: 
Given an array of numbers, allow duplicate numbers 
a maximum of 2 times and return the length of the array. 

Examples: 
eliminateDuplicates([4, 4, 4, 2, 2, 3]); // 5 
eliminateDuplicates([6, 6, 2, 2, 2, 3]); // 5 
eliminateDuplicates([1, 2, 3, 4, 9, 9, 9, 9]); // 5 
'''



list_numbers = [4, 4, 4, 2, 2, 3]

def eliminate_duplicates(numbers:list) -> int:
    counter = {}
    list_calculated = []
    for number in numbers:
        if number in counter:
            counter[number] += 1
        else:
            counter[number] = 1
    for number,count in counter.items():
        if count <= 1:
            list_calculated.append(number)
        else:
            list_calculated.append(number)
            list_calculated.append(number)

    len_list_calculated = len(list_calculated)

    return len_list_calculated

#print(eliminate_duplicates(list_numbers))

def eliminate_duplicates_refactor(numbers:list) -> int:
    counter = {}
    
    #                 Refactor using dictionary get method to simplify counting
    for number in numbers:
        counter[number] = counter.get(number, 0) + 1
    
    list_calculated = [
        number for number,count in counter.items()
        #             Refactor using list comprehension and slicing to limit duplicates to 2
        for _ in range(min(count,2))
    ]

    len_list_calculated = len(list_calculated)

    return list_calculated


print(eliminate_duplicates_refactor(list_numbers))