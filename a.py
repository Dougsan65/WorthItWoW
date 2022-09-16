#1 = Gloria
#2 = Radicerne
#3 = Broto
#4 = Tocha


def cheaper():
    itens = [8.68, 11.93, 7.50, 7.53]

    quantity = int(input(f'Digite a quantidade de itens desejada: '))
    gold = int(input(f'Digite a quantidade de gold disponivel: '))
    mostexpensive = max(itens)

    if (mostexpensive*quantity)*4 > gold:
        print('Muito caro')
    else:
        gold_total = ((itens[0]*quantity) + (itens[1]*quantity) + (itens[2]*quantity) + (itens[3]*quantity))
        print(f'Se tu comprar 300 unidades de cada, você irá gastar: {gold_total}, e irá sobrar: {gold - gold_total}')
        quantity_extra = ((gold - gold_total)/max(itens))/4 # Quantidade a mais que pode comprar
        overall_itens = quantity + quantity_extra 
        print(f'Você pode comprar {overall_itens:.0f} itens de cada')


cheaper()