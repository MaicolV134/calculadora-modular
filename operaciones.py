# operaciones.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b
def potencia(a, b):
    return a ** b
def division_entera(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a // b
