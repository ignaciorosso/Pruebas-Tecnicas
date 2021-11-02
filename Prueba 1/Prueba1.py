# PRUEBA TECNICA #1

# En la variable 'text' disponemos de una cadena de texto
# Debes contar las palabras y devolver cuantas veces se repite cada una de ellas 
# Ejemplo ---> 'nadie' aparece dos veces


def texto_minuscula(text):
    return text.lower()

def remplazar_simbolos(text):
    return text.replace(',', '').replace('.', '')

def crear_lista(text):
    return text.split(' ')

# En esta funcion considere hacerlo con un metodo que cuanta la
# cantidad de veces que se repite la 'palabra' en la lista. 
"""
def crear_diccionario(lista):
    diccionario = {}
    for palabra in lista:
        diccionario[palabra] = lista.count(palabra)
    return diccionario
"""
# En esta funcion se utilizó un ciclo for y un condicional if. (Con ambos funciona,
# deberiamos considerar cual es el mas optimo, rapido o preciso. Dependiendo de las 
# necesidades)
def crear_diccionario(lista):
    diccionario = {}
    for palabra in lista:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario

# Bloque principal del programa

text = 'Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie imagina.'
text1 = texto_minuscula(text)
text2 = remplazar_simbolos(text1)
lista = crear_lista(text2)
diccionario = crear_diccionario(lista) 


print(f'Cantidad de veces que se repite cada palabra {diccionario}')