'''
Statement of Exercise 17: 
Given an array of phrases, count the number of words it contains 
 
Examples: 
countWords([ 
"Hello, I'm Victor Robles WEB", 
"I like programming," 
"And I'm a web developer" 
            ]);
            
       Returns: 12       
''' 


def countWords(sentence:str) -> str:
    words = [x for x in sentence.split() if len(x) > 0 and x.lower() != 'a']
    return print(len(words))

sentence = "Hello, I'm Victor Robles WEB, I like programming And I'm a web developer"
countWords(sentence)