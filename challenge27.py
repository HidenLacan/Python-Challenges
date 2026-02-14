

# eu tava aqui pensando
#  imaginando o teu cheiro
# beijando a sua boca
# pra te deixar louca
# sonhei com teu sorriso
# querendo teu olhar
# querendo tua atenção
#  pra eu te falar
#

'''
Challenge 27 : search word in statement

Create a function that takes a phrase and a word as input
and check it the word exist in the sentence,Case is not a factor

Examples:
search_word("The quick brown fox jumps over the lazy dog", "fox") // Returns: true

'''
sentence = "The quick brown fox jumps over the lazy dog"
word = "fox"

def search_word(sentence:str,search_word:str) -> bool:
    sentence_list = list(sentence.split(" "))
    return search_word in sentence_list

print(search_word(sentence,word))