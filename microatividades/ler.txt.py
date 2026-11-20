# Microatividade 4: leitura de dados de um arquivo externo

from pathlib import Path

# Caminho do txt na mesma pasta deste script (funciona de qualquer pasta de execução)
ARQUIVO = Path(__file__).parent / "loremipsum.txt"

# Abrindo com "open" e guardando o arquivo em uma variável
arquivo = open(ARQUIVO, "r", encoding="utf-8")

print("Conteúdo completo do arquivo:")
print(arquivo.read())

# Volta ao início do arquivo para ler de novo
arquivo.seek(0)
print("Apenas a primeira linha:")
print(arquivo.readline(), end="")  # a linha lida já termina com quebra de linha

arquivo.seek(0)
print("Apenas os 3 primeiros caracteres:")
print(arquivo.read(3))

arquivo.close()

# Com "with" o arquivo é fechado automaticamente ao final do bloco
with open(ARQUIVO, "r", encoding="utf-8") as arquivo_with:
    conteudo = arquivo_with.read()

print("\nConteúdo lido com a instrução with:")
print(conteudo)
