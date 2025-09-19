# 1) Pedir los 3 números

numeros = []

for i in range(3):
    n = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(n)

# 2) Ordenarlos de mayor a menor

numeros.sort(reverse=True)

# 3) Mostrar el resultado 

print("\nLos números ordenados de mayor a menor son: ")

for num in numeros:
    print(num)

# ====================================================

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

mayor = max(a,b,c)
menor = min(a,b,c)
medio = (a+b+c) - (mayor + menor) 

print("\nNúmeros ordenados de mayor a menor: ")
print(mayor,medio,menor)

# ==================================================

numeros = []
suma = 0

for i in range(3):
    numeros[i] = float(input(f"Ingrese el número{i+1}: "))
    suma = numeros[i]

max = 0

for i in range(3):
    if numeros[i] > max:
        máx = numeros[i]

min = max 

for i in range(3):
    if numeros[i] < min:
        min = numeros [i]

medio = suma - (max + min) 