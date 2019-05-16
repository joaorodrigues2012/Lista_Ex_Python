# 1. Faça a seguinte simulação com dois geradores.
# O primeiro gerador representa um atendente de restaurante. Ele devolve, logo no
# início, uma lista com os produtos que o restaurante oferece. Crie uma lista com cinco
# tipos de lanches e dois tipos de bebidas. Cada produto deve ter seu preço.
# O segundo gerador é um cliente que está ligando para o restaurante. Após receber a
# lista de produtos disponíveis, o cliente escolhe um deles aleatoriamente.
# Após a primeira escolha do cliente, o atendente informa qual o seu gasto atual e
# mostra o menu novamente.
# O cliente, por sua vez, escolhe um outro produto ou então envia a mensagem
# “Tchau”, indicando que não irá comprar mais nada.
# Ao receber a mensagem “Tchau”, o atendente deve dizer qual o total gasto pelo
# cliente.

import random

MENU = {
    'X-Salada':5,
    'esfilha':2.9,
    'cozinha':3,
    'refrigerante':4,
    'suco':2.5,
    'Tchau':1
}

def atedente():
    while True:
        yield MENU



def speaker ():
    precoTotal = 0
    while True:
        nome, preco = random.choice(list(MENU.items()))
        if nome != "Tchau":
            print('O cliente escolheu o produto é', nome, ' e preço é R$', preco)
            precoTotal = precoTotal + preco
        else:
             print(nome,'e o valor total é R$',precoTotal)
             break


c = atedente()
print(next(c))
speaker()



