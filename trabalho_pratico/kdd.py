"""
Trabalho prático: glossário de palavras ordenadas (MVP do dicionário de termos jurídicos).

Lê o documento txt linha a linha, separa as palavras, ordena com o método nativo sort
(o mais rápido na comparação feita com Bubble Sort e Selection Sort) e grava o glossário
em um novo arquivo txt.

Uso:
    python kdd.py
"""

import string
import textwrap
import time
import unicodedata
from pathlib import Path

PASTA = Path(__file__).parent
DOCUMENTO = PASTA / "documento.txt"
GLOSSARIO = PASTA / "palavras_ordenadas.txt"

# Pontuação removida das pontas de cada palavra (inclui aspas tipográficas)
PONTUACAO = string.punctuation + "“”‘’–—"


def limpar(palavra):
    """Deixa a palavra em minúsculas e sem pontuação nas pontas."""
    return palavra.strip(PONTUACAO).lower()


def chave_alfabetica(palavra):
    """Chave sem acentos, para 'ação' ficar perto de 'acesso' e não depois de 'z'."""
    sem_acento = unicodedata.normalize("NFD", palavra)
    return "".join(c for c in sem_acento if unicodedata.category(c) != "Mn")


def ler_palavras(caminho):
    """Lê o arquivo linha a linha e devolve a lista com todas as palavras."""
    palavras = list()
    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            for palavra in linha.split():
                palavra = limpar(palavra)
                if palavra:
                    palavras.append(palavra)
    return palavras


def gravar_glossario(caminho, palavras_ordenadas):
    """Grava uma palavra por linha, sem repetições, mantendo a ordem alfabética."""
    unicas = list(dict.fromkeys(palavras_ordenadas))
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for palavra in unicas:
            arquivo.write(palavra + "\n")
    return unicas


def main():
    palavras = ler_palavras(DOCUMENTO)

    # Cada item é (chave sem acento, palavra original)
    itens = [(chave_alfabetica(p), p) for p in palavras]

    inicio = time.perf_counter()
    itens.sort()
    fim = time.perf_counter()

    palavras_ordenadas = [palavra for _, palavra in itens]

    print(f"Documento: {DOCUMENTO.name}")
    print(f"Palavras lidas: {len(palavras)}")
    print("\n=== Palavras ordenadas com sort ===")
    print(textwrap.fill(", ".join(palavras_ordenadas), width=100))
    print(f"\nTempo de execução do sort: {(fim - inicio) * 1000:.3f} ms")

    unicas = gravar_glossario(GLOSSARIO, palavras_ordenadas)
    print(f"Glossário gravado em {GLOSSARIO.name} com {len(unicas)} palavras diferentes.")


if __name__ == "__main__":
    main()
