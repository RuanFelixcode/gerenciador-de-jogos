from modulo import continuar,registrar_jogo



class Vendedor:
    def __init__(self):
        self.estoque = {}

    
    def cadastrar_jogo(self):
        while True:
            genero,nome,preco = registrar_jogo()
            if genero in self.estoque:
                self.estoque[genero].update({nome:preco})
            else:
                self.estoque.update({genero:{nome:preco}})
            print('novo jogo?')
            if continuar():
                break
                
    def buscar(self):
        print('voce acessou a função de busca')
        while True:
            busca_genero = input('digite o genero do jogo:').strip()
            if busca_genero in self.estoque:
                print(f'jogos e preços do genero:{busca_genero}')
                for i,p in self.estoque[busca_genero].items():
                    print(f'nome:{i} preço:{p}')
            else:
                print('genero não encontrado')

            print('nova busca?')
            if continuar():
                break

    def remover_jogo(self):
        print('voce acessou a função remover jogo')
        while True:
            opc = input('deseja remover um jogo ou genero?(j/g)').strip().lower()
            if opc == 'g':
                genero_remover = input('digite o genero a ser removido:').strip()
                if genero_remover in self.estoque:
                    self.estoque.pop(genero_remover)
                else:
                    print('genero não existe')
            elif opc == 'j':
                buscar_genero = input('digite o genero do jogo:').strip()
                if buscar_genero in self.estoque:
                    jogo_remover = input('digite o jogo a ser removido:')
                    if jogo_remover in self.estoque[buscar_genero]:
                        self.estoque[buscar_genero].pop(jogo_remover)
                    else:
                        print('jogo não existe')
            else:
                print('opção invalida')

            if continuar():
                break




            
        
