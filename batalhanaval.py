'''
*-- EQUIPE --*
Henrique Martins - RM563620
Henrique Texeira - RM563088
*-- -====- --*

TITULO: Escrita personalizada no site FSymbols
'''
# Importações
import random
import os

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
    while True:
        print(
            '1. Single Player'
            f'\n2. Multiplayer'
            f'\n3. Como jogar?'
            f'\n4. Sair'
        )
        try:
            user_opcao = int(input('Escolha uma opção: '))
            if user_opcao < 1 or user_opcao > 4:
                print('❌ Digite apenas números do menu.')
            else:
                return user_opcao
        except ValueError:
            print('❌ Letras não são permitidas, digite apenas números.')

def redirecionar_opcao(user_opcao):
    if user_opcao == 1:
        pass
    elif user_opcao == 2:
        multiplayer()
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
    os.system('cls' if os.name == 'nt' else 'clear')

def multiplayer():
    tabuleiro = criar_tabuleiro()
    posicionar_navios(tabuleiro)
    navios_acertados = 0
    tentativas = 0

    print("Bem-vindo ao Batalha Naval!")
    print("Tente acertar os 3 navios escondidos no tabuleiro.")

    while navios_acertados < 3:
        mostrar_tabuleiro(tabuleiro)
        try:
            linha = int(input("Escolha a linha (0-4): "))
            coluna = int(input("Escolha a coluna (0-4): "))
            resultado = atacar(tabuleiro, linha, coluna)
            if resultado != None:
                tentativas += 1
                if resultado:
                    navios_acertados += 1
        except:
            print("Entrada inválida. Digite números de 0 a 4.")

    print(f"Parabéns! Você acertou todos os navios em {tentativas} tentativas.")
    print("Tabuleiro final (navios mostrados):")
    mostrar_tabuleiro(tabuleiro)
    
def main():
    jogo_titulo()
    opcao = menu_opcoes()    
    redirecionar_opcao(opcao)
    
main()
