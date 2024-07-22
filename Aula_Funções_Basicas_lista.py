"""
Algumas Funções Básicas de Lista

Tamanho da Lista
tamanho = len(lista)
"""

produtos = ['apple tv', 'mac', 'iphone x', 'IPad', 'apple watch', 'mac book', 'airpods']

# 1. Quantos produtos temos a venda?
# Para saber quantos produtos temos, primeiro criamos uma variavel chamada tamanho
# logo depois usamos a função len(serve para conta os itens dentro de uma lista)
# depois usamos a função format para escrever um texto detalhado para o usuario.

tamanho = len(produtos)
print('Temos {} produtos'.format(tamanho))

"""
Maior e Menor Valor

maior = max(lista)

menor = min(lista)
"""

# Qual o item mais vendido?
# Qual o item menos vendido?

vendas= [1000, 1500, 15000, 270, 900, 100, 1200]
mais_vendido = max(vendas)
menos_vendido = min(vendas)
print('O produto mais vendido teve {} unidades vendidas e o menos vendido teve {} unidades vendidas'.format(mais_vendido, menos_vendido))

i = vendas.index(mais_vendido)
produto_mais_vendido = produtos[i]
print(produto_mais_vendido)


i = vendas.index(menos_vendido)
produto_menos_vendido = produtos[i]
print(produto_menos_vendido)