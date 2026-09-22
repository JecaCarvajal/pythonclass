# loop sigue iterando hasta que la condicion sea true

i= 1

while i < 6:
    print(i)
    # i = i + 1
    i += 1


nombre = input()
i= 1
while nombre != "salir":    
    print(f"Hola canson {i}")
    i += 1 
    nombre = input()
print(f"Te saliste, hasta luego baby...")