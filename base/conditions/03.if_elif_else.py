## Expresion que se evalua y devuelve Falso o Verdadero
## IF CONDICION, si la condicion es verdadera, ejecuta las instrucciones que este debajo del if, sino se salta 
## Mayor(>), Mayor o gual (>=), Menor(<), Menor o igual(<=), Igualdad (==), Diferente !=

# ELSE sino se cumple una condicion, ejecute otra instrucion
# ELIF sino (CONDICION) ejecuta la instruccion

#Es mayor a 18, si el valor el igual a 17, ya casi soy mayor de edad, soy un bebe

edad = 15

if edad >= 18:
    print("Es mayor de edad")
    print("Ya puedo ir a rumbiar solo")
elif edad == 17:
    print("Ya casi soy mayor de edad") 
else:
    print("Soy un bebe")

print("Estoy fuera del if")

#Es mayor a 18, si el valor el igual a 17, ya casi soy mayor de edad,  si es igual a 15, soy una quinceanero, soy un bebe

edad = 15

if edad >= 18:
    print("Es mayor de edad")
    print("Ya puedo ir a rumbiar solo")
elif edad == 17:
    print("Ya casi soy mayor de edad")
elif edad == 15:
    print("Ya quinceraro") 
else:
    print("soy un bebe")

print("Estoy fuera del if")