import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.spatial import distance

#Calcularemos las distancias entre todos los pares de puntos y determinaremos cuáles están más alejados entre sí y cuáles están más cercanos, utilizando las distancias Euclidiana, Manhattan y Chebyshev.
#Ejercicio: Determinación de Distancias entre Puntos
#Puntos en el Plano

#Los puntos en el plano son los siguientes:

#    Punto A: (2, 3)
#   Punto B: (5, 4)
#    Punto C: (1, 1)
#    Punto D: (6, 7)
#    Punto E: (3, 5)
#    Punto F: (8, 2)
#    Punto G: (4, 6)
#    Punto H: (2, 1)


# Definimos las coordenadas de los puntos en el plano
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

# Convertir las coordenadas a un DataFrame
df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X', 'Y']
print('Coordenadas de los puntos:')
print(df_puntos)

# Inicializamos matrices para las distancias
distancias_eu = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
distancias_mh = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
distancias_ch = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)

# Cálculo de las distancias para cada par de puntos
for i in df_puntos.index:
    for j in df_puntos.index:
        # Distancia Euclidiana
        distancias_eu.loc[i, j] = distance.euclidean(df_puntos.loc[i], df_puntos.loc[j])
        # Distancia Manhattan (utilizamos cityblock)
        distancias_mh.loc[i, j] = distance.cityblock(df_puntos.loc[i], df_puntos.loc[j])
        # Distancia Chebyshev
        distancias_ch.loc[i, j] = distance.chebyshev(df_puntos.loc[i], df_puntos.loc[j])

# Mostrar resultados de las matrices de distancia
print("\nDistancias Euclidianas entre los puntos:")
print(distancias_eu)
print("\nDistancias Manhattan entre los puntos:")
print(distancias_mh)
print("\nDistancias Chebyshev entre los puntos:")
print(distancias_ch)

# Función para determinar la menor y mayor distancia (ignorando la diagonal)
def encontrar_min_max(dist_df):
    # Convertir a float y reemplazar la diagonal (donde la distancia es cero) por NaN para ignorarla
    d = dist_df.copy().astype(float)
    np.fill_diagonal(d.values, np.nan)
    min_val = d.min().min()
    max_val = d.max().max()
    min_pair = d.stack().idxmin()
    max_pair = d.stack().idxmax()
    return min_val, min_pair, max_val, max_pair

# Determinar los pares de puntos más cercanos y más alejados para cada tipo de distancia
min_eu, min_pair_eu, max_eu, max_pair_eu = encontrar_min_max(distancias_eu)
min_mh, min_pair_mh, max_mh, max_pair_mh = encontrar_min_max(distancias_mh)
min_ch, min_pair_ch, max_ch, max_pair_ch = encontrar_min_max(distancias_ch)

print("\nResultados de las distancias:")
print("Euclidiana -> Menor distancia:", min_eu, "entre", min_pair_eu, 
      " | Mayor distancia:", max_eu, "entre", max_pair_eu)
print("Manhattan  -> Menor distancia:", min_mh, "entre", min_pair_mh, 
      " | Mayor distancia:", max_mh, "entre", max_pair_mh)
print("Chebyshev  -> Menor distancia:", min_ch, "entre", min_pair_ch, 
      " | Mayor distancia:", max_ch, "entre", max_pair_ch)
