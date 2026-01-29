
'''
Statement of Exercise 15: 
Given an array of words, create a function that returns it sorted. 
by the length of their words from shortest to longest 
'''
def lenght_information(p_list: list) -> list:
    p_list.sort(key=lambda x:len(x))
    return print(p_list)

p_list = [  "Hello", 
"soy", 
"Victor Robles", 
"how", 
"is", 
"today", 
"friend", 
"they", 
"go", "a", 
"study", 
"now" ]
lenght_information(p_list)

