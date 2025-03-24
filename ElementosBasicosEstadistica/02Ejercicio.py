import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_excel('proyecto1.xlsx')


#suma total
ventas = datos["ventas_tot"].sum()
print(ventas)
#clientes con adeudo y sin adeudo
con_adeudo = datos["B_adeudo"] == "Con adeudo"
sin_adeudo = datos["B_adeudo"] == "Sin adeudo"

clientes = datos["no_clientes"]

print(con_adeudo)

