'''
3. Realizar una función recursiva que permita realizar la suma de los dígitos de un número:
'''

def sumar_digitos(numero:int) -> int:  #numero 123 = 1 + 2 + 3 = 6
    if numero == 0:
        resultado = 0
    else:
        resultado = (numero % 10) + sumar_digitos(numero // 10)
    return resultado


print(sumar_digitos(123))