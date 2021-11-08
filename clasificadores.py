from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import statistics

import pandas as pd

def comparaciones(n):
    """
    Recibe un número entero n que será la cantidad de veces que repetirá
    el fit y score de cada clasificador.
    Devuelve el promedio obtenido por cada tipo.
    """
    iris_dataset = load_iris()
    iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
    iris_dataframe['target'] = iris_dataset['target']
    
    p_clf = []
    p_knn = []
    p_rfk = []
  
    for i in range(n):
        # Hace la partición del dataset en train y test
        X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'])
        
        # Crea un objeto de cada clasificador
        clf = DecisionTreeClassifier()
        knn = KNeighborsClassifier(n_neighbors = 1)
        rfk = RandomForestClassifier()
     
        # Entrena cada modelo
        clf.fit(X_train, y_train)
        knn.fit(X_train, y_train)
        rfk.fit(X_train, y_train)
    
        # Evaluación de cada clasificador
        c = clf.score(X_test, y_test)  
        k = knn.score(X_test, y_test)
        f = rfk.score(X_test, y_test)
        
        # Agregamos el score de cada uno en su lista
        p_clf.append(c)
        p_knn.append(k)    
        p_rfk.append(f)
      
    # Obtenemos los promedios por modelo
    promedio_clf = statistics.mean(p_clf)
    promedio_knn = statistics.mean(p_knn)
    promedio_rfk = statistics.mean(p_rfk)
  
    return promedio_knn, promedio_clf, promedio_rfk

#%%
if __name__ == '__main__':
    n = 100
    r_knn, r_clf, r_rfk = comparaciones(n)
    print('El promedio de KNeighborsClassifier es: {:.2f}'.format(r_knn))
    print('El promedio de DecisionTreeClassifier es: {:.2f}'.format(r_clf))
    print('El promedio de RandomForestClassifier es: {:.2f}'.format(r_rfk))