numero = int(input("Ingresa un número: "))
print(f"\nProceso de reducción para {numero}:")

#Mientras que la suma del numero sea menor o igual a 10. 

while numero >= 10:
    suma_digitos = sum(int(i) for i in str(numero)) #suma de digitos. Recorre todos los numeros ingresados en el input y los convierte en string.
    #luego convierte el elemento recorrido en un entero y los suma.
    print(f"\n{numero} = {suma_digitos}") #Impreme la version ya sumada de todos los valores.
    numero = suma_digitos 

print(f"\nEl resultado final es: {numero}")
