
''' 
Statement of Exercise 32: 
Given a text, create a function that is capable of generating 
a new text that includes only words of 4 characters or more. 

Examples: 
Filteredphrase("Hello, I'm Victor Robles, it's cold today"); 

// Returns: Hello Victor Robles, it's cold 

'''
sentence = "Hello, I'm Victor Robles, it's cold today"

def filter_sentence(sentence:str) -> str:
    filter_words = " ".join([x for x in sentence.split(" ") if len(x) >= 4  ])
    return filter_words

print(filter_sentence(sentence))