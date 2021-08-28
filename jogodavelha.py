
from funcoesJDV import *


def main():
    while True:
        print('<----------Menu---------->')
        print('1 - Cadastrar um jogador')
        print('2 - Excluir um jogador')
        print('3 - Verificar pontuação')
        print('4 - Iniciar o Jogo')
        print('5 - Sair')
        print()
        opcao = input()

        if opcao == '1':
            novojogador()
        elif opcao == '2':
            excluirjogador()
        elif opcao == '3':
            verificapontuacao()
        elif opcao == '4':
            jogar()
        elif opcao == '5':
           break

main()
