# -*- coding: utf-8 -*-
"""
Este módulo permite procesar, renombrar y trasladar archivos de extensión 'png' de uno o varios directorios a otro.
Los archivos usados tenían la fecha de acceso en el mismo nombre. 
"""
import os
import sys
import datetime
import shutil
from datetime import datetime

def obtener_fecha(nombre_archivo: str):
    '''
    Recibe el nombre del archivo. Obtiene y devuelve esa fecha.
    '''
    a = list(nombre_archivo)
    fecha = [int(c)for c in a if c.isdigit()]
    fecha = [str(n) for n in fecha]
    fecha = ''.join(fecha)
    fecha = datetime.strptime(fecha, '%Y%m%d')
    return fecha


def nombre_nuevo(archivo):
    '''
    Recibe el nombre de un archivo y lo modifica quitando
    numeros y _. Devuelve el nombre nuevo. 
    '''
    nombre_nuevo = archivo.split('.')[0][:-8]  + '.png'
    nombre_nuevo = nombre_nuevo.replace('_', '')
    print('Nuevo nombre: ', nombre_nuevo)
    return nombre_nuevo


def procesar(directorio_origen, directorio_destino):
    '''
    Recibe un directorio de origen, selecciona y procesa los archivos png
    y los envía al directorio de destino
    '''    
    archivos_png = [] 
    
    # Crea el directorio de destino si no existe
    existe = os.path.isdir(directorio_destino)
    if existe == False:
        os.mkdir(directorio_destino)    
        #print('Creé la carpeta')
    
    # Recorro los directorios y archivos
    for root, dirs, files in os.walk(directorio_origen, topdown = False):         
        for file in files:
            nombre, extension = os.path.splitext(file)          
            if extension == '.png':
                #print('Estoy revisando el archivo: ', nombre)            
                
                # Obtener fecha del nombre del archivo
                fecha_archivo =  obtener_fecha(file)
                
                # Editar fecha
                procesar_fecha(fecha_archivo, os.path.join(root, file))
                
                # Editar nombre
                nombre_editado = nombre_nuevo(file)      
            
                archivos_png.append(nombre_editado)
                
                # Cambia el nombre
                os.rename(os.path.join(root, file), nombre_editado)
                
                # Mueve el archivo desde la ubicación actual al directorio_destino
                shutil.move(nombre_editado, directorio_destino)
                
    # Devuelve la lista con los archivos que fueron procesados y trasladados      
    return archivos_png

    
def procesar_fecha(fecha, path_archivo):
    '''
    Recibe una fecha y el path del archivo y le modifica la ultima fecha
    de acceso y modificación
    '''
    #print('Estoy procesando la fecha:', path_archivo)                   
    fecha_acceso = datetime.now().timestamp()
    fecha_modifi = fecha.timestamp()           
    os.utime(path_archivo, (fecha_acceso, fecha_modifi))
 

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'directorio_origen' 'directorio_destino')
    directorio_origen = sys.argv[1]
    directorio_destino = sys.argv[2]
    print(directorio_origen, directorio_destino)
    lista_archivos_png = procesar(directorio_origen, directorio_destino)
    print(lista_archivos_png)
    print('Terminado')

    
