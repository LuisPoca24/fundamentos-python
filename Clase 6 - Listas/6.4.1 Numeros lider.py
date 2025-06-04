#6.4.1 Numeros lider

numeros = list(map(int, input("Ingresa una serie de números con espacios: ").split()))
Numero_lider = []
max_derecha = -1

for i in numeros[::-1]:
    if i > max_derecha:
        Numero_lider.append(i)
        max_derecha = i

print(*Numero_lider[::-1])




