def pascal(n, k):
    '''
    Recibe dos numeros enteros y devuelve el valor que se encuentra
    en esa celda de un triángulo de pascal.
    n representa cantidad de filas
    k represeta cantidad de columnas
    '''
    #print(f'Entre a pascal con {n} y {k}')
    # Caso base 1, si la cantidad de filas es igual a la cantidad de columnas es 1
    if n == k:
        #print(f'Caso base {n} es igual a {k}')
        res = 1
    
    # Caso base 2, si la cantidad de columnas es 0, es la primera celda y su valor es 1
    elif k == 0:
        #print(f'Caso base {k} es igual a cero')
        res = 1
    
    else:
        # Se llama a sí misma para conocer el valor de "arriba" de una columna anterior
        aux1 = pascal(n-1, k-1)
        #print(f'Esto es aux1: {aux1}')
        
        # Se llama a sí misma para conocer el valor de "arriba" de la misma columna
        aux2 = pascal(n-1, k)
        #print(f'Esto es aux2: {aux2}')
        
        # Suma ambos valores
        res = aux1 + aux2
        #print(f'El resultado: {res}')
        
    return res
