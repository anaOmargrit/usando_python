import random
import numpy as np
from matplotlib import pyplot as plt
import time
import timeit as tt

def generar_lista(N):
    """
    Genera una lista de N valores enteros entre 1 y 1000.
    """
    lista = [0] * N
    for i in range(N):
          lista[i] = random.randint(1, 1000)
    return lista

def generar_listas(Nmax):
    """
    Genera una lista de listas de 1 a Nmax valores enteros.
    """
    listas = []
    for i in range(Nmax):
        lista = generar_lista(i+1)
        listas.append(lista)
    return listas

#%% Burbujeo
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
       
    return lista

def b_recur(lista, n):
    """
    Recibe una lista y una longitud n. Intercambia los elementos de la lista
    si el de la izquierda es mayor que el de la derecha.
    """
   
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
    
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        #c += 1
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1
    #print(f'Lista ordenada por seleccion: {lista}')
    return lista

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
       
        if lista[i] > lista[pos_max]:
            pos_max = i
        
    return pos_max

#%% Ordenamiento por inserción
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
      
    return lista

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
      
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v


#%% Merge
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    
    if len(lista) < 2:        
        lista_nueva = lista
    
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    
    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    
    while(i < len(lista1) and j < len(lista2)):
        
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

        
    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado


    
#%% Timeit
def experimento_timeit(Nmax):
    """
    Evalúa con timeit el tiempo que le lleva a cada algoritmo ordenar 
    las mismas listas. 
    Recibe un número entero Nmax con la cantidad de valores enteros máxima
    que tendrá la última lista. 
    Genera al inicio una lista de listas, desde 1 a Nmax elementos.
    Devuelve un array por algoritmo con la cantidad de comparaciones que
    realizó por lista para poder ordenarla.
    """
    
    listas = generar_listas(Nmax)
    
    # Creo un array para cada algoritmo con Nmax ceros.
    timeit_burbujeo = np.zeros(Nmax)
    timeit_insercion = np.zeros(Nmax)
    timeit_seleccion = np.zeros(Nmax)
    timeit_merge = np.zeros(Nmax)
    
    global lista
    
    for i, lista in enumerate(listas):        
        # evalúo cada método de selección en una copia nueva 
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', number = 1, globals = globals())
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', number = 1, globals = globals())
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = 1, globals = globals())
        tiempo_merge = tt.timeit('merge_sort(lista.copy())', number = 1, globals = globals())
        
        # guardo el resultado del tiempo que le llevó a cada algoritmo
        # ordenar cada lista
        timeit_burbujeo[i] = tiempo_burbujeo
        timeit_insercion[i] = tiempo_insercion
        timeit_seleccion[i] = tiempo_seleccion
        timeit_merge[i] = tiempo_merge 
        
    return timeit_seleccion, timeit_insercion, timeit_burbujeo, timeit_merge
 
#%% Graficar los vectores
def graficar_timeit(v1, v2, v3, v4, Nmax):
    """
    Genera un gráfico con los vectores de los 4 algoritmos de ordenamiento
    Recibe 4 vectores en este orden: seleccion, insercion, burbujeo y merge.
    Recibe Nmax para establecer los valores en el eje x.
    """
    plt.figure(figsize=(12, 6), dpi=80)       
    plt.plot(v1, label = 'Seleccion')
    plt.plot(v2, label = 'Inserción')
    plt.plot(v3, label = 'Burbujeo')
    plt.plot(v4, label = 'Merge')
    plt.legend(loc = 'upper left')
    plt.title(f'Comparacion de ordenamiento con {Nmax} listas')
    plt.xlabel('Número de lista')
    plt.ylabel('Tiempo de ejecución')   
    plt.xticks(np.arange(0, Nmax + 1, 10))
    aux = max([max(v1), max(v2), max(v3), max(v4)]) #Elijo el valor más alto de los vectores para ticks de y
    plt.yticks(np.arange(0, aux, 0.01))
    plt.show() 
    
    
#%%
if __name__ == '__main__':
    Nmax = 300
    v1, v2, v3, v4 = experimento_timeit(Nmax)
    graficar_timeit(v1, v2, v3, v4, Nmax)