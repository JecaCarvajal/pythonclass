supervillanos = ["lex luthor", "Wiane", "Guason", "Thanos"]

for villano in supervillanos:
    print(villano)
    print(f"{villano} son muy malos")

numeros = [1,2,3,4,5,6]
for numero in numeros:
     print(numero * 2) 

for number in range(3):
     print("Thank you")

##Tengo un lista de numeros y quiero encontrar los duplicados de esa lista
## Lista, For, Diccionario 
## El resultado es 2:3 3:2 5:2 

## 1:1
## 2:1
## 3:1
## 2:2

lst = [1,2,3,2,4,5,3,2,6,5]
feq = {}

for num in lst:
     if num in feq:
          feq[num] = feq[num] + 1
     else:
          feq[num] = 1
print(feq)
  
for key in feq:
     if feq[key] > 1:
          print(key, ":" , feq[key])







