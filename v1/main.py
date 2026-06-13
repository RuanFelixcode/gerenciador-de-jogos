from vendedor_jogos import Vendedor

sistema = Vendedor()

while True:
    print('''menu do vendedor\nopções:\n1 - buscar\n2 - cadastrar jogo\n3 - remover jogo\n4- sair''')
    opc = int(input('selecione uma opção:'))
    if opc == 1:
        sistema.buscar()
    elif opc == 2:
        sistema.cadastrar_jogo()
    elif opc == 3:
        sistema.remover_jogo()
    elif opc == 4:
        break
    else:
        print('opção invalida')
