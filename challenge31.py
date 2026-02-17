
''' 
Statement of Exercise 31: 
Given a text, create a function that is able to reverse 
the order of his words. 

We cannot use native language functions. 

Examples: 
invertWords("Hello, I'm Victor Robles"); // Returns: Robles Victor I'm Hello 
'''


text = "Hello, I'm Victor Robles"


def reverse_sentence(text:str)->str:
    reverse_text = ""
    list_text = text.split(" ")
    for x in list_text:
        reverse_text = x + " " + reverse_text 
    return reverse_text

print(reverse_sentence(text))


def reverse_sentence_refactor(text:str)->str:
    return " ".join([x for x in text.split(" ")[::-1]])

print(reverse_sentence_refactor(text))
