"""
Calculadora - funciones 
Ingresar parámetros y retornar el resultado de la operación
"""


# === FUNCIONES ===

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar (a,b):
    return a*b

def dividir (a,b):
    if b != 0: 
        return a/b
    else: 
        return "Error!"
    
def potencia (a,b):
    return a ** b

# ==== PROGRAMA PRINCIPAL ====

opcion = 0

while opcion !=6:
    print("\===== INGRESE UNA OPCIÖN ==== ")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Potencia")
    print("6 - Salir")

    opcion = int(input("Seleccione una opcion: "))
    if opcion in [1,2,3,4,5]: 
        x = float(input("Ingrese el primer número: "))
        y = float(input("Ingrese el segundo número: "))

        if opcion == 1:
            print("Resultado", sumar(x,y))
    
        elif opcion == 2: 
            print("Resultado", restar(x,y))
    
        elif opcion == 3:
            print("Resultado", multiplicar(x,y))
    
        elif opcion == 4:
            print("Resultado", dividir(x,y))
    
        elif opcion == 5:
            print("Resultado", potencia (x,y))

    elif opcion == 6:
        print("Nos vemos!")

    else: 
        print("Opción no válida, vuelva a intentarlo")