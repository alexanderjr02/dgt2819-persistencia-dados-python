# Microatividade 5: escrita de dados em um arquivo externo

from pathlib import Path

# O arquivo é criado na mesma pasta deste script
ARQUIVO = Path(__file__).parent / "texto.txt"

# Modo "w": cria o arquivo se ele ainda não existir
arquivo = open(ARQUIVO, "w", encoding="utf-8")

texto = list()
texto.append("Python permite ler e gravar arquivos de forma simples.\n")
texto.append("O método open abre o arquivo e o modo w cria um arquivo novo.\n")
texto.append("Cada frase desta lista vira uma linha no arquivo texto.txt.\n")
texto.append("Depois de escrever, o arquivo deve ser fechado com close.\n")

arquivo.writelines(texto)
arquivo.close()

print(f"Arquivo criado: {ARQUIVO.name}")
print("Conteúdo gravado:")
print("".join(texto))
