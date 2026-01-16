"""
Statement of Exercise 5: 
Given an array of people with first and last names 
Create a function to sort the array by surnames 
in alphabetical order 
 
Example: 
sortByLastName([ 
    "Victor Robles", 
    "Antonio Alcantara", 
    "Al Pacino", 
    "Robert DeNiro", 
    "Brad Pitt", 
    "Sylvester Stallone" 
]);   
"""



def sortBySurnames(names:list):
    surnames = []
    sort_names = []

    # split names and store reversed in surnames
    for name in names:
        sunames = name.split(" ")
        surnames.append(sunames[::-1])

    # sort by surnames
    sorted_surnames = sorted(surnames)

    # reconstruct names in sorted order
    for name in sorted_surnames:
        sort_names.append(" ".join(name[::-1]))
    
    return print(sort_names)

sortBySurnames(
    [ 
    "Victor Robles", 
    "Antonio Alcantara", 
    "Al Pacino", 
    "Robert DeNiro", 
    "Brad Pitt", 
    "Sylvester Stallone" 
]
)

#output: ['Antonio Alcantara', 'Robert DeNiro', 'Al Pacino', 'Brad Pitt', 'Victor Robles', 'Sylvester Stallone']