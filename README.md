# DGT2819 | Persistência de dados com Python

Trabalho prático **"Colocando tudo em ordem e guardando"**: algoritmos de ordenação e leitura/escrita de
arquivos em Python, aplicados na criação de um glossário de palavras ordenadas, primeiro passo de um
dicionário de termos jurídicos.

Não há dependências externas: tudo usa apenas a biblioteca padrão do Python (testado no Python 3.12).

## Estrutura

```
.
├── microatividades/
│   ├── array.sort.py          1. ordenação com o método sort (crescente e decrescente)
│   ├── bubble.sort.py         2. algoritmo Bubble Sort
│   ├── selection.sort.py      3. algoritmo Selection Sort
│   ├── ler.txt.py             4. leitura de arquivo com open e com with
│   ├── loremipsum.txt            arquivo lido na microatividade 4
│   ├── escrever.txt.py        5. escrita de arquivo a partir de uma lista
│   └── texto.txt                 arquivo gerado na microatividade 5
└── trabalho_pratico/
    ├── kdd.py                 leitura do documento, ordenação e gravação do glossário
    ├── documento.txt          texto jurídico usado como entrada (contrato fictício)
    └── palavras_ordenadas.txt glossário gerado pelo kdd.py
```

## Como executar

No VS Code, abra a pasta do projeto, abra o script e clique no botão **Run Python File** (triângulo no canto
superior direito). Pelo terminal:

```bash
python microatividades/array.sort.py
python microatividades/bubble.sort.py
python microatividades/selection.sort.py
python microatividades/ler.txt.py
python microatividades/escrever.txt.py
python trabalho_pratico/kdd.py
```

Os scripts localizam os arquivos txt pela própria pasta, então funcionam a partir de qualquer diretório.

## Trabalho prático: kdd.py

1. Cria uma lista com `list()`.
2. Com a instrução `with`, lê o `documento.txt` linha a linha.
3. Separa cada linha em palavras com `split()`, tira a pontuação das pontas, deixa em minúsculas e adiciona à lista.
4. Ordena as palavras e mede o tempo com a biblioteca `time`.
5. Grava o resultado em `palavras_ordenadas.txt`, uma palavra por linha e sem repetições.

Para a ordem ficar correta em português, a comparação usa a palavra sem acentos como chave: assim
"ação" fica perto de "acesso", e não depois do "z", como aconteceria comparando os caracteres diretamente.

### Comparação de desempenho

Antes da versão final, o `kdd.py` ordenou as mesmas 550 palavras com **Bubble Sort**, **Selection Sort** e o
método nativo **sort**, e o script foi executado 5 vezes para cada método (`python kdd.py bubble`,
`python kdd.py selection` e `python kdd.py sort`). Essa versão está preservada no histórico do repositório,
no commit [Compara Bubble Sort, Selection Sort e sort](https://github.com/alexanderjr02/dgt2819-persistencia-dados-python/blob/6ec0194/trabalho_pratico/kdd.py).

| Método | Execuções (ms) | Média |
|---|---|---|
| Bubble Sort | 28,43 · 27,76 · 28,31 · 17,78 · 37,44 | **27,94 ms** |
| Selection Sort | 11,33 · 14,11 · 16,15 · 15,30 · 22,33 | **15,85 ms** |
| sort (nativo) | 0,42 · 0,25 · 0,34 · 0,32 · 0,45 | **0,36 ms** |

Os três métodos produziram exatamente a mesma ordem. O `sort` foi cerca de **79 vezes mais rápido** que o
Bubble Sort e **45 vezes mais rápido** que o Selection Sort. Bubble e Selection fazem da ordem de n² comparações
(com 550 palavras, mais de 150 mil), enquanto o `sort` usa o Timsort, de ordem n log n e implementado em C.
Por isso o `sort` foi o método escolhido, e os outros dois foram removidos da versão final, como pede o roteiro.
Num dicionário jurídico completo, com milhares de documentos, essa diferença cresceria muito.

### Resultado

```
Palavras lidas: 550
Tempo de execução do sort: 0.414 ms
Glossário gravado em palavras_ordenadas.txt com 281 palavras diferentes.
```
