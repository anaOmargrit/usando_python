# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 19:41:29 2021

@author: Mary

Evalúa con comparaciones la eficiencia de diferentes algoritmos de ordenamiento en Python.
"""
import random
import numpy as np
from matplotlib import pyplot as plt

def generar_lista(N):
    """
    Genera una lista de N valores enteros entre 1 y 1000.
    """
    lista = [0] * N
    for i in range(N):
          lista[i] = random.randint(1, 1000)
    return lista

#%% Burbujeo
def ord_burbujeo(lista):
    """Ordena una lista de elementos según el método de burbujeo.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada.
    """
    n = len(lista) - 1    
    c = 0
    while n > 0:
        # Llama a la función recursiva y le pasa la lista y una longitud.        
        lista, c = b_recur(lista, n, c)
        # Resta un valor a la longitud, para que cada llamado a la recursiva 
        # compare los valores del index 0 al n - 1, así no vuelve a comparar
        # el mayor que queda en el index n.
        n-=1
        
        #print(c)
    #print(f'Lista ordenada por burbujeo: {lista}')
    return c

def b_recur(lista, n, c):
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
        c +=1
    return lista, c


def intercambiar(lista, i):
    """Intercambia al elemento que está en la posición i de la lista
       con el siguiente.
       Pre: i tiene que ser una posicion válida de lista."""
    v = lista[i]         # Este es el mayor
    aux = lista[i + 1]   # Guardo en una auxiliar el menor
    lista[i + 1] = v     # Guardo el mayor en la posición de la derecha
    lista[i] = aux       # Guardo el menor en la posición de la izquierda
    
#%% 12.2 Ordenamiento por selección
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    c = 0
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        #c += 1
        # posición del mayor valor del segmento
        p, c = buscar_max(lista, 0, n, c)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1
    #print(f'Lista ordenada por seleccion: {lista}')
    return c

def buscar_max(lista, a, b, c):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        c += 1
        if lista[i] > lista[pos_max]:
            pos_max = i
        
    return pos_max, c

#%% Ordenamiento por inserción
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    c = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
           c = reubicar(lista, i + 1, c)
        c += 1
        #print("DEBUG: ", lista)
    #print(f'Lista ordenada por insercion: {lista}')
    return c

def reubicar(lista, p, c):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        c += 1
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
    return c

#%% Ordenamiento Merge
def merge_sort(lista, c = 0):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    
    if len(lista) < 2:
        c += 1
        lista_nueva = lista
    
    else:
        medio = len(lista) // 2
        izq, c = merge_sort(lista[:medio], c)
        der, c = merge_sort(lista[medio:], c)
        lista_nueva, c = merge(izq, der, c)
    
    return lista_nueva, c

def merge(lista1, lista2, c):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    
    while(i < len(lista1) and j < len(lista2)):
        c += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

        
    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado, c

#%% Experimento

def experimento(N, k):
    """
    Evalúa con la cantidad de comparaciones la eficiencia de cada algoritmo
    para ordenar las mismas listas. 
    Recibe un número entero N con la cantidad de valores enteros
    que tendra la lista lista y un entero k con la cantidad de veces
    que va a repetir el experimento. 
    Saca y devuelve un promedio de compataraciones por algoritmo.
    """
    lista = generar_lista(N)
    k_aux = k
    c_insercion = 0
    c_seleccion = 0 
    c_burbujeo = 0
    c_merge = 0
    
    while k > 0:
        c_burbujeo += ord_burbujeo(lista.copy())
       # print(f'Lista ordenada x burbujeo llevó {c_burbujeo} comparaciones en la vuelta {k}.')

        c_insercion += ord_insercion(lista.copy())
       # print(f'Lista ordenada x insercion llevó {c_insercion} comparaciones en la vuelta {k}.')
        
        c_seleccion += ord_seleccion(lista.copy())
       # print(f'Lista ordenada x seleccion llevó {c_seleccion} comparaciones e la vuelta {k}.')
        
        c_merge += merge_sort(lista.copy())[1]
        k -= 1
    
    #print(c_insercion, c_seleccion, c_burbujeo, c_merge)
    prom_burbujeo = c_burbujeo/k_aux
    prom_insercion = c_insercion/k_aux
    prom_seleccion = c_seleccion/k_aux
    prom_merge = c_merge/k_aux
    
    #print(prom_burbujeo, prom_insercion, prom_seleccion, prom_merge)
    return prom_burbujeo, prom_insercion, prom_seleccion, prom_merge
    
    
#%% Gráficos
def experimento_vectores(Nmax):
    """
    Evalúa con la cantidad de comparaciones la eficiencia de cada algoritmo
    para ordenar las mismas listas.
    Recibe un número entero Nmax con la cantidad de valores enteros máxima
    que tendrá la última lista. 
    Genera al inicio una lista de listas, desde 1 a Nmax elementos.
    Devuelve un array por algoritmo con la cantidad de comparaciones que
    realizó por lista para poder ordenarla.
    """
    comparaciones_burbujeo = np.zeros(Nmax)
    comparaciones_insercion = np.zeros(Nmax)
    comparaciones_seleccion = np.zeros(Nmax)
    comparaciones_merge = np.zeros(Nmax)
    
    for n in range(Nmax):
        #print(f'Estoy en la vuelta {n} de {Nmax}')
        aux = n+1
        lista = generar_lista(aux)
        #print(f'La lista es: {lista}')
        comparaciones_burbujeo[n] = ord_burbujeo(lista.copy())     
        #print(f'Array de burbujeo: {comparaciones_burbujeo}')
        comparaciones_insercion[n] = ord_insercion(lista.copy())  
        #print(f'Array de insercion: {comparaciones_insercion}')
        comparaciones_seleccion[n] = ord_seleccion(lista.copy())
        #print(f'Array de seleccion: {comparaciones_seleccion}')
        comparaciones_merge[n] = merge_sort(lista.copy())[1]
        
    return comparaciones_seleccion, comparaciones_insercion, comparaciones_burbujeo, comparaciones_merge

#%% Graficar los vectores
def graficar_comparaciones(v1, v2, v3, v4, Nmax):
    """
    Genera un gráfico con los vectores de los 4 algoritmos de ordenamiento.
    Recibe 4 vectores en este orden: seleccion, insercion, burbujeo y merge.
    Recibe Nmax para establecer los valores en el eje x.
    """
    plt.figure(figsize=(12, 6), dpi=80)       
    plt.plot(v1, label = 'Seleccion', linestyle = 'dotted')
    plt.plot(v2, label = 'Inserción')
    plt.plot(v3, label = 'Burbujeo')
    plt.plot(v4, label = 'Merge')
    plt.legend(loc = 'upper left')
    plt.title(f'Comparacion de ordenamiento con {Nmax} listas')
    plt.xlabel('Cantidad de listas')
    plt.ylabel('Cantidad de repeticiones')   
    plt.xticks(np.arange(0, Nmax + 1, step = Nmax//10))
    aux = max([max(v1), max(v2), max(v3), max(v4)]) #Elijo el valor más alto de los vectores para ticks de y
    plt.yticks(np.arange(0, aux + 1, step = aux//10))
    plt.show()  

    
#%%
if __name__ == '__main__':
    Nmax = 300
    v1, v2, v3, v4 = experimento_vectores(Nmax)
    graficar_comparaciones(v1, v2, v3, v4, Nmax)
