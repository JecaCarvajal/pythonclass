prompt = """
fdfdfdf
fdfdf
fdfdfdf
fdfdf."""
print(prompt)

segundo_ejemplo = "Hola Samuel"

print(segundo_ejemplo[0])

for letra in segundo_ejemplo:
    print(letra)

print(len(segundo_ejemplo))

print("Samuel" in segundo_ejemplo)

if "Samuel" in segundo_ejemplo:
    print("Samuel se va a graduar")

if "Jaime" not in segundo_ejemplo:
    print("No esta la palabra Jaime")

segundo_ejemplo = segundo_ejemplo + " Vamos de paseo     "
print(segundo_ejemplo)

tercer_ejemplo = segundo_ejemplo[:4]
print(tercer_ejemplo)
print(segundo_ejemplo[4:])
print(tercer_ejemplo.upper())
print(tercer_ejemplo.lower())
print(segundo_ejemplo.strip())


primero = " Jaime "
segundo = "JAime"

if primero.strip().lower() == segundo.strip().lower():
    print("Son iguales")
else:
    print("No son iguales")

tercero = "Hola,Samuel,Jaime"
print(tercero.split(","))

nombre = "Samuel"
saludo = f"Hola {nombre}, que gusto conocerte"
print(saludo)

print("jaime".capitalize())
print("Termina con".endswith("con"))
print("Termina con".startswith("Termina"))
print("1212144sdd-*/".isalnum())
print("1212144sdd-*/".isalnum())
print("1212144".isdigit())
print("Hola Samuel".replace("Samuel", "Jaime"))
print("Hola Samuel".find("Samuel"))
print("Hola Samuel".isupper())

## mi_numero, Dado un texto en Camel case ejemplo MiNumero, quiero convertirlo en snake case ejemplo: mi_numero

camel_case = "MiNumeroDos"
snake_case = ""

camel_case_a = camel_case[0].lower() + camel_case[1:]
print(camel_case_a)
for letra in camel_case_a:
    if letra.isupper():
        snake_case += '_' + letra.lower()
    else:
        snake_case += letra  
print(snake_case)














