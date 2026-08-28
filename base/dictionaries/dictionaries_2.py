#Operaciones 
#key y valores
super_heores = {
    "Spiderman" : "Piter",
    "Batman": "Bruce",
    "Superman": "Clark",
}

super_heores["Spiderman"] = "Harry"
print(super_heores)

super_heores["Hulk"] = "Bruce Waner"
print(super_heores)

super_heores.update({"Black panter": "T'Challa"})
super_heores.update({"Batman": "Bruce Wayne"})
print(super_heores)

super_heores.pop("Hulk")
print(super_heores)

#Recorrer los diccionarios
for hereo in super_heores:
    print(hereo)

for hereo in super_heores:
    print(super_heores[hereo])

for value in super_heores.values():
    print(value)

for key in super_heores.keys():
    print(key)

super_hereos2 = super_heores.copy()

super_hereos2["Superman"] = "Samuel"


print(super_heores)
print(super_hereos2)

dc = {
    "Batman" : "Murcielago",
    "Superman" : "El lider"
}

marvel = {
    "Spiderman" : "Hombre araña",
    "Iron Man": "Hombre de lata"
}

heroes = {
    "dc": dc,
    "marvel" : marvel 
}

print(heroes)
print(heroes["marvel"]["Spiderman"])
print(heroes["dc"]["Superman"])