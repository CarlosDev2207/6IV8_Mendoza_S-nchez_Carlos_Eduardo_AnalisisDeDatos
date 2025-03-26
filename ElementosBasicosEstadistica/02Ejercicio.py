import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates  #manejamos fechas en graficos

ruta_ventas = "proyecto1.xlsx"
ruta_sucursales = "Catalogo_sucursal.xlsx"


df_ventas = pd.read_excel(ruta_ventas, sheet_name="in")
df_sucursales = pd.read_excel(ruta_sucursales, sheet_name="in")

if "B_mes" in df_ventas.columns:
    df_ventas["B_mes"] = pd.to_datetime(df_ventas["B_mes"], errors='coerce') #aqui como que vemo la columna de B_mes esta en la de df_ventas se hace data time  para las fechas

df_ventas = df_ventas.merge(df_sucursales, on="id_sucursal", how="left") #normalizamos

total_ventas = df_ventas["ventas_tot"].sum() #total de ventas


#clientes con y sin adeudo

clientes_deudores = df_ventas[df_ventas["B_adeudo"] == "Con adeudo"]["no_clientes"].sum()
clientes_sin_deuda = df_ventas[df_ventas["B_adeudo"] == "Sin adeudo"]["no_clientes"].sum()

total_clientes = clientes_deudores + clientes_sin_deuda
porcentaje_con_adeudo = (clientes_deudores / total_clientes) * 100
porcentaje_sin_adeudo = (clientes_sin_deuda / total_clientes) * 100

#la deuda total y el margen de utilidad

total_deuda = df_ventas["adeudo_actual"].sum()

porcentaje_utilidad = ((total_ventas - total_deuda) / total_ventas) * 100



#proyeccion de las graficas

fig, ax = plt.subplots(figsize=(10,5))
ventas_por_mes = df_ventas.groupby("B_mes")["ventas_tot"].sum()
ventas_por_mes.plot(kind="bar", ax=ax, title="Ventas Totales por Mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas Totales")
ax.set_xticklabels(ventas_por_mes.index.strftime('%Y-%m'), rotation=45)
plt.show()

fig, ax = plt.subplots(figsize=(10,5))
desviacion_pagos = df_ventas.groupby("B_mes")["pagos_tot"].std()
desviacion_pagos.plot(kind="bar", ax=ax, title="Desviación Estándar de Pagos por Mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Desviación Estándar")
ax.set_xticklabels(desviacion_pagos.index.strftime('%Y-%m'), rotation=45)
plt.show()

ventas_por_sucursal = df_ventas.groupby("suc")["ventas_tot"].sum()
ventas_por_sucursal.plot(kind="pie", autopct='%1.1f%%', figsize=(8,8), title="Distribución de Ventas por Sucursal")
plt.ylabel("")
plt.show()

utilidad_por_sucursal = df_ventas.groupby("suc").agg({"adeudo_actual": "sum", "ventas_tot": "sum"})
utilidad_por_sucursal["margen_utilidad"] = ((utilidad_por_sucursal["ventas_tot"] - utilidad_por_sucursal["adeudo_actual"]) / utilidad_por_sucursal["ventas_tot"]) * 100

fig, ax1 = plt.subplots(figsize=(10,5))
ax2 = ax1.twinx()
ax1.bar(utilidad_por_sucursal.index, utilidad_por_sucursal["adeudo_actual"], color='r', alpha=0.6, label="Deuda Total")
ax2.plot(utilidad_por_sucursal.index, utilidad_por_sucursal["margen_utilidad"], color='b', marker='o', label="Margen de Utilidad (%)")
ax1.set_xlabel("Sucursal")
ax1.set_ylabel("Deuda Total", color='r')
ax2.set_ylabel("Margen de Utilidad (%)", color='b')
plt.title("Deuda Total por Sucursal vs Margen de Utilidad")
plt.legend()
plt.show()
