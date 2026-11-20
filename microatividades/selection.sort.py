# Microatividade 3: algoritmo de ordenação Selection Sort

array = [42, 7, 93, 15, 68, 3, 81, 27, 54, 11, 99, 36, 60, 22, 5]

print("Array original:")
print(array)

for i in range(len(array)):
    # Posição do menor valor encontrado a partir de i
    menor = i

    for j in range(i + 1, len(array)):
        if array[menor] > array[j]:
            menor = j

    # Coloca o menor valor encontrado na posição i
    array[i], array[menor] = array[menor], array[i]

print("\nArray ordenado com Selection Sort:")
print(array)
