import pandas as pd #hace operaciones de estadistica el pandas

##Escribir un programa que pregunte al usuario pro las ventas de un rango de años y muestre en la pantalla una serie de datos de ventas indexadas por los años, antes y despues de aplicarles un descuento

inicio = int(input("introduce el año de ventas inicial: "))
fin = int(input("introduce el año final de ventas"))

ventas = {}

for i in range(inicio, fin + 1):
    ventas[i] = float(input("introduce las ventas del año: " + str(i) + ": "))
    
    ventas = pd.Series(ventas)
    print('ventas \n', ventas)
    print('ventas con descuento \n', ventas*0.9)