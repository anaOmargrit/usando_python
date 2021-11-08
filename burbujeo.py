#%% Ejercicio 12.2: burbujeo
def ord_burbujeo(lista):
    """Ordena una lista de elementos según el método de burbujeo.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada.
    """
    n = len(lista) - 1    

    while n > 0:
        # Llama a la función recursiva y le pasa la lista y una longitud.        
        lista = b_recur(lista, n)
        # Resta un valor a la longitud, para que cada llamado a la recursiva 
        # compare los valores del index 0 al n - 1, así no vuelve a comparar
        # el mayor que queda en el index n.
        n-=1
        #print(n)
    return lista

def b_recur(lista, n):
    """
    Recibe una lista y una longitud n. Intercambia los elementos de la lista
    si el de la izquierda es mayor que el de la derecha.
    """
    #print(f'Estoy en recur con {n} elementos')
    for i in range(n):
        # Si el elemento en la posición i es mayor que el siguiente, llama
        # a la función intercambiar y le pasa la lista y el index del elemento mayor.
        if lista[i] > lista[i + 1]:
            intercambiar(lista, i)            
        #print("DEBUG: ", lista)
    return lista


def intercambiar(lista, i):
    """Intercambia al elemento que está en la posición i de la lista
       con el siguiente.
       Pre: i tiene que ser una posicion válida de lista.
    """
    v = lista[i]         # Este es el mayor
    aux = lista[i + 1]   # Guardo en una auxiliar el menor
    lista[i + 1] = v     # Guardo el mayor en la posición de la derecha
    lista[i] = aux       # Guardo el menor en la posición de la izquierda