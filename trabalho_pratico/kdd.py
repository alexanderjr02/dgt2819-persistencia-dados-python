"""
Trabalho prático: glossário de palavras ordenadas (MVP do dicionário de termos jurídicos).

Lê o documento txt linha a linha, separa as palavras e compara o tempo de três formas
de ordenação: Bubble Sort, Selection Sort e o método nativo sort.

Uso:
    python kdd.py              compara os três métodos
    python kdd.py bubble       executa só o Bubble Sort
    python kdd.py selection    executa só o Selection Sort
    python kdd.py sort         executa só o sort nativo
"""

import string
import sys
import textwrap
import time
import unicodedata
from pathlib import Path

PASTA = Path(__file__).parent
DOCUMENTO = PASTA / "documento.txt"

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


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temporario = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temporario


def selection_sort(array):
    for i in range(len(array)):
        menor = i
        for j in range(i + 1, len(array)):
            if array[menor] > array[j]:
                menor = j
        array[i], array[menor] = array[menor], array[i]


def sort_nativo(array):
    array.sort()


METODOS = {
    "bubble": ("Bubble Sort", bubble_sort),
    "selection": ("Selection Sort", selection_sort),
    "sort": ("sort (nativo do Python)", sort_nativo),
}


def executar(nome, funcao, itens):
    """Ordena uma cópia dos itens, mede o tempo e imprime o resultado."""
    copia = list(itens)

    inicio = time.perf_counter()
    funcao(copia)
    fim = time.perf_counter()

    palavras_ordenadas = [palavra for _, palavra in copia]
    tempo_ms = (fim - inicio) * 1000

    print(f"\n=== {nome} ===")
    print(textwrap.fill(", ".join(palavras_ordenadas), width=100))
    print(f"Tempo de execução: {tempo_ms:.3f} ms")
    return palavras_ordenadas, tempo_ms


def main():
    escolha = sys.argv[1].lower() if len(sys.argv) > 1 else "todos"
    if escolha != "todos" and escolha not in METODOS:
        print(f"Método desconhecido: {escolha}. Use bubble, selection, sort ou nada para todos.")
        sys.exit(1)

    palavras = ler_palavras(DOCUMENTO)

    # Cada item é (chave sem acento, palavra original): os três métodos comparam
    # exatamente os mesmos valores, o que deixa a comparação de tempo justa
    itens = [(chave_alfabetica(p), p) for p in palavras]

    print(f"Documento: {DOCUMENTO.name}")
    print(f"Palavras lidas: {len(palavras)}")

    selecionados = METODOS if escolha == "todos" else {escolha: METODOS[escolha]}
    resultados = {}
    for codigo, (nome, funcao) in selecionados.items():
        resultados[codigo] = executar(nome, funcao, itens)

    if len(resultados) > 1:
        listas = [lista for lista, _ in resultados.values()]
        iguais = all(lista == listas[0] for lista in listas)

        print("\n=== Resumo ===")
        for codigo, (_, tempo_ms) in sorted(resultados.items(), key=lambda r: r[1][1]):
            print(f"{METODOS[codigo][0]:<26}{tempo_ms:>12.3f} ms")
        print(f"Os três métodos produziram a mesma ordem: {'sim' if iguais else 'não'}")


if __name__ == "__main__":
    main()
