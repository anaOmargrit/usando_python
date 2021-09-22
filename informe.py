'''
Tomando dos archivos, genera un balance de un negocio.
Se le pasar un archivo con costos y otro con ventas.
@author: Mary
'''

import csv
import fileparse
import sys

#%%
def leer_precios(archivo):  
    '''
    Recibe un archivo y crea un diccionario con nombres y precios
    '''
    rows = csv.reader(archivo)
    precios = {}        
    
    for i, row in enumerate(rows):
        try:
            precios[row[0]] = float(row[1])            
        except IndexError:
            print(f'No se comprendio la linea {i+1}')
    
    return precios

#%%
def leer_camion(archivo):
    '''
    Recibe un archivo y crea una lista de diccionarios con los datos del archivo
    '''
    camion = []
    rows = csv.reader(archivo)
    headers = next(rows)
    
    for row in rows:
        d = {
            'nombre':row[0],
            'cajones': int(row[1]),
            'precio': float(row[2])
            }
        camion.append(d)
   
    return camion 

#%%
def hacer_informe(cam, pre):
    '''
    Recibe una lista y un diccionario y crea un informe con nombre de verduras,
    cantidad de cajones, precio y costo. Devuelve una lista
    '''    
    nuevo_informe = []
    
    for c in cam:
        n = c['nombre']
        caj = c['cajones']
        cost = c['precio']
        pre_vta = pre[n]
        cambio = pre_vta - cost
        p = (n, caj, round(cost, 2), round(cambio,2))
        nuevo_informe.append(p)
    
    return nuevo_informe    

#%%
def imprimir_informe(informe):
    '''
    Recibe el informe e imprime los datos de forma ordenada.     
    '''
    print('%10s %10s %10s %10s' % ('Nombre', 'Cajones', 'Precio', 'Cambio'))    
    print('%10s %10s %10s %10s' % ('----------', '----------', '-----------', '-----------')) 
   
    for nom, cajos, prec, cambi in informe:
        precio = f'${prec}'
        print(f'{nom:>10s} {cajos:>10d} {precio:>10s} {cambi:>10.2f}')

#%%
def imprimir_balance(camion, precio):
    '''
    Recibe una lista y un diccionario y calcula el balance entre el costo y
    las ventas. Imprime el balance.
    '''    
    balance = 0.0
    total_pagado = 0.0
    total_ganado = 0.0
    
    for c in camion:
        nombre = c['nombre']
        cajones = c['cajones']
        pr = c['precio']
        total_pagado += cajones*pr
        precio_venta = precio[nombre] #busca el que coincide con la variable nombre
        total_ganado += cajones*precio_venta
   
    balance = total_ganado - total_pagado
    print(f'El balance de las ventas de la verdulería es de ${round(balance,2)}. Resulta de restar a las ganancias, ${total_ganado:0.2f}, el total pagado, ${total_pagado:0.2f}')

#%%
def informe_camion(archivo_camion, archivo_precios):
    '''
    Recibe dos archivos, llama a las funciones para obtener la información de
    cada uno y crear una lista y un diccionario. Llama a la función para hacer
    el informe y le pasa la lista de precios y el diccionario con los datos
    de la compra del camión. Llama a las funciones de imprimir el informe
    y el balance de la venta.
    '''
    camion = fileparse.parse_csv(archivo_camion, types = [str, int, float])
    precio = dict(fileparse.parse_csv(archivo_precios, types = [str, float], has_headers = False))
    informe = hacer_informe(camion, precio)
    imprimir_informe(informe)
    imprimir_balance(camion, precio)
    
#%%
def f_principal(argv):
    if len(argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]}' 'archivo_camion archivo_precios')
    camion = argv[1]
    precios = argv[2]
    informe_camion(camion, precios)
    print(informe_camion)

# Test
#if __name__ == '__main__':
#    f_principal(sys.argv)

