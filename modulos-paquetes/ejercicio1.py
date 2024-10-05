'''
Realizar una función para pedir un número por consola.
● mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
● mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
● mínimo: valor mínimo admitido (inclusive)
● máximo: valor máximo admitido (inclusive)
● reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.
En caso de que la función no haya podido conseguir un número válido, la misma retorna None.
'''

def get_int(mensaje:str , mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
    if reintentos == 0:
        return None
    else:
        print(mensaje)
        numero_str = input("Ingrese un numero entero: ")

        if numero_str.isdigit() == 0:
            print(mensaje_error)
            return get_int('', mensaje_error , minimo , maximo , reintentos - 1)
            
        numero = int(numero_str)

        if numero < minimo or numero > maximo:
            print(mensaje_error)
            return get_int('', mensaje_error , minimo , maximo , reintentos - 1)
        else:
            return numero



mensaje = "Bienvenido"
minimo = 4
maximo = 9
mensaje_error = f"El numero ingresado es invalido. Tiene que ser entre {minimo} y {maximo}."
reintentos = 3

print(get_int(mensaje , mensaje_error , minimo , maximo , reintentos))