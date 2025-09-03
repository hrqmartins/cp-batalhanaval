'''
*-- EQUIPE --*
Henrique Martins - RM563620
Henrique Texeira - RM563088
*-- -====- --*

TITULO: Escrita personalizada no site FSymbols
'''
import random

def jogo_titulo():
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
    print(
        '1. Single Player'
        f'\n2. Multiplayer'
        f'\n3. Como jogar?'
        f'\n4. Sair'
        )
    while True:
        try:
            user_opcao = int(input('Escolha uma opção: '))
            if user_opcao < 0 or user_opcao > 4:
                print('❌ Digite apenas números do menu.')
        except ValueError:
            print('❌ Letras não são permitidas, digite apenas números.')

def redirecionar_opcao(user_opcao):
    if user_opcao == 1:
        pass
    elif user_opcao == 2:
        pass
    elif user_opcao == 3:
        pass
    else:
        pass

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
    for i in range(5):
        print(i, end=' ')
        for j in range(5):
            if tabuleiro[i][j] == 'N':  # esconde navio
                print('~', end=' ')
            else:
                print(tabuleiro[i][j], end=' ')
        print()
    print()