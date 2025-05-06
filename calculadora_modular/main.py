# main.py

from operaciones import (
    sumar,
    restar,
    multiplicar,
    dividir,
    potencia,
    division_entera
)

def mostrar_menu():
    print("\nCalculadora Modular")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. División entera")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "7":
            print("¡Hasta luego!")
            break

        try:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
            continue

        if opcion == "1":
            print("Resultado:", sumar(a, b))
        elif opcion == "2":
            print("Resultado:", restar(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicar(a, b))
        elif opcion == "4":
            print("Resultado:", dividir(a, b))
        elif opcion == "5":
            print("Resultado:", potencia(a, b))
        elif opcion == "6":
            print("Resultado:", division_entera(a, b))
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()