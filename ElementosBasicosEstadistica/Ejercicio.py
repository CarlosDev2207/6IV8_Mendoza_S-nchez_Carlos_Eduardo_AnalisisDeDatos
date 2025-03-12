import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display

# Cargar el dataset
data = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

# ---------------------------
# Estadísticas para median_house_value
# ---------------------------
median_house_value = data['median_house_value']

media = median_house_value.mean()
mediana = median_house_value.median()
moda = median_house_value.mode()[0]  # Se toma la primera moda en caso de múltiples
rango = median_house_value.max() - median_house_value.min()
varianza = median_house_value.var()
desviacion = median_house_value.std()

# Crear tabla resumen con las estadísticas solicitadas
tabla_resumen = pd.DataFrame({
    'Estadística': ['Media', 'Mediana', 'Moda', 'Rango', 'Varianza', 'Desviación Estándar'],
    'Valor': [media, mediana, moda, rango, varianza, desviacion]
})

print("Tabla Resumen de median_house_value:")
# Se utiliza .style para cambiar colores: fondo azul claro y texto azul oscuro
display(tabla_resumen.style.set_properties(**{'background-color': '#e6f2ff', 'color': '#003366', 'border-color': 'black'}))
print("\n")

# ---------------------------
# Tabla de Frecuencias para median_house_value
# ---------------------------
# Se crean 10 intervalos (bins) para agrupar los datos
data['m_hv_bin'] = pd.cut(median_house_value, bins=10)
tabla_frecuencias = data['m_hv_bin'].value_counts().sort_index().reset_index()
tabla_frecuencias.columns = ['Intervalo', 'Frecuencia']

print("Tabla de Frecuencias (bins) para median_house_value:")
# Se utiliza .style para cambiar colores: fondo rosado claro y texto rojo oscuro
display(tabla_frecuencias.style.set_properties(**{'background-color': '#ffe6e6', 'color': '#660000', 'border-color': 'black'}))
print("\n")

# ---------------------------
# Graficar el Histograma de median_house_value
# ---------------------------
plt.figure(figsize=(8,6))
# Se cambia el color a púrpura para el histograma
plt.hist(median_house_value, bins=30, color='purple', alpha=0.7)
# Línea de la media en color magenta oscuro
plt.axvline(media, color='darkmagenta', linestyle='dashed', linewidth=2, label=f'Media: {media:.2f}')
plt.title('Histograma de median_house_value')
plt.xlabel('median_house_value')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

# ---------------------------
# Graficar Histograma para total_bedrooms
# ---------------------------
plt.figure(figsize=(8,6))
# Se cambia el color a teal para este histograma
plt.hist(data['total_bedrooms'].dropna(), bins=30, color='teal', alpha=0.7)
plt.title('Histograma de total_bedrooms')
plt.xlabel('total_bedrooms')
plt.ylabel('Frecuencia')
plt.show()

# ---------------------------
# Graficar Histograma para population
# ---------------------------
plt.figure(figsize=(8,6))
# Se cambia el color a marrón para este histograma
plt.hist(data['population'], bins=30, color='brown', alpha=0.7)
plt.title('Histograma de population')
plt.xlabel('population')
plt.ylabel('Frecuencia')
plt.show()

import pandas as pd

# Cargar el dataset
data = pd.read_csv('ElementosBasicosEstadistica/housing.csv')
median_house_value = data['median_house_value']

# Calcular el mínimo, máximo y definir el número de bins
min_value = median_house_value.min()
max_value = median_house_value.max()
bins = 10
bin_width = (max_value - min_value) / bins

# Generar los rangos (bins)
rangos = [(min_value + i * bin_width, min_value + (i+1) * bin_width) for i in range(bins)]

print("Rangos propuestos para median_house_value:")
for idx, (inicio, fin) in enumerate(rangos, 1):
    print(f"Rango {idx}: [{inicio:.2f}, {fin:.2f})")
