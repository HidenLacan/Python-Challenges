
'''
Statement of Exercise 20: 
Create a function that sorts an array of objects based on their properties 
that passes it as a parameter. 
 
const users = [ 
{ name: 'Antonio', age: 20 }, 
{ name: 'Juan', age: 23 }, 
{ name: 'Pepe', age: 12 }, 
{ name: 'Raul', age: 28 }, 
{ name: 'Paco', age: 38 }, 
{ name: 'Jason', age: 56 } 
  ]; 
 
 
Examples: 
orderObjects(users, "age"); 
'''


users = [ 
{ 'name': 'Antonio', 'age': 20 }, 
{ 'name': 'Juan', 'age': 23 }, 
{ 'name': 'Pepe', 'age': 12 }, 
{ 'name': 'Raul', 'age': 28 }, 
{ 'name': 'Paco', 'age': 38 }, 
{ 'name': 'Jason', 'age': 56 } 
]

def orderObjects(users: list,value : str) -> list:
    sort_by_age = sorted(users, key=lambda x: x[value])
    return print(sort_by_age)

orderObjects(users,"age")

# ----------------------No lambda version -- function
# def get_age(user):
#    return user["age"]

# sort_by_age = sorted(users, key=get_age)

# --------------------- DSU Decorate → Sort → Undecorate
#value = "age"
#decorated = []

#for user in users:
#    decorated.append((user[value],user))
#decorated.sort()
#undercorated = [user for age,user in decorated]

#print(undercorated)