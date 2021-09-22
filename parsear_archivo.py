'''
@author: Mariana Blanco
Módulo para parsear un archivo.
'''

import csv

def parse_csv(lines, types, select = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo en una lista de registros cambiando el tipo de dato,
    y devolviendo una lista de tuplas si no tiene encabezado o una lista
    de diccionarios si tiene encabezado. Si se incluye el parámetro select (lista) es para seleccionar
    determinados encabezados.
    Parámetros:
    lines = archivo; types = [str, int]; select = ['nombre']; has_headers = True/False; silence_errors = True/False (para silenciar un error en una línea).
    '''
    lineas = csv.reader(lines)
    if has_headers == False and select:
        raise RuntimeError ("Para seleccionar, necesito encabezados.")
        
    if has_headers:
        # Si tiene, lee los encabezados en la primera línea
        encabezados =  next(lineas)
            
    if select:
        # Si le pasé encabezados, crea una lista con los índices de esos encabezados y otrs con los encabezados.
        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
        encabezados = select
    else:
        indices = [] 
            
    registros = []
    
    for i, linea in enumerate(lineas):
        try:
            # Saltea filas sin datos
            if not linea:    
                continue
                
            if indices:
                linea = [linea[index] for index in indices]
                
            if types:
                linea = tuple([func(val) for func, val in zip(types, linea)])
                    
            if has_headers:
                registro = dict(zip(encabezados, linea))
                registros.append(registro)
            else:
                registros.append(linea)
                
        except ValueError as e:
            if silence_errors == False:
                print(f'No pude convertir {linea} de la fila {i}. \nMotivo: ', e)
    
    return registros       
            
