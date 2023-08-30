#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Julian
#
# Created:     16/08/2023
# Copyright:   (c) Julian 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    def suma(a, b):
        return a + b

    def resta(a, b):
        return a - b

    def multiplicacion(a, b):
        return a * b

    def division(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: No es posible dividir por cero"

    print("Calculadora")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Seleccione la operación (1/2/3/4): ")

    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print("Resultado:", suma(numero1, numero2))
    elif opcion == '2':
        print("Resultado:", resta(numero1, numero2))
    elif opcion == '3':
        print("Resultado:", multiplicacion(numero1, numero2))
    elif opcion == '4':
        print("Resultado:", division(numero1, numero2))
    else:
        print("Opción inválida")
    input('ingrese enter para finaliza')
    main()