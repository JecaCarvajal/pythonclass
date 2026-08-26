frutas = ["apple", "banana", "naranja", "uva", "pera", "melocoton"]
print(frutas)
# copia de valores de una lista a otra lista
frutas2 = frutas.copy()
frutas2[0]="manzana" 
print(frutas2)
print(frutas)
#tamaño de la lista
print(len(frutas))
#acceder a un elemento de la lista
print(frutas[3])
#acceder a un elemento de la lista desde el final
print(frutas[-1])
#sacar un rango de elementos de la lista
print(frutas[1:4])
#sacar desde posicion 2 hasta el final
print(frutas[2:])
#sacar desde el final hasta la posicion 3
print(frutas[:-3])
print(frutas[:4]) 
frutas[1:2]=["kiwi", "sandia"]
print(frutas)