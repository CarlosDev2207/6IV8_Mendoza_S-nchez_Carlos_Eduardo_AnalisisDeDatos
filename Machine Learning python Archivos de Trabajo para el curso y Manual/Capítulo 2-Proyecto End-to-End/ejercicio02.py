"""calculemos las distancias entre todos los pares de puntos y determinaremos cuales estan más alejados entre sí y
cuales estan mas cercanos utilizando las distancias Euclidiana, Manhattan y Chebyshev"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.spatial import distance

puntos = {
    'Punto A': (2, 3),
    'Punto B': (5, 4),
    'Punto C': (1, 1),
    'Punto D': (6, 7),
    'Punto E': (3, 5),
    'Punto F': (8, 2),
    'Punto G': (4, 6),
    'Punto H': (2, 1)
}

# Convertir las coordenadas a un dataframe
df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X', 'Y']
print('Coordenadas de los puntos:')
print(df_puntos)

def calcular_distancias(df_puntos, metodo):
    distancias = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
    for i in df_puntos.index:
        for j in df_puntos.index:
            if i != j:
                if metodo == 'euclidiana':
                    distancias.loc[i, j] = distance.euclidean(df_puntos.loc[i], df_puntos.loc[j])
                elif metodo == 'manhattan':
                    distancias.loc[i, j] = distance.cityblock(df_puntos.loc[i], df_puntos.loc[j])
                elif metodo == 'chebyshev':
                    distancias.loc[i, j] = distance.chebyshev(df_puntos.loc[i], df_puntos.loc[j])
    return distancias.astype(float)

distancias_euclidiana = calcular_distancias(df_puntos, 'euclidiana')
distancias_manhattan = calcular_distancias(df_puntos, 'manhattan')
distancias_chebyshev = calcular_distancias(df_puntos, 'chebyshev')

for nombre, distancias in [('Euclidiana', distancias_euclidiana), ('Manhattan', distancias_manhattan), ('Chebyshev', distancias_chebyshev)]:
    max_value = distancias.values.max()
    punto1, punto2 = distancias.stack().idxmax()
    print(f'\nTabla de distancias {nombre}:')
    print(distancias)
    print(f'Distancia máxima ({nombre}): {max_value} entre {punto1} y {punto2}')
