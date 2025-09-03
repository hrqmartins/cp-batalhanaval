'''
*-- EQUIPE --*
Henrique Martins - RM563620
Henrique Texeira - RM563088
*-- -====- --*

TITULO: Escrita personalizada no site FSymbols
'''

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


    