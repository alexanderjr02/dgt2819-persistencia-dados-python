# Microatividade 2: algoritmo de ordenação Bubble Sort


def bubbleSort(array):
    # A cada passada, o maior valor ainda fora de ordem "sobe" para o fim do array
    for i in range(len(array)):
        # Compara os elementos de dois em dois; os últimos i já estão no lugar certo
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temporario = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temporario


numeros = [42, 7, 93, 15, 68, 3, 81, 27, 54, 11, 99, 36, 60, 22, 5]

print("Array original:")
print(numeros)

bubbleSort(numeros)

print("\nArray ordenado com Bubble Sort:")
print(numeros)
