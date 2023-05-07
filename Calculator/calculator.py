import sys
import gmpy2


def show_menu():
    print("----------------------")
    print("Calculadora Modular")
    print("----------------------\n")
    print("1. Suma")
    print("2. Multiplicación")
    print("3. División")
    print("4. Potencia Modular")
    print("5. Inverso Multiplicativo Modular")
    print("6. Raíz Cuadrada Modular")
    print("7. Cuadrados Perfectos")
    print("0. Salir")


def get_modulus():
    while True:
        try:
            modulus = int(input("Ingrese el valor de Zn (n): "))
            if modulus <= 0:
                print("El valor de Zn debe ser mayor que cero.")
            else:
                return modulus
        except ValueError:
            print("El valor ingresado no es un número entero válido.")


def get_number():
    while True:
        try:
            number = gmpy2.mpz(input("Ingrese el número: "))
            return number
        except ValueError:
            print("El valor ingresado no es un número válido.")


def perform_addition(modulus):
    a = get_number() % modulus
    b = get_number() % modulus
    result = (a + b) % modulus
    print(f"El resultado de la suma es: {result}\n\n")


def perform_multiplication(modulus):
    a = get_number() % modulus
    b = get_number() % modulus
    result = (a * b) % modulus
    print(f"El resultado de la multiplicación es: {result}")


def perform_division(modulus):
    a = get_number() % modulus
    b = get_number() % modulus
    try:
        result = gmpy2.divm(a, b, modulus)
        print(f"El resultado de la división es: {result}")
    except ZeroDivisionError:
        print("No se puede dividir por cero.")


def perform_modular_exponentiation(modulus):
    base = get_number() % modulus
    exponent = get_number()
    result = gmpy2.powmod(base, exponent, modulus)
    print(f"El resultado de la potencia modular es: {result}")


def perform_modular_inverse(modulus):
    number = get_number() % modulus
    try:
        inverse = gmpy2.invert(number, modulus)
        print(f"El inverso multiplicativo modular es: {inverse}")
    except ZeroDivisionError:
        print("No existe el inverso multiplicativo modular para el número ingresado.")


def perform_modular_square_root(modulus):
    number = get_number() % modulus
    try:
        roots = gmpy2.iroot(number, 2)
        if roots[1]:
            print(f"Las raíces cuadradas modulares son: {roots[0]} y {-roots[0] % modulus}")
        else:
            print("El número no tiene raíces cuadradas modulares.")
    except ValueError:
        print("El número no tiene raíces cuadradas modulares.")


def perform_modular_square_list(modulus):
    squares = []
    for i in range(1, modulus):
        square = (i * i) % modulus
        squares.append(square)
    print(f"Los cuadrados perfectos modulares son: {squares}")


def main():
    while True:
        show_menu()
        option = int(input("Seleccione una opción: "))
        if option == 1:
            perform_addition(get_modulus())
        if option == 2:
            perform_multiplication(get_modulus())
        if option == 3:
            perform_division(get_modulus())
        if option == 4:
            perform_modular_exponentiation(get_modulus())
        if option == 5:
            perform_modular_inverse(get_modulus())
        if option == 6:
            perform_modular_square_root(get_modulus())
        if option == 7:
            perform_modular_square_list(get_modulus())
        if option == 0:
            sys.exit()

main()