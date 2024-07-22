"""
Juntar Listas, Ordenar e Cuidados Especiais 
2 Formas
. lista1.extend(lista2)
. lista_nova = lista1 + lista2

Obs: o Método .append não junta listas, mas adiciona um valor no final da lista
"""

produtos = ['apple tv', 'mac', 'iphone x', 'IPad', 'apple watch', 'mac book', 'airpods']
novos_produtos = ['iphone 12', 'ioculos']
produtos.extend(novos_produtos)
todos_produtos = produtos + novos_produtos
#print(todos_produtos)

# Cuidado:
# . [1] + [2] não é a mesma coisaa que 1 + 2, então cuidado sempre com o formato dos valores na hora de 
# fazer operações.

vendas = [1000, 1500, 15000, 20000, 270, 900, 100, 1200]
vendas_iphonex = [15000]
vendas_iphone11 = [20000]

total_iphone = vendas[2] + vendas[3]
total_iphone_listas = vendas_iphonex[0] + vendas_iphone11[0]
print(total_iphone)
print(total_iphone_listas)

# Ordenar listas
#lista.sort()
produtos.sort(reverse=False)
print(vendas)