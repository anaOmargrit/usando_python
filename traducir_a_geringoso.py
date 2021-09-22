'''
Recibe una lista de palabras y genera un diccionario de las mismas palabras traducidas al geringoso.
@author: Mariana Blanco
'''
lista = ['banana', 'manzana', 'mandarina']

def diccionario_geringoso(lista):
    nueva_lista = []    
    
    for palabra in lista:
        npalabra = ''        
        for c in palabra:
            npalabra += c
            
            if c in 'aeiou':
                npalabra += 'p' + c
            
            elif c in 'AEIOU':
                npalabra += 'P' + c
        
        nueva_lista.append(npalabra)
    d = dict(zip(lista, nueva_lista))
    
    return d
