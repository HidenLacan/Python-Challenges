
# Statement of the Hangman game
#Create the game of hangman. 
#The user will have to guess and discover the letters of a word 
#secret, and will have 5 attempts (one attempt per limb of the human body). 
#Example: 
#HangmanGame('victor'); 
#// Exit: 
#Guess the letter: i 
#The word is: _i___ 
#You have 5 attempts left 
#*/ 

def hangman_game(word:str):
    word_list = list(word)
    structure_word = ["_"] * len(word)
    attends = 5
    # iteraction
    while attends > 0 and '_' in structure_word:
        print("The current word is:"," ".join(structure_word))
        print('Attends left:', attends)
        
        letter = input("Enter a letter: ").lower()
    # condition 
        if letter in word_list:
            print('The letter is in the word!')
            # fill structure
            for x in range(len(word_list)):
                if word_list[x] == letter:
                    structure_word[x] = letter
        else:
            print('The letter is not in the word!')
            attends -= 1
    if '_' in structure_word:
        print('You Lost! The word was:', word)
    else:
        print('You won! the word was:', word)

hangman_game("hangman")