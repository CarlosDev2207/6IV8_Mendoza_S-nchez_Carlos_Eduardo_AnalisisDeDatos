import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.spatial import distance

#Definimos las coordenasdas de las tiendas

tiendas={
    'Tienda A':(1,1),
    'Tienda B':(1,5),
    'Tienda C':(7,1),
    'Tienda D':(3,3),
    'Tienda E':(4,8)
}

#Convertir las coordenadas a un dateframe
df_tiendas= pd.DataFrame(tiendas).T
df_tiendas.columns =['X', 'Y']
print('Coordenasdas de las tiendas: ')
print(df_tiendas)

#inicializamos una distancia euclidiana
distancias_eu=pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)
distancias_mh=pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)
distancias_ch=pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)

#calculo de las distancias
for i in df_tiendas.index:
    for j in df_tiendas.index:
        #distancia Euclidiana
        distancias_eu.loc[i, j]=distance.euclidean(df_tiendas.loc[i], df_tiendas.loc[j])
        #distancia Manhattan
        distancias_mh.loc[i, j]=distance.euclidean(df_tiendas.loc[i], df_tiendas.loc[j])
        distancias_ch.loc[i, j]=distance.chebyshev(df_tiendas.loc[i], df_tiendas.loc[j])

#Mostrar resultados
print("\nDistancias Euclideanas entre las tiendas")
print(distancias_eu)
print("\nDistancias Manhattan entre las tiendas")
print(distancias_mh)
print("\nDistancias Chebyshev entre las tiendas")
print(distancias_ch)

