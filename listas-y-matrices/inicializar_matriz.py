def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:

    matriz = []

    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz = matriz + [fila]

    return matriz

print(inicializar_matriz(2,4,0))
