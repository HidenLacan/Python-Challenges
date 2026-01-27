


'''
Statement of Exercise 14: 
Given a string of text, check if it is a palindrome or not. Do not use functions of 
JavaScript, only control structures 
 
Palindromes are words that read the same even when reversed. 
For example: Ana, Bob, Otto, AllivesSevilla 
 
Examples: 
isPalindrome("otto") // Returns: true 
isPalindrome("victor") // Returns: false 
'''
def check_palindromo(word:str)->str:

    word_comparition = ""

    for letter in word:
        word_comparition = letter + word_comparition
        
    if word_comparition.lower() == word.lower():
        return print("Es palindromo")
    else:
        return print("No es palindromo")

word = 'AllivesSevilla'
check_palindromo(word)