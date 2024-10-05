'''
2. Realizar una función recursiva que calcule la potencia de un número:
'''

def calcular_potencia(base:int, exponente:int) -> int: #5 ^ 3 = 5 * 5 * 5 
    if exponente == 0:
        resultado = 1
    else:
        resultado = base * calcular_potencia(base, exponente - 1)
    return resultado


numero = 5
exponente_numero = 3
print(calcular_potencia(numero, exponente_numero))