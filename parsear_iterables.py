#Ejercicio 7.6 que lea objetos iterables
import csv

def parse_csv(lines, types = None, select = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo en una lista de registros cambiando el tipo de dato,
    y devolviendo una lista de tuplas si no tiene encabezado o una lista
    de diccionarios si tiene encabezado. El parámetro select es para seleccionar
    determinados encabezados.
    '''
    lineas = csv.reader(lines)
    if has_headers == False and select:
        raise RuntimeError ("Para seleccionar, necesito encabezados.")
        
    if has_headers:
        # Si tiene, lee los encabezados e la primera línea
        encabezados =  next(lineas)
    else:
        encabezados = []
            
    if select:
        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
        encabezados = select
    else:
        indices = [] 
            
    registros = []
    for i, linea in enumerate(lineas):
        try:
            if not linea:    # Saltea filas sin datos
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
            
#Prueba
#with open('../Data/camion.csv') as f:
#    filas = parse_csv(f, types=[str,int,float])
#print(filas)

#with open('../Data/precios.csv') as f:
#    filas = parse_csv(f, types=[str,float], has_headers = False)
#print(filas)

#lines = ['nombre,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
#camion = parse_csv(lines, types=[str,int,float])

#camion1 = parse_csv('../Data/camion.csv', types=[str,int,float])
#print(camion1)

