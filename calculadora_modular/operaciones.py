# operaciones.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def potencia(a, b):
    return a ** b

def division_entera(a, b):
    if b == 0:
        return "Error: división por cero"
    return a // b