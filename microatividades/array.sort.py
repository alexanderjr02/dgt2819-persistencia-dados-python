# Microatividade 1: ordenação de um array com o método nativo "sort"

# Array de 15 números inteiros, sem ordenação
numeros = [42, 7, 93, 15, 68, 3, 81, 27, 54, 11, 99, 36, 60, 22, 5]

print("Array de números original:")
print(numeros)

# Ordem crescente
numeros.sort()
print("\nOrdem crescente (sort):")
print(numeros)

# Ordem decrescente
numeros.sort(key=None, reverse=True)
print("\nOrdem decrescente (sort com key=None, reverse=True):")
print(numeros)

# Mesmos passos com um array de strings
campos = ["nome", "dataNascimento", "cpf", "rg"]

print("\nArray de strings original:")
print(campos)

campos.sort()
print("\nOrdem crescente (sort):")
print(campos)

campos.sort(key=None, reverse=True)
print("\nOrdem decrescente (sort com key=None, reverse=True):")
print(campos)
