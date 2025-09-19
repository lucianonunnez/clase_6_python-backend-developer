"""
Crear un programa que: 
1) Pedimos al usuario que ingrese una frase
2) Determinar para esa frase
- Cuántas palabras tiene la frase
- Cuente cuántas letras tiene
- Devolver la palabra más larga
3) Mostrar los resultados en pantalla
"""

def contar_palabras(frase):
    a = len(frase.split())
    return a

def contar_letras(frase):
    a = len(frase.replace(" ", ""))
    return a

def palabra_mas_larga(frase):
    palabras = frase.split()

    return max(palabras,key=len)

# ===== PROGRAMA 

texto = input("Ingrese la frase: ")

print("\nCantidad de palabras", contar_palabras(texto))
print("Cantidad de letras", contar_letras(texto))
print("Palabra más larga", palabra_mas_larga(texto))

