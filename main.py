def quantidade(broto_qnt, ascend_qnt, radicerne_qnt, beladona_qnt, tocha_qnt):


    menor = broto_qnt

    if broto_qnt < menor:
        menor = broto_qnt
    if ascend_qnt < menor:
        menor = ascend_qnt
    if radicerne_qnt < menor:
        menor = radicerne_qnt
    if beladona_qnt < menor:
        menor = beladona_qnt
    if tocha_qnt < menor:
        menor = tocha_qnt
    
    return menor

def lucro_def():
    broto = (10)
    ascend = int(10)
    radicerne = int(12)
    beladona = int(2)
    tocha = int(8)
    gold_atual = int(115000)


    craft = ((beladona*3) + (ascend*4) + (radicerne * 4) + (broto * 4) + (tocha * 4) )
    frasco = int(172)
    lucro = frasco - craft 
    if craft<frasco:
        print(f'O custo do craft é {craft:.2f}, seu lucro seria {(lucro):.2f}g')
        print(f'com {gold_atual}g, você iria ter de lucro {((gold_atual / craft) * lucro):.0f}g')
        print()
    else:
        print(f'O custo do craft é {craft:.2f}, seu prejuizo seria {(lucro):.2f}g')
        print()

def quantidade_print():
    broto_qnt = int(input('Digite a quantidade de Broto: '))
    ascend_qnt = int(input('Digite a quantidade de Ascedente: '))
    radicerne_qnt = int(input('Digite a quantidade de Radicerne: '))
    beladona_qnt = int(input('Digite a quantidade de Beladona: '))
    tocha_qnt = int(input('Digite a quantidade de Tocha: '))
    broto_qnt = broto_qnt/4
    ascend_qnt = ascend_qnt/4
    radicerne_qnt = radicerne_qnt/4
    beladona_qnt = beladona_qnt/4
    tocha_qnt = tocha_qnt/4
    faltante = quantidade(broto_qnt, ascend_qnt, radicerne_qnt, beladona_qnt, tocha_qnt)//4
    print(f'Total de crafts: {quantidade(broto_qnt, ascend_qnt, radicerne_qnt, beladona_qnt, tocha_qnt)}')
    print(f'Com mais {faltante} você consegue craftar outro item')
    print()

def quantity():
    #1 = Gloria
    #2 = Radicerne
    #3 = Broto
    #4 = Tocha
    itens = [8.68, 11.93, 7.50, 7.53]

    quantity = int(input(f'Digite a quantidade de itens desejada: '))
    gold = int(input(f'Digite a quantidade de gold disponivel: '))
    print()
    mostexpensive = max(itens)

    if (mostexpensive*quantity)*4 > gold:
        print('Muito caro')
    else:
        gold_total = ((itens[0]*quantity) + (itens[1]*quantity) + (itens[2]*quantity) + (itens[3]*quantity))
        print(f'Se tu comprar 300 unidades de cada, você irá gastar: {gold_total}, e irá sobrar: {gold - gold_total}')
        quantity_extra = ((gold - gold_total)/max(itens))/4 # Quantidade a mais que pode comprar
        overall_itens = quantity + quantity_extra 
        print(f'Você pode comprar {overall_itens:.0f} itens de cada')
        print()
        print()

def menu():
    print('Digite 1 para saber a quantidade de craft disponivel.')
    print('Digite 2 para saber a margem de lucro.')
    print('Digite 3 para saber a quantidade para comprar')
    print('Digite 0 para sair do aplicativo.')
    app = int(input('O Que deseja? '))
    print()
    
    if app == 1:
        quantidade_print()
    if app == 2:
        lucro_def()
    if app == 3:
        quantity()
    if app == 0:
        exit()

while True:
    menu()