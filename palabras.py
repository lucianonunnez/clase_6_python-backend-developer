"""
1. El programa pide al usuario ingresar una palabra o frase
2. Se muestra un menú con funciones para analizar la cadena:
- Contar cuántas letras tiene
- Contar cuántas vocales tiene
- Invertir la cadena
- Ver si alguna palabra o frase es un palíndromo
- Salir

3. Cada acción es una función 
"""

def contar_letras(cadena):
    a = len(cadena.replace(" ", ""))

    return a

def contar_vocales(cadena):

    cadena = cadena.lower()
    vocales = "aeiouáéíóú"
    total = 0

    for v in vocales:
        total += cadena.count(v)

    return total

def invertir_cadena(cadena):

    return cadena[::-1]

"""
[::-1] --> slice (rebanado)

- inicio:fin:paso 
- si no ponemos inicio ni fin, se toma toda la cadena
- el -1 en paso significa ir de atrás hacia adelante

"hola"[::-1] --> empieza en la última letra y va
hacia atrás --> "aloh"

"""

def es_palindromo(cadena):
    limpio = cadena.replace(" ", "").lower()

    return limpio == limpio [::-1]

# === PROGRAMA PRINCIPAL ===

texto = input("Ingrese una palabra o frase")

opcion = 0

while opcion != 5:
    print("\n=== MENÚ ===")
    print("1 - Contar letras")
    print("2 - Contar vocales")
    print("3 - Invertir cadena")
    print("4 - Verificar si es palíndromo")
    print("5 - Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("Cantidad de letras: ",contar_letras(texto))
    elif opcion == 2:
        print("Cantidad de vocales: ",contar_vocales(texto))
    elif opcion == 3:
        print("Invertida: ", invertir_cadena(texto))
    elif opcion == 4:
        if es_palindromo(texto):
            print("Es un palíndromo!")
        else:
            print("No es palíndromo")
    elif opcion == 5:
        print ("Chao")
    
    else:
        print("Opción no válida")