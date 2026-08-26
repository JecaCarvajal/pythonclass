#key y valores
super_heores = {
    "Spiderman" : "Piter",
    "Batman": "Bruce",
    "Superman": "Clark"
}

print(super_heores)
print(super_heores["Spiderman"])
print(super_heores.get("Spiderman"))
print(super_heores.keys())
print(super_heores.values())
print(super_heores.items())

if "Spiderman" in super_heores:
    print("Es un heroe de Marvel")
else:
    print("No encontre el heore, estas mal, aprende")




