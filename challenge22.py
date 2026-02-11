'''
Statement of Exercise 22: 
Create a function that reverses the order of a text 
without using native language functions. 
'''

def invertir_largo(text:str) ->str:
    
    resultado = ""
    for i in text:
        resultado = i + resultado
        
    return resultado

def invertir(text:str) -> str:
    
    return text[::-1]


print(invertir_largo("hola"))