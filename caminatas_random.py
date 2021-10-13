import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    '''
    Recibe un número entero n y genera una lista de n
    cantidad de números aleatorios
    '''
    pasos=np.random.randint (-1,2,largo) 
    return pasos.cumsum()


def valor_absoluto(trayectoria):
    '''
    Recibe una lista de enteros positivos y negativos y devuelve
    una lista con los absolutos
    '''
    nueva_trayectoria = []
    
    for paso in trayectoria:
        if paso >= 0:
            nueva_trayectoria.append(paso)
        else:
            nueva_trayectoria.append(-paso)   
    
    return nueva_trayectoria


def graficar_trayectorias(cantidad_trayectorias, cantidad_pasos):
    '''
    Recibe dos valores enteros, la cantidad de trayectorias a mostrar (c) y
    la cantidad de pasos (p).
    Grafica c cantidad de trayectorias.
    Grafica la trayectoria que menos se alejó.
    Grafica la trayectoria que más se alejó
    '''
    
    menos_aleja = cantidad_pasos + 1
    mas_aleja = -1
    
    a_graficar_menos_aleja = []
    a_graficar_mas_aleja = []
    
    #Variables para control de funcionamiento
    #contador = 1
    #r1 = 0
    #r2 = 0    
    
    # Crea una figura nueva, de 8x6 pulgadas, con 80 puntos por pulgada
    plt.figure(figsize=(12, 6), dpi=80)
        
    while cantidad_trayectorias > 0: 
       
        # Define la figura de arriba                 
        plt.subplot(2, 1, 1)     
        
        # Genera la trayectoria
        trayectoria = randomwalk(cantidad_pasos)        
        #print('Trayectoria ', contador)
        
        # Grafica la trayectoria
        plt.plot(trayectoria)
        plt.xlabel('Tiempo')
        plt.ylabel('Distancia al origen')
        plt.title('Trayectorias de las caminatas')
        plt.xticks([])
        plt.ylim(-750, 750)
        plt.yticks(np.linspace(-500, 500, 3))        
        
        # Convierte la trayectoria en absolutos y en un array para buscar el max
        #trayectoria_absoluta = valor_absoluto(trayectoria)
        #array_trayectoria = np.array(trayectoria_absoluta)
        #paso_mas_lejos = array_trayectoria.max()
        #print(paso_mas_lejos)

        # Convierte el vector en absolutos y busca el mayor         
        paso_mas_lejos = (abs(trayectoria)).max()
        print(paso_mas_lejos)
        # Busca la trayectoria que más se alejó    
        if paso_mas_lejos > mas_aleja:
            a_graficar_mas_aleja = trayectoria
            mas_aleja = paso_mas_lejos
            #r2 = contador
            
        # Busca la trayectoria que menos se alejó 
        if paso_mas_lejos < mas_aleja:
            if paso_mas_lejos < menos_aleja:
                a_graficar_menos_aleja = trayectoria
                menos_aleja = paso_mas_lejos
                #r1 = contador
        
        cantidad_trayectorias -=1
        #contador += 1
        
    #print('Menos final: ', menos_aleja, 'Trayectoria: ', r1)
    #print('Mas final: ', mas_aleja, 'Trayectoria: ', r2)
    
    # Grafica la trayectoria que más se aleja
    plt.subplot(2, 2, 3)
    plt.plot(a_graficar_mas_aleja, color="red")
    plt.xticks([])
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia al origen')
    plt.title('Caminata que más se aleja')
    plt.xticks([])
    plt.ylim(-750, 750)
    plt.yticks(np.linspace(-500, 500, 3))
    
    # Grafica la trayectoria que menos se aleja
    plt.subplot(2, 2, 4)
    plt.plot(a_graficar_menos_aleja, color="blue")
    plt.xticks([])
    plt.xlabel('Tiempo')
    plt.ylabel('Distancia al origen')
    plt.title('Caminata que menos se aleja')
    plt.xticks([])
    plt.ylim(-750, 750)
    plt.yticks(np.linspace(-500, 500, 3)) 
    plt.show()                    

if __name__ == '__main__':
    cantidad_trayectorias = 12
    cantidad_pasos = 100000
    graficar_trayectorias(cantidad_trayectorias, cantidad_pasos)

#%% Otra forma de trabajar la repeciciones
# No se si me queda claro, cualquier cosa esta en el video de la clase 8

def repeticiones(n):
    caminatas = [randomwalk(n) for i in range(n)]
    distancias = [max(abs(caminata)) for caminata in caminatas]
    
    # Devuelve 2 array: uno con los máximos y otro con lso mínimos
    return caminatas[np.argmin(distancias)], caminatas[np.argmax(distancias)]

t = repeticiones(10)
print(t)

caminatas = [randomwalk(10) for i in range(10)]
distancias = [max(abs(caminata)) for caminata in caminatas]

# Genera el array y toma el mayor luego de convertirlo en absolutos
caminata = randomwalk(100)
h = max(abs(caminata))























