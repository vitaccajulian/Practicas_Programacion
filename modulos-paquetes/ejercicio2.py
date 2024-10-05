'''
2. Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud
de la cadena ingresada dado el parámetro recibido. El siguiente prototipo es la base para realizar el
ejercicio (se puede extender):

def get_string(longitud:int) -> str | None:


Nota: utilizar la función len.
'''

def get_string(mensaje:str, mensaje_error: str, longitud:int, reintentos:int) -> str | None:
    if reintentos == 0:
        return None
    else:
        print(mensaje)
        cadena = input("Ingrese un mensaje: ")

        if len(cadena) > longitud:
            print(mensaje_error)
            return get_string('', mensaje_error, longitud , reintentos - 1)
        elif len(cadena) == 0:
            return print(mensaje_error)
            get_string('', mensaje_error, longitud , reintentos - 1)
        else:
            return cadena



mensaje = "Bienvenido"
longitud = 25
mensaje_error = f"La longitud ingresada es invalida. Tiene que ser de un maximo de {longitud} caracteres."
reintentos = 3

print(get_string(mensaje , mensaje_error, longitud , reintentos))