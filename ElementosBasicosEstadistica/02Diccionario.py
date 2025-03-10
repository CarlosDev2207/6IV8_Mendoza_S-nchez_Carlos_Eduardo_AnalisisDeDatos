import pandas as pd

##Escribri una funcion que reciba un diccionario con las notas de los estudiasntes del curso y devuelve una serie con minimo, maximo, media, desviacion tipica
def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticas = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index= ['Minimo', 'max', 'Media', 'Desviacion Estandar'])
    return estadisticas

notas = {'Juan': 9, 'Juanita': 7, 'Pedro': 6.6, 'Fabian': 8.5, 'Maximiliano': 7.5, 'Sandra': 9.8, 'Rosario': 9}

print(estadistica_notas(notas))
    