import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

#mostrar las primeras 5 filas
print(df.head())


#mostrar las ultimas 5 filas
print(df.tail())

#mostrar una fila en especifico
print(df.iloc[7])

#mostrar la columna ocean_proximity
print(df["ocean_proximity"])

#Obtener la media de la columna total_rooms
mediadecuarto = df["total_rooms"].mean()
print('La media de cuartos es: ', mediadecuarto)

#mediana
medianadecuarto = df['median_house_value'].median()
print('La mediana de la columna valor mediana de la casa: ', medianadecuarto)

#la suma de popular
salariototal = df['population'].sum()
print('el salario total es de: ', salariototal)

#para poder filtrar
vamosahacerunfiltro = df[df['ocean_proximity'] == 'ISLAND']
print(vamosahacerunfiltro)


#vamos a hacer un grafico de dispercion
plt.scatter(df['ocean_proximity'][:10], df['median_house_value'][:10])

#nombramos los ejes
plt.xlabel("proximidad")
plt.ylabel("precio")

plt.title("Grafico de Dispercion de Proximidad al Oceano vs Precio")
plt.show()