'''
1. Realizar una función recursiva que calcule la suma de los primeros números naturales:
'''

def sumar_naturales(numero: int) -> int: # 5 =  1 + 2 + 3 + 4 + 5 = 15 
    if numero == 0:
        resultado = 0
    else:
        resultado = numero + sumar_naturales(numero - 1)
    return resultado

print(sumar_naturales(5))

