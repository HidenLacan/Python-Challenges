'''
Statement of Exercise 12: 
Create a program that counts the words in a text 
'''
phrase= "Saint Roch's dog has no tail because he's a very , very bad dog"

def count_word_list(phrase : str) -> dict:
    list_words = phrase.split(" ")
    dictionary_words = {}
    
    for words in list_words:
        
        if words in dictionary_words:
            dictionary_words[words] += 1
        else:
            dictionary_words[words] = 1
    return print (dictionary_words)

count_word_list(phrase)