"""
Exercício do Módulo 1 - Operações, Variáveis e Input

Parte 1 -Operações e Variáveis

Crie um programa que imprima (print) os principais indicadores da loja Hashtag&Drink no último ano. Obs: faça tudo usando variáveis.

valores do último ano:

Quantidade de Vendas de Coca = 150 Quantidade de Vendas de Pepsi = 130 Preço Unitário da Coca = 1,50 Preço Unitário da Pepsi = 1,50 Custo da loja: 2.500,00

Use o bloco abaixo para criar todas as variáveis que precisa
"""

qntd_pepsi = 130
qntd_coca = 150
unid_coca = 1.50
unid_pepsi = 1.50
custo_loja = 2500

# 1º Qual foi o faturamento de Pepsi da Loja ?
print(qntd_pepsi * unid_pepsi)

# 2º Qual foi o de Coca da Loja ?
print(qntd_coca * unid_coca)

# 3º Qual foi o Lucro da Loja ?
faturamento = qntd_coca * unid_coca + qntd_pepsi * unid_pepsi
lucro = faturamento - custo_loja
print(lucro)

# 4º Qual foi a Margem da Loja ? (Lembre-se, margem = lucro/faturamento). não precisa formatar em percentual
print(lucro / faturamento)

"""
Parte 2 - inputs e strings
A maioria das empresas trabalham com um Código para cada produto que possuem. A Hashtag&Drink, por exemplo, tem mais de 1.000 
prodrutos e possui um código para cada produto. Ex:
Coca -> Código: BEB1300543
Pepsi -> Código: BEB1300545
Vinho Primitivo Lucarelli -> Código: BAC1546001
Vodka Smirnof -> Código: BAC17675002

Repare que todas as bebidas não alcóolicas tem inicio do Código "BEB" e todas as bebidas alcóolicas tem início do código "BAC".
Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcóolica. O programa deve responder True para
bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, use um input

Dica: Lembre-se do comando in para strings e sempre insira os códigos com letra maiúscula para facilitar.  
"""

