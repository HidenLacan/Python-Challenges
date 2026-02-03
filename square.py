
'''
Statement of Exercise 16: 
Create a function that puts the phrase into a box of asterisks 
that we pass it as a parameter 
 
Examples: 
showTextBox('Hello, I'm Victor Robles WEB'); 
 
********** 
* Hello  * 
* soy    * 
* Victor * 
* Robles * 
* WEB    * 
********** 
 
*/ 
'''

def showTextBox(sentence:str) -> str:
    words = sentence.split()
    max_len = len(max(words,key=len))
    for row in range(0,len(words) + 2):
        if row == 0 or row == len(words)+1:
            print( "*" * (max_len + 4))
        else:
            word = words[row -1]
            print( "* " + word + " " * (max_len - len(word)) + " *")
        

showTextBox("Hello soy Luis")