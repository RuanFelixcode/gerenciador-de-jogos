def continuar():
    while True:
        opc = input('deseja continuar(s/n):').strip().lower()
        if opc in ('nao','n','não'):
            return True
        elif opc in ('s','sim'):
            return False
        else:
            print('opção invalida')

def registrar_jogo():
    while True:
        try:
            genero = input('digite o genero do jogo:').strip()
            if not genero.replace(' ','').isalpha():
                print('não e permitido numeros no genero, somente letras são permitidas.')
                continue
            
            nome = input('digite o nome do jogo:').strip()
            if not nome.replace(' ','').isalnum():
                print('não e permitido caracteres especiais so letras e numeros.')
                continue
            
            preco = float(input(f'genero:{genero}-jogo:{nome}\ndigite o preço:').strip())
            if preco <=0:
                print('preços negativos ou zero não são permitidos.')
                continue
            return genero,nome,preco
   
        except ValueError:
                print('so e permitido digitar numeros inteiros ou reais.')

            
