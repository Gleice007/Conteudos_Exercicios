"""
Adicionar e Remover itens de uma lista 
Adicionar:
lista.append(item)

Remover:
item_removido = lista.pop(indice)
lista.remove(item)

Digamos que você está construindo o controle de produtos 
da Apple. E a Apple lançou o IPhone 11 e irá tirar 
dos seus estoques o IPhone X
"""


produtos = ['apple tv', 'mac', 'iphone x', 'IPad', 'apple watch', 'mac bool', 'airpods']
# Para trocar um intem da lista é feito dessa seguinte forma:
#produtos[2] = 'iphone 11'
print(produtos)

# Para acrescentar um item na lista é feito dessa forma:
produtos.append('iphone 11')
print(produtos)

# Remover um item da lista 
produtos.remove('iphone x')
print(produtos)

# Remover um item da lista de outra forma
item_removido = produtos.pop(2)
print(produtos)
print('Removemos o {} da lista'.format(item_removido))

"""
Existem 2 formas de tratar o erro:
1. Criar um if para evitar que ele aconteça
2. Esperar que ele possa acontecer e tratar caso o erro aconteça com:
"""
try:
    produtos.remove('mac') #caso errado
    print(produtos) 
except:
    print('iphonex não existe na lista de produtos')    
