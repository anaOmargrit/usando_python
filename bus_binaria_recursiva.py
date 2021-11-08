def bbinaria_rec(lista, e):
    '''
    Recibe una lista ordenada de enteros y un número.
    Devuelve True si ese numero se encuentra en la lista y False
    si no lo encuentra.
    '''
    #print(f'Entra con lista: {lista}')
    # Caso base 1, la lista no tiene elementos
    if len(lista) == 0:
        #print('Caso base la lista no tiene elementos')
        res = False
    
    # Caso base 2, la lista tiene 1 elemento y ese elemento es igual a e    
    elif len(lista) == 1:
        #print('Caso base la lista tiene 1 elemento')
        res = lista[0] == e
        
    else:
        #print('Recursiva...')
        # Calcula el valor medio de la lista
        medio = len(lista)//2
        
        # Si en el index del medio esta e, devuelve True
        if lista[medio] == e:
            #print('Lo encontre')
            res = True
            return res    
        
        # Si e es menor que el valor que está en el index del medio, pasa la lista
        # con los valores desde el 0 al index del medio
        if lista[medio] > e:
            #print(f'{e} es menor que {medio}')
            res = bbinaria_rec(lista[:medio], e)
            
        # Si e es mayor que el valor que está en el index del medio, pasa la lista
        # con los valores desde el index que sigue al del medio hasta el último    
        else:              
            #print(f'{e} es mayor que {medio}')
            res = bbinaria_rec(lista[medio+1:], e)

    return res
