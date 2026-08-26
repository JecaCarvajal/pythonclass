#Operaciones listas
frutas = ["apple", "banana", "naranja", "uva", "pera", "melocoton"]
#Agregar un elemento al final de la lista
frutas.append("kiwi")
print(frutas)   
#Agregar un elemento en una posicion especifica
frutas.insert(1,"sandia")
print(frutas)
#Remover un elemento de la lista
frutas.remove("naranja")
print(frutas)
#Remover un elemento de la lista por su posicion
frutas.pop(2)
print(frutas)
#Remover el ultimo elemento de la lista
frutas.pop()
print(frutas)   
# Remover todos los elementos de la lista
frutas.clear()
print(frutas)

#Recorrer una lista
frutas = ["apple", "banana", "naranja", "uva", "pera", "melocoton"]

for fruta in frutas:
    print(fruta)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    print(numero * 2)
    print(numero ** 2)
    print(numero ** 3)

#Recorrer una lista con un rango de indices
for i in range(len(frutas)):
    print(frutas[i])

#List comprehension
new_list = []
for fruta in frutas:
    if "a" in fruta:
        new_list.append(fruta)

new_list = [x for x in frutas if "a" in x]
print(new_list)

new_list_numeros = [x for x in numeros if x % 2 == 0]
print(new_list_numeros)