'''
Uso de matplotlib para comparar datos. 
@ author: Mariana Blanco
'''
import csv
import os
import matplotlib.pyplot as plt
import numpy as np

def leer_arboles(nombre_archivo):
    '''
    Recibe un archivo csv con un listado de árboles de la ciudad de Buenos Aires.
    Devuelve una lista de diccionarios con los datos de cada registro.
    '''
    arboleda = []    
    with open(nombre_archivo, 'rt', encoding="utf-8") as f:
        filas = csv.reader(f)
        encaezados = next(filas)
        for i, fila in enumerate(filas, start = 1): 
            registro = dict(zip(encabezados, fila))
            arboleda.append(registro)                
    
    return arboleda 

  
def hacer_historiograma(lista_de_arboles):
    '''
    Genera un historiograma con la altura de un determinado árbol.
    '''
    altos = [float(arbol['altura_tot']) for arbol in lista_de_arboles if arbol['nombre_com'] == 'Jacarandá' ]
    plt.hist(altos,bins=30)
    plt.show()

    
def scatter_hd(lista_de_pares, especie, label):
    '''
    Genera un diagrama de dispersión con los diámetros y alturas de una especie de árboles. 
    Recibe una lista de diámetros y alturas; la especie; un color. 
    Genera el diagrama.
    '''
    pares = np.array(lista_de_pares)
    
    # Paso el array y saca todas las filas(:) de la columna 0
    h = pares[:,0] 
    
    # Paso el array y saca todas las filas(:) de la columna 1
    d = pares[:,1]  
    
    N = len(lista_de_pares)
    area = (10 * np.random.rand(N))**2  
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto " + especie)
    plt.scatter(d,h, s = area, alpha = 0.3, label = label)
    plt.show()

    
def medidas_de_especies(especies, arboleda):
    '''
    Recibe una lista de especies y el documento con los datos.
    Devuelve un diccionario con las medidas de las especies que se le pasan.
    '''
    diccionario = {}    
    for especie in especies:
        e = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie]
        diccionario[especie] = e
    
    return diccionario

  
def scatter_por_especie(dict_medidas, especie, label):
    '''
    Recibe un diccionario con los datos de las especies, y una lista de especies.
    Label es la especie que se quiere mostrar.
    Realiza un scatterplot para esa especie.
    ''' 
    for key in dict_medidas.keys():        
        if key == especie:
            medidas_especie = dict_medidas[key]
            scatter_hd(medidas_especie, especie, label = especie)

            
def scatter_tres_especies(dict_medidas, especies):
    '''
    Recibe un diccionario con los datos de las especies, y una lista de especies.
    Realiza un scatterplot para la lista de especies.
    '''   
    for especie in especies:
        medidas = dict_medidas[especie]
        scatter_hd(medidas, '', label=especie)
        

def test_grafico_una_especie():
    os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)
    grafico_una_especie = scatter_por_especie(medidas, 'Jacarandá', 'Jacarandá')    
    

def test_tres_especies():
    os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)        
    grafico_todas = scatter_tres_especies(medidas, especies)

# Test, descomentar para probar una opción.
#if __name__ == "__main__":
    #test_grafico_una_especie()
    #test_tres_especies()    
    
