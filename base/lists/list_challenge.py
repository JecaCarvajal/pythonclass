#  if i % 2 == 0
list_pares = []

for i in range(20):
    if i % 2 == 0:
        list_pares.append(i)

print(list_pares)

#List comprehension
list_impares = [i for i in range(20) if i % 2 != 0]
print(list_impares)

#Listas de frutas 
frutas = ["manzana", "banana", "manzana", "pera", "banana", "uva"]
frutas_sin_duplicados = []

for fruta in frutas:
    if fruta not in frutas_sin_duplicados:
        frutas_sin_duplicados.append(fruta)

print(frutas_sin_duplicados)

#Lista de frutas no duplicas version 2
frutas_sin_duplicados = set(frutas)
print(frutas_sin_duplicados)
