## Expresion que se evalua y devuelve Falso o Verdadero
## IF CONDICION, si la condicion es verdadera, ejecuta las instrucciones que este debajo del if, sino se salta 
## Mayor(>), Mayor o gual (>=), Menor(<), Menor o igual(<=), Igualdad (==), Diferente !=

# ELSE sino se cumple una condicion, ejecute otra instrucion
# ELIF sino (CONDICION) ejecuta la instruccion

#Es mayor a 18, si el valor el igual a 17, ya casi soy mayor de edad, soy un bebe
#OPERACIONES LOGICAS and => Es mayor a 17 AND Es menor a 25 
# OR  Es mayor a 17 OR tiene permiso, puede ir a la fiesta 

#Tabla del AND 
#Condicion1 Condiction2 Resultado
#True       True        True
#True       False       False
#False      True        False
#False      False       False

#Tabla del OR
#Condicion1 Condiction2 Resultado
#True       True        True
#True       False       True
#False      True        True
#False      False       False

edad = 23

if edad >= 18 and edad <= 25:
    print("Listo para ir a la universidad")
else:
    print("Estoy en el colegio")

edad = 70

if (edad >= 18 and edad <= 25) or edad >=70:
    print("Listo para ir a la universidad")
else:
    print("Estoy en el colegio")

#Si es mayor de edad 18, puede salir, pero si es menor de 17 AND mayor a 15 y tiene permiso, puede ir a rumbiar, si no, quedate en casa

permiso = True
edad = 14

if edad >= 18 or (edad <= 17 and edad >= 15 and permiso == True):
    print("puede salir a rumbiar")
else:
    print("quedate en casa")

 
