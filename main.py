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

def menu():
    print('Digite 1 para saber a quantidade de craft disponivel.')
    print('Digite 2 para saber a margem de lucro.')
    print('Digite 0 para sair do aplicativo.')
    app = int(input('O Que deseja? '))
    print()
    
    if app == 1:
        quantidade_print()
    if app == 2:
        lucro_def()
    if app == 0:
        exit()

while True:
    menu()