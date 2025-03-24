#ventas sumas todo
#cuantos socios tienen adeudo y cuantos no con porcentaje = contamos

#(restar ventas - adeudos)
"""
1 Conocer las ventas totales del comercio
2 Conocer cuantos socios tienen adeudo y cuantos no tienen adeudo con su porcentaje correspondiente
3 Grafica donde se pueda observar las ventas totales respecto del tiempo, en una grafica de barras 
4 Grafica donde se pueda visualizar la desviación estándar de los pagos realizados del comercio respecto del tiempo
5 Cuanto es la deuda total de los clientes
6 Cuanto es el porcentaje de utilidad del comercio a partir de el total de las ventas respecto del adeudo 
7 Crear un grafico circular de ventas por sucursal.
8 Presentar un grafico de cuales son las deudas totales por cada sucursal respecto del margen de utilidad de cada sucursal.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_xlsx('ElementosBasicosEstadist/Catalogo_sucursal.xlsx')
df2 = pd.read_xslx('ElementosBasicosEstadist/proyecto1.xlsx')
#leer los exel
df1["id_sucursal"] = df1["id_sucursal"].astype

"""

#Intento numero 1, no funciono copiando de las librerias unu

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los archivos Excel
df_proyecto = pd.read_excel('proyecto1.xlsx')
df_sucursal = pd.read_excel('Catalogo_sucursal.xlsx')

# Si es necesario, se puede unir información de sucursales
# Por ejemplo, si en df_sucursal se tiene columna 'NombreSucursal' y se desea unir:
# df_proyecto = df_proyecto.merge(df_sucursal[['Sucursal', 'NombreSucursal']], on='Sucursal', how='left')

#

# 1. Conocer las ventas totales del comercio
ventas_totales = df_proyecto['Venta'].sum()
print("Ventas totales del comercio:", ventas_totales)

# 2. Conocer cuantos socios tienen adeudo y cuantos no, junto a sus porcentajes
# Se asume que cada fila corresponde a un socio o transacción; se pueden agrupar si se cuenta con un ID de socio.
socios_con_adeudo = df_proyecto[df_proyecto['Adeudo'] > 0].shape[0]
socios_sin_adeudo = df_proyecto[df_proyecto['Adeudo'] == 0].shape[0]
total_socios = df_proyecto.shape[0]

porcentaje_con = (socios_con_adeudo / total_socios) * 100
porcentaje_sin = (socios_sin_adeudo / total_socios) * 100

print("Socios con adeudo:", socios_con_adeudo, "({:.2f}%)".format(porcentaje_con))
print("Socios sin adeudo:", socios_sin_adeudo, "({:.2f}%)".format(porcentaje_sin))

