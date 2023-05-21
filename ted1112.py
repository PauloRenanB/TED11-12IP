import csv
from os import name, system


def limparLinha():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def maiorPublicoDeFilmes(filmes):
    cabecalho = next(filmes)
    totalPublico = 0
    nomeDoFilme = ''
    anoDeExibicao = ''

    for i, filme in enumerate(filmes):
        coluna = float(filme[9])

        if coluna > totalPublico:
            totalPublico = coluna
            nomeDoFilme = filme[2]
            anoDeExibicao = filme[1]
        else:
            continue

    print(f'O filme com maior publico é {nomeDoFilme}')
    print(f'Total do publico é {totalPublico}')
    print(f'Ano de exibição é {anoDeExibicao} ')


with  open('filmes.csv', newline='', encoding='utf-8') as filmes:
    limparLinha()

    lerFilmes = csv.reader(filmes)

    maiorPublicoDeFilmes(lerFilmes)
