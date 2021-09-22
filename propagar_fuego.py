'''
Propaga el fuego: en una lista de números -1, 0 y 1; si hay un 0 junto a un 1, lo transforma en 1, lo quema.
'''

def invertir_lista(lista):
    '''
    Recibe una lista y crea una nueva con sus elementos invertidos. 
    Devuelve la lista con elementos invertidos. 
    '''
    invertida = []
    
    for e in reversed(lista):
        invertida.append(e)
    return invertida


def propagar(lista):
    '''
    Recibe una lista de -1, 0 y 1. Cambia los 0 por 1 cuando esté junto a un 1.
    Devuelve una nueva lista con los elementos modificados.
    '''
    # Transforma los 0 en 1 hacia la derecha.
    for i, n in enumerate(lista):
        if n == 0:
            if lista[i-1] == 1:
                lista[i] = 1
    lista_invertida = invertir_lista(lista)   
    
    # Invierte la lista y transforma los 0 que quedaron.
    for i, n in enumerate(lista_invertida):
        if n == 0:
            if lista_invertida[i-1] == 1:
                lista_invertida[i] = 1
                
    lista_propagada = invertir_lista(lista_invertida)    
    return lista_propagada
        
