produtos = ['Tv', 'Celular', 'Tablet', 'Mouse', 'Teclado', 'Geladeira', 'Forno']
estoque = [100, 150, 100, 120, 70, 180, 80]

i = produtos.index('Geladeira')
qtde_estoque = estoque[i]
#print('Quantidade em estoque da geladeira é de: {}'.format(qtde_estoque))

"""
 Crie um programa para fazer uma consulta de estoque. O
 usuário do programa deve inserir o nome do produto e,
 caso ele não exista na list, ele avisado. Casó exista,
 o programa deve dizer a quantidade de unidades em
 estoque do produto.
"""

produto = input("Insira o nome do produto desejado: ")
if produto in produtos:
    i = produtos.index(produto)
    qtde_estoque = estoque[i]
    print('Temos {} unidades de {} no estoque'.format(qtde_estoque, produto))
else:
    print('{} Esse produto não existe no estoque!'.format(produto))    