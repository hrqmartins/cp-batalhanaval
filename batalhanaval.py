'''
*-- EQUIPE --*
Henrique Martins - RM563620
Henrique Texeira - RM563088
*-- -====- --*

TITULO: Escrita personalizada no site FSymbols.
OS: Para limpar o terminal e ficar mais limpo o programa.
RANDOM: Para colocar os navios de forma aleatória.
'''

# Importações
import random
import os

def jogo_titulo():
    ''' 
    Exibe o titulo do jogo 
    '''
    print('==============================================')
    print(
        f'''  
░██████╗███████╗██╗░██████╗░██╗░░░██╗███╗░░██╗
██╔════╝██╔════╝██║██╔════╝░██║░░░██║████╗░██║
╚█████╗░█████╗░░██║██║░░██╗░██║░░░██║██╔██╗██║
░╚═══██╗██╔══╝░░██║██║░░╚██╗██║░░░██║██║╚████║
██████╔╝███████╗██║╚██████╔╝╚██████╔╝██║░╚███║
╚═════╝░╚══════╝╚═╝░╚═════╝░░╚═════╝░╚═╝░░╚══╝
       \n      ⚓ B A T A L H A   N A V A L 🚢
        '''
    )
    print('==============================================')
    
def menu_opcoes():
    ''' 
    Exibe opções do menu com tratamento de erros 
    '''
    while True:
        print(
            '1. Iniciar Batalha'
            f'\n2. Como Funciona?'
            f'\n3. Sair'
        )
        try:
            user_opcao = int(input('Escolha uma opção: '))
            if user_opcao < 1 or user_opcao > 3:
                limpar_terminal()
                print('❌ Digite apenas números do menu.')
                voltar_menu()
            else:
                return user_opcao
        except ValueError:
            limpar_terminal()
            print('❌ Letras não são permitidas, digite apenas números.')
            voltar_menu()

def redirecionar_opcao(user_opcao):
    ''' 
    Leva o usuário para a opção que ele escolheu 
    '''
    if user_opcao == 1:
        batalha()
    elif user_opcao == 2:
        funcionamento()
    else:
        print('Encerrando programa..')
        return None
    
def criar_tabuleiro():
    '''
    Função para criar o tabuleiro
    '''
    tabuleiro = []
    for i in range(5):
        linha = []
        for j in range(5):
            linha.append('~')  # Água
        tabuleiro.append(linha)
    return tabuleiro

def mostrar_tabuleiro(tabuleiro):
    '''
    Função para mostrar o tabuleiro sem revelar os navios
    '''
    print("  0 1 2 3 4")
    for x in range(5):
        print(x, end=' ')
        for y in range(5):
            if tabuleiro[x][y] == 'N':  # esconde navio
                print('~', end=' ')
            else:
                print(tabuleiro[x][y], end=' ')
        print()
    print()
    
def posicionar_navios(tabuleiro):
    '''
    Função para posicionar os navios aleatoriamente.
    '''
    navios = 0
    while navios < 3:
        linha = random.randint(0,4)
        coluna = random.randint(0,4)
        if tabuleiro[linha][coluna] != 'N':
            tabuleiro[linha][coluna] = 'N'
            navios += 1

def atacar(tabuleiro, linha, coluna):
    '''
    Função para atacar uma posição do tabuleiro.
    '''
    if tabuleiro[linha][coluna] == 'N':
        tabuleiro[linha][coluna] = 'X'
        print("Acertou um navio!")
        return True
    elif tabuleiro[linha][coluna] == '~':
        tabuleiro[linha][coluna] = 'O'
        print("Água!")
        return False
    else:
        print("Você já atacou essa posição.")
        return None

def limpar_terminal():
    '''
    Limpa o terminal
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

def batalha():
    '''
    Inicia a batalha naval
    O jogador deve tentar encontrar os 3 navios escondidos no tabuleiro.
    '''
    limpar_terminal()
    tabuleiro = criar_tabuleiro()
    posicionar_navios(tabuleiro) 
    navios_acertados = 0
    tentativas = 0

    print(f'\n==================================================')
    print('    Bem-vindo ao Seigun - Batalha Naval!')
    print('Tente acertar os 3 navios escondidos no tabuleiro.')
    print('==================================================')

    while navios_acertados < 3:
        mostrar_tabuleiro(tabuleiro)
        try:
            linha = int(input("Escolha a linha (0-4): "))
            coluna = int(input("Escolha a coluna (0-4): "))
            print()
            print('*-- -=X=- --*')
            print()
            resultado = atacar(tabuleiro, linha, coluna)
            if resultado != None:
                tentativas += 1
                if resultado:
                    navios_acertados += 1
        except:
            print("Entrada inválida. Digite números de 0 a 4.")

    print(f"Parabéns! Você acertou todos os navios em {tentativas} tentativas.")
    print("Tabuleiro final:")
    mostrar_tabuleiro(tabuleiro)
    voltar_menu()

def voltar_menu():
    '''
    Função para voltar ao menu
    '''
    input('Pressione ENTER para voltar ao menu ')
    limpar_terminal()
    main()

def funcionamento():
    '''
    Mostra todas as instruções de funcionamento do jogo.
    '''
    limpar_terminal()
    print(f'''
*-=-=-=-=-=-=-=-=-=- SEIGUN -=-=-=-=-=-=-=-=-=-*
Como jogar:

1. O jogo é disputado em um tabuleiro 5x5.
2. Existem 3 navios escondidos no tabuleiro.
3. Cada turno você escolhe uma linha e uma coluna para atacar.
4. Se acertar um navio, ele será marcado com "X".
5. Se errar, a água será marcada com "O".
6. Você não pode atacar a mesma posição duas vezes.
7. O objetivo é acertar todos os navios com o menor número de tentativas.

Dicas:
- Observe onde você já atacou para não repetir posições.
- Planeje seus ataques para descobrir os navios rapidamente.

Boa sorte!
-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=-=-
''')
    voltar_menu()

def main():
    '''
    Função principal do programa
    '''
    jogo_titulo()
    opcao = menu_opcoes()    
    redirecionar_opcao(opcao)
    
main()
