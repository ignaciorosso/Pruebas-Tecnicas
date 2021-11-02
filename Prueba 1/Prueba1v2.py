

text = "Supongamos un texto bien escrito, donde no tengamos tanto lio. ¿Que pasaria? Seguramente, ¡Nada!"

def texto_minuscula(text):
    return text.lower()

def reemplazar_simbolos(text):
    lista = [",", ".", '!', '?', '¿', '¡']
    new_text = text
    for simb in lista:
        new_text = new_text.replace(simb, '')
    return new_text
        
def convertir_lista(text):
    return text.split()

texto1 = texto_minuscula(text)
texto2 = reemplazar_simbolos(texto1)
lista = convertir_lista(texto2)

print(f'Pasamos el texto a minusculas: \n{texto1}')
print(f'Reemplazamos los simbolos: \n{texto2}')
print(f'Convertimos a lista: \n{lista}')