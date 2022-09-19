itens = [7.73, #Gloria
        11.38, #Radicerne
        9.29,  #Broto
        7.30,  #Tocha
        1.70]  #Beladona
frasco = [154.32]
gold_atual = int(input('Digite a quantidade de gold atual: '))

def quantidade(broto_qnt, ascend_qnt, radicerne_qnt, beladona_qnt, tocha_qnt): #Checa o menor valor da função quantidade_print() e retorna


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

def quantidade_print(): #Quantidade de itens possiveis para craft
    beladona_qnt = int(input('Digite a quantidade de Beladona: '))
    broto_qnt = int(input('Digite a quantidade de Broto: '))
    ascend_qnt = int(input('Digite a quantidade de Ascedente: '))
    radicerne_qnt = int(input('Digite a quantidade de Radicerne: '))
    tocha_qnt = int(input('Digite a quantidade de Tocha: '))
    print()
    broto_qnt = broto_qnt/4
    ascend_qnt = ascend_qnt/4
    radicerne_qnt = radicerne_qnt/4
    beladona_qnt = beladona_qnt/3
    tocha_qnt = tocha_qnt/4
    total_craft = quantidade(broto_qnt, ascend_qnt, radicerne_qnt, beladona_qnt, tocha_qnt)
    print(f'Total de crafts: {total_craft}')
    print(f'Você irá demorar {(total_craft*2.5)/60:.0f} minutos para craftar')
    print()


def lucro_def(): #Lucro do Frasco de Poder Espectral


    craft = ((itens[4]*3) + (itens[0]*4) + (itens[1] * 4) + (itens[2] * 4) + (itens[3] * 4) )
    lucro = frasco[0] - craft 
    if craft<frasco[0]:
        print(f'O custo do craft é {craft:.2f}, seu lucro seria {(lucro):.2f}g')
        print(f'com {gold_atual}g, você iria ter de lucro {((gold_atual / craft) * lucro):.0f}g')
        print()
    else:
        print(f'O custo do craft é {craft:.2f}, seu prejuizo seria {(lucro):.2f}g')
        print()



def quantity(): #Quantos Frasco de Poder Espectral, consegue craftar com a quantia de gold atual.

    quantity = int(input(f'Digite a quantidade de itens desejada: '))
    print()
    mostexpensive = max(itens)

    if (mostexpensive*quantity)*4 > gold_atual:
        print('Você não consegue comprar essa quantidade de itens com esse gold')
    else:
        gold_total = ((itens[0]*quantity) + (itens[1]*quantity) + (itens[2]*quantity) + (itens[3]*quantity))
        print(f'Se tu comprar {quantity} unidades de cada, você irá gastar: {(gold_total):.2f}, e irá sobrar: {gold_atual - gold_total}')
        quantity_extra = ((gold_atual - gold_total)/max(itens))/4 # Quantidade a mais que pode comprar
        overall_itens = quantity + quantity_extra 
        print(f'Você pode comprar {overall_itens:.0f} itens de cada')
        print()
        print()

def menu():
    print('Digite 1 para saber a quantidade para comprar')
    print('Digite 2 para saber a quantidade de craft disponivel.')
    print('Digite 3 para saber o seu lucro')
    print('Digite 0 para sair do aplicativo.')
    app = int(input('O Que deseja? '))
    print()
    
    if app == 1:
        quantity()
    if app == 2:
        quantidade_print()
    if app == 3:
        lucro_def()
    if app == 0:
        exit()

while True:
    menu()
    