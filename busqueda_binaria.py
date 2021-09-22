def busqueda_binaria(lista, x, verbose = False):
    '''
    Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    @ author: Función compartida en curso de Python de la UNSAM
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

def donde_insertar(lista, x):
    '''
    Recibe una lista ordenada y busca a x. Si se encuentra en la lista,
    devuelve su posición; si no se encuentra, devuelve la posición en la
    que tendría que estar.
    @ author: Mariana Blanco
    '''
    pos = -1      # Inicializo respuesta, el valor no fue encontrado
    existe = 0    # Registra si se encontró x 
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio
            existe = 1       # Si encuentra a x, cambia el valor a 1 
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:                # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    if existe == 0:          # Si existe sigue en 0 es que no se encontró
        pos = izq            # a x. Toma la última posición de izq.
    return pos

def insertar(lista, x):
    '''
    Recibe una lista ordenada y busca a x. Si se encuentra en la lista,
    devuelve su posición; si no se encuentra, devuelve la posición en la
    que tendría que estar y lo inserta en ese índice.
    @ author: Mariana Blanco
    '''    
    pos = -1      # Inicializo respuesta, el valor no fue encontrado
    existe = 0    # Registra si se encontró x 
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio
            existe = 1       # Si encuentra a x, cambia el valor a 1 
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:                # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    if existe == 0:          # Si existe sigue en 0 es que no se encontró
        pos = izq            # a x. Toma la última posición de izq.
        lista.insert(pos, x) # Agrego x en la posición indicada para que respete
    return pos               # el orden de la lista
