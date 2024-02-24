def separar_longitudes(longitudes):
    longitudes_separadas = longitudes.split(' ')
    longitudes_separadas = [x for x in longitudes_separadas if x]  #La comprensión de lista [x for x in longitudes_separadas if x] elimina cualquier elemento vacío de la lista longitudes_separadas antes de convertirla a enteros. Esto debería evitar el error que estás experimentando.
    longitudes_separadas = list(map(int, longitudes_separadas))
    longitudes_separadas.sort()
    return longitudes_separadas


def sumar_longitudes(longitudes_separadas):
    suma = 0
    for longitud in longitudes_separadas:
        suma += longitud
    return suma


def descomponer_en_primos(suma):
    lista_primos = []
    for i in range(1, suma):
        if (suma % i == 0):
            lista_primos.append(i)
    return lista_primos


def encontrar_longitud_mayor(longitudes_separadas):
    mayor = 0
    for longitud in longitudes_separadas:
        if (longitud > mayor):
            mayor = longitud
    return mayor


def sumar_extremos(longitudes_separadas):
    suma_extremos = []
    n = len(longitudes_separadas)
    for i in range((n + 1) // 2):
        suma = longitudes_separadas[i] + longitudes_separadas[n - 1 - i]
        suma_extremos.append(suma)
    return suma_extremos


def comparar_sumas_extremos(suma_extremos):
    son_iguales = True
    for i in range(len(suma_extremos) - 1):
        if (suma_extremos[i] != suma_extremos[i + 1]):
            son_iguales = False
            break
    return son_iguales





def main():
    print('Ingrese el número de partes de palitos y las longitudes de las partes separadas por un espacio, recuerde que es en dos lineas diferentes:\n')
    while True:
        # Leer el número de partes de palitos
        palitos_cortados = int(input())
        if (palitos_cortados == 0):
            break  # Salir del bucle si el número de partes es 0

        # Leer las longitudes de las partes de palitos
        longitudes = input()

        # Procesar y mostrar las longitudes separadas
        longitudes_separadas = separar_longitudes(longitudes)
        print(longitudes_separadas)

        suma = sumar_longitudes(longitudes_separadas)
        print(suma)

        lista_primos = descomponer_en_primos(suma)
        print(lista_primos)

        mayor = encontrar_longitud_mayor(longitudes_separadas)
        print(mayor)

        suma_extremos = sumar_extremos(longitudes_separadas)
        print(suma_extremos)

        son_iguales = comparar_sumas_extremos(suma_extremos)
        print(son_iguales)


if __name__ == "__main__":
    main()

