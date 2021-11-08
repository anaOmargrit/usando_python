def medidas_hoja_A(N):
    '''
    Para una entrada N mayor que cero, devuelve una tupla con
    el ancho y el largo de la hoja A(N). 
    '''
    # Caso base
    if N == 0:
        res = (841, 1189)
    
    else:
        # Se llama a sí misma hasta llegar a 0         
        res = medidas_hoja_A(N-1)
        
        # Calcula el valor hasta llegar al de la hoja A(N) 
        res = (res[1]//2, res[0])
        #print(res)
        
    return res