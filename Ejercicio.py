# Ejercicio del libro "lenguaje interpretado Python" UNI
from tabulate import tabulate

fideo_list=[]
arroz_list=[]
azucar_list=[]
total_almacenes=[]
vector_entero=[]


n=int(input("Total de productos para cada tipo = "))

for i in range(n):
    fideo=float(input(f"Precio del fideo en el distrito [{i+1}] = S/ "))
    arroz=float(input(f"Precio del arroz en el distrito [{i+1}] = S/ "))
    azucar=float(input(f"Precio del azucar en el distrito [{i+1}] = S/"))

    fideo_list.append(fideo)
    arroz_list.append(arroz)
    azucar_list.append(azucar)
    print(" ")

tabla=[fideo_list,arroz_list,azucar_list]

print(tabulate(tabla,headers=[]))
print("\n")
print(f'Totales de cada producto: '"\n"
      f'Total de Fideo: {sum(fideo_list)} --> {round(sum(fideo_list))}' "\n"
      f'Total de Arroz: {sum(arroz_list)} --> {round(sum(arroz_list))}' "\n"
      f'Total de Azucar: {sum(azucar_list)}--> {round(sum(azucar_list))}' "\n")


print("Total del almacenes")

for i,fila in enumerate(tabla,start=1):
    print(f'Total de almacen [{i}]: {sum(fila)}')
    total_almacenes.append(sum(fila))

print(" ")
print("Valores redondeados: ")
for i,fila in enumerate(tabla,start=1):
    print(f'Total de almacen [{i}]: {round(sum(fila))}')

print("")
print("Totales sin repetirse: ")
print(set(total_almacenes))


