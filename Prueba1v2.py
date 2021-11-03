# Tomamos un fragmento de texto de un archivo con .txt

with open(r'C:\Users\Ignacio\Desktop\Prueba Tecnica\text.txt', 'r') as f:
    text = f.read()

# Procesamos el texto para dejarlo lo mas simple posible, sin simbolos ni mayusculas   

def texto_minuscula(text):
    return text.lower()

def reemplazar_simbolos(text):
    lista = [',', '.', '!', '?', '¿', '¡', ':', '(', ')']
    new_text = text
    for simb in lista:
        new_text = new_text.replace(simb, '')
    return new_text
        
def convertir_lista(text):
    return text.split()

# Cargamos las palabras en un diccionario, de esta manera podemos visualizar de un mejor modo
# la cantidad de veces que se repiten algunas palabras

def crear_diccionario(lista):
    diccionario = {}
    for palabra in lista: 
        diccionario[palabra] = lista.count(palabra)
    return diccionario

def mas_repetida(diccionario):
    mayor = 0
    for clave, valor in diccionario.items(): # items() devuelve una lista con keys y values del diccionario
        if (valor > mayor):
            mayor = valor
            palabra = clave
    return f'Palabra que mas se repite: "{palabra}", {mayor} veces.'

# Bloque principal del programa 

texto1 = texto_minuscula(text)
texto2 = reemplazar_simbolos(texto1)
lista = convertir_lista(texto2)
diccionario = crear_diccionario(lista)


print(f'Pasamos el texto a minusculas: \n{texto1}')
print(f'Reemplazamos los simbolos: \n{texto2}')
print(f'Convertimos a lista: \n{lista}')
print(diccionario)
print(mas_repetida(diccionario))