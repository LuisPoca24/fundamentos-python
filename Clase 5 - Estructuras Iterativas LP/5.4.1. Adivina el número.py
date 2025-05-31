# 5.4.1. ¡Adivina el número!
import random
numero_secreto = random.randint(1, 100) #chatgpt utilizado para confirmar como se importaba la función random. 

#print(numero_secreto)

while True:
    numero = int(input("Ingresa un número del 1 al 100: "))
    if numero > numero_secreto: #si el intento es menor que el numero secreto.
        print("El numero secreto es menor")
    elif numero == numero_secreto: #si el intento es igual al numero secreto.
        print(f"¡Felicidades! Has adivinado el número secreto")
        print ("Fin del juego")
        break 
    else: #si el intento es mayor que el numero secreto.
        print("El numero secreto es mayor")

