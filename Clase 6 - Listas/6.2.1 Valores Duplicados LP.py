valores = input("Ingrese valores para su lista: ").split(" ")
print (valores)

liste = []

for numero in valores:
    if numero not in liste:
       liste.append(numero)
    else: 
        continue
print(liste, end=".")

