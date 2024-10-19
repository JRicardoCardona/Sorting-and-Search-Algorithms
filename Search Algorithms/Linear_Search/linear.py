lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12,13,14,17,18,19,20,21,22,23,24,25,26,27,28,29,30]


def linear_search(lista, number):
    return f"La posición del número en la lista es: {next((index for index, value in enumerate(lista) if value == number), 'No encontrado')}"

# Example usage
lista = [4, 2, 9, 5, 7]
number = 9
print(linear_search(lista, number))
