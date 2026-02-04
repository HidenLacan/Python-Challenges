'''
Statement of Exercise 18: 
Given an array of users, show only those who are over 20 years old 
and have the letters "o" and "n" in their name 
 
const users = [ 
{ name: 'Antonio', age: 20 }, 
{ name: 'Juan', age: 23 }, 
{ name: 'Pepe', age: 12 }, 
{ name: 'Raul', age: 28 }, 
{ name: 'Paco', age: 38 }, 
{ name: 'Jason', age: 56 } 
  ]; 
 
Examples: 
filterUsers(users); 
 
Returns: 
[ 
{ name: 'Antonio', age: 20 }, 
{ name: 'Jason', age: 56 } 
] 
'''

def filterUsers(users: list) -> list:
    
    container = []
    for elements in users:
        if 'o' in elements.get("name") and 'n' in elements.get("name"):
            if elements.get("age") >= 20:
                container.append(elements)

    return print(container)

users = [ 
{ 'name': 'Antonio', 'age': 20 }, 
{ 'name': 'Juan', 'age': 23 }, 
{ 'name': 'Pepe', 'age': 12 }, 
{ 'name': 'Raul', 'age': 28 }, 
{ 'name': 'Paco', 'age': 38 }, 
{ 'name': 'Jason', 'age': 56 } 
]

filterUsers(users)