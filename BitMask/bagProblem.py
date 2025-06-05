
'''2. Problema de mochila (versão pequena)
Você tem itens com pesos e valores, e uma mochila com capacidade limitada. 
Use bitmask para testar todas as combinações possíveis de itens e encontrar o maior valor total 
sem ultrapassar o peso máximo.'''

v = []
resp = 0
maior = []

quantidade_itens = int(input("Quantidade de itens: "))
peso_maximo = float(input("Peso máximo em Kg que a mochila aguenta: "))

for i in range(quantidade_itens):
    v.append(float(input(f"Peso do item {i+1} em Kg: ")))

for mask in range((1 << quantidade_itens)):
    soma = 0
    itens = []
    for i in range(quantidade_itens):
        if(mask &(1<<i)):
            soma+=v[i]
            itens.append(i+1)
            

    if  soma <= peso_maximo:
        if len(maior)<len(itens):
            maior = itens
        

print("Quantidade de itens máximos que cabem na mochila: ",len(maior))
print("Itens", maior)
