
from time import sleep
import os.path

perdedor = ' '
vencedor = ' '
matriz = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]


# função para resetar matriz ao final de cada jogo
def reset():
    global matriz
    global vencedor
    global perdedor 
    vencedor = ' '
    perdedor = ' '
    matriz = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
    ]


# função para criar um novo jogador
def novojogador():
    nome = input('Digite o nome do novo jogador: ')
    if os.path.isfile('{}.txt'.format(nome)):
        print('Jogador {} ja registrado.'.format(nome))
        sleep(1)
    else:
        print('Registrando {}...'.format(nome))
        f = open('{}.txt'.format(nome), 'w')
        f.write('0\n')
        f.write('0\n')
        f.close()
        sleep(1)


# função para excluir um jogador
def excluirjogador():
    nome = input('Digite o nome do jogador que quer excluir: ')
    if os.path.isfile('{}.txt'.format(nome)):
        print('Excluindo jogador {}...'.format(nome))
        os.remove('{}.txt'.format(nome))
        sleep(1)
    else:
        print('Jogador {} não existe no banco de dados.'.format(nome))
        sleep(1)


# função para consultar pontuação
def verificapontuacao():
    nome = input('Digite o nome do jogador: ')
    print()
    if os.path.isfile('{}.txt'.format(nome)):
        print('Pontuação do jogador {}: '.format(nome))
        f = open('{}.txt'.format(nome))
        historico = f.readlines()
        vitorias = historico[0]
        derrotas = historico[1] 
        print('Vitorias:\n{}\nDerrotas:\n{}'.format(vitorias, derrotas))
        sleep(1)
    else:
        print('Jogador {} não existe.'.format(nome))
        sleep(1)


# função para atualizar o tabuleiro
def atualizatabuleiro():
    tabuleiro = '''
     Colunas:       0 | 1 | 2 | 3 | 4 
      Linhas: 0 |   {} | {} | {} | {} | {}
              --+  ---+---+---+---+---
              1 |   {} | {} | {} | {} | {}
              --+  ---+---+---+---+---
              2 |   {} | {} | {} | {} | {}
              --+  ---+---+---+---+---
              3 |   {} | {} | {} | {} | {}
              --+  ---+---+---+---+---
              4 |   {} | {} | {} | {} | {}
    '''.format(matriz[0][0], matriz[0][1], matriz[0][2], matriz[0][3], matriz[0][4],
               matriz[1][0], matriz[1][1], matriz[1][2], matriz[1][3], matriz[1][4],
               matriz[2][0], matriz[2][1], matriz[2][2], matriz[2][3], matriz[2][4],
               matriz[3][0], matriz[3][1], matriz[3][2], matriz[3][3], matriz[3][4],
               matriz[4][0], matriz[4][1], matriz[4][2], matriz[4][3], matriz[4][4], )
    print(tabuleiro)


# função para verificar o vencedor
def verificavencedor():
    jogador = ['X', 'O']
    global vencedor
    # verifica se houve vitória por linha
    for i in jogador:
        linha = 0
        while linha < 5:
            soma = 0
            coluna = 0

            # verifica qual o valor de i
            if i == 'X':
                jogador_oposto = 'O'
            elif i == 'O':
                jogador_oposto = 'X'

            while coluna < 5:
                if matriz[linha][coluna] == i:
                    soma += 1
                elif matriz[linha][coluna] == jogador_oposto:
                    soma = 0
                if soma == 4:
                    vencedor = i
                    print('O jogador {} é o vencedor'.format(vencedor))
                    return vencedor
                coluna += 1   
            linha += 1
            

    # verifica se houve vitória por coluna
    for i in jogador:
        coluna = 0

        # verifica qual o valor de i
        if i == 'X':
            jogador_oposto = 'O'
        elif i == 'O':
            jogador_oposto = 'X'

        while coluna < 5:
            soma = 0
            linha = 0
            while linha < 5:
                if matriz[linha][coluna] == i:
                    soma += 1
                elif matriz[linha][coluna] == jogador_oposto:
                    soma = 0
                if soma == 4:
                    vencedor = i
                    print('O jogador {} é o vencedor'.format(i))
                    return vencedor
                linha += 1
            coluna += 1


    # verifica se houve vitória por diagonais

    # verifica se houve vitória por diagonal1
    for i in jogador:
        soma = 0

        # verifica qual o valor de i
        if i == 'X':
            jogador_oposto = 'O'
        elif i == 'O':
            jogador_oposto = 'X'

        for ind_diag in range(5):
            if matriz[ind_diag][ind_diag] == i:
                soma += 1
            elif matriz[ind_diag][ind_diag] == jogador_oposto:
                soma = 0
            if soma == 4:
                vencedor = i
                print('O jogador {} é o vencedor'.format(i))
                return vencedor


    # verifica se houve vitória por diagonal2
    for i in jogador:
        soma = 0
        ind_diag_linha = 0
        ind_diag_coluna = 4

        # verifica qual o valor de i
        if i == 'X':
            jogador_oposto = 'O'
        elif i == 'O':
            jogador_oposto = 'X'

        for ind_diag in range(5):
            if matriz[ind_diag_linha][ind_diag_coluna] == i:
                soma += 1
            elif matriz[ind_diag_linha][ind_diag_coluna] == jogador_oposto:
                soma = 0
            if soma == 4:
                vencedor = i
                print('O jogador {} é o vencedor'.format(vencedor))
                return vencedor
            ind_diag_linha += 1
            ind_diag_coluna -= 1


    # verifica se houve vitória por diagonal3
    for i in jogador:
        soma = 0
        ind_diag_linha = 0
        ind_diag_coluna = 3

        # verifica qual o valor de i
        if i == 'X':
            jogador_oposto = 'O'
        elif i == 'O':
            jogador_oposto = 'X'

        for ind_diag in range(4):
            if matriz[ind_diag_linha][ind_diag_coluna] == i:
                soma += 1
            elif matriz[ind_diag_linha][ind_diag_coluna] == jogador_oposto:
                soma = 0
            if soma == 4:
                vencedor = i
                print('O jogador {} é o vencedor'.format(vencedor))
                return vencedor
            ind_diag_linha += 1
            ind_diag_coluna -= 1


    # verifica se houve vitória por diagonal4
    for i in jogador:
        soma = 0
        ind_diag_linha = 1
        ind_diag_coluna = 4

        # verifica qual o valor de i
        if i == 'X':
            jogador_oposto = 'O'
        elif i == 'O':
            jogador_oposto = 'X'

        for ind_diag in range(4):
            if matriz[ind_diag_linha][ind_diag_coluna] == i:
                soma += 1
            elif matriz[ind_diag_linha][ind_diag_coluna] == jogador_oposto:
                soma = 0
            if soma == 4:
                vencedor = i
                print('O jogador {} é o vencedor'.format(vencedor))
                return vencedor
            ind_diag_linha += 1
            ind_diag_coluna -= 1


    # verifica se houve vitória por diagonal5
    for i in jogador:
        soma = 0
        ind_diag_linha = 0
        ind_diag_coluna = 1

        # verifica qual o valor de i
        if i == 'X':
            jogador_oposto = 'O'
        elif i == 'O':
            jogador_oposto = 'X'

        for ind_diag in range(4):
            if matriz[ind_diag_linha][ind_diag_coluna] == i:
                soma += 1
            elif matriz[ind_diag_linha][ind_diag_coluna] == jogador_oposto:
                soma = 0    
            if soma == 4:
                vencedor = i
                print('O jogador {} é o vencedor'.format(vencedor))
                return vencedor
            ind_diag_linha += 1
            ind_diag_coluna += 1        


    # verifica se houve vitória por diagonal6
    for i in jogador:
        soma = 0
        ind_diag_linha = 1
        ind_diag_coluna = 0

        # verifica qual o valor de i
        if i == 'X':
            jogador_oposto = 'O'
        elif i == 'O':
            jogador_oposto = 'X'

        for ind_diag in range(4):
            if matriz[ind_diag_linha][ind_diag_coluna] == i:
                soma += 1
            elif matriz[ind_diag_linha][ind_diag_coluna] == jogador_oposto:
                soma = 0
            if soma == 4:
                vencedor = i
                print('O jogador {} é o vencedor'.format(vencedor))
                return vencedor
            ind_diag_linha += 1
            ind_diag_coluna += 1
    return vencedor


# função para iniciar o jogo
def jogar():
    atualizatabuleiro()
    global vencedor
    global perdedor
    contador = 0
    Jogador_1 = input('Jogador 1 (X): ')
    Jogador_2 = input('Jogador 2 (O): ')
    print()

    # verifica se os jogadores estão no banco de dados
    if os.path.isfile('{}.txt'.format(Jogador_1)) and os.path.isfile('{}.txt'.format(Jogador_2)) :

        # loop do jogo com condição de empate e vencedor
        while contador < 25 or vencedor == ' ':
            if contador % 2 == 0:
                jogador = Jogador_1
            elif contador % 2 != 0:
                jogador = Jogador_2
            linha = int(input('>> {} <<\n\nLinha: '.format(jogador)))
            coluna = int(input('Coluna: '))
            print('Vencedor: ', vencedor)

            if (linha >= 0 or coluna >= 0) and (linha < 5 or coluna < 5): 
                # verifica se a coordenada esta vazia
                if matriz[linha][coluna] == ' ':
                    if contador % 2 == 0:
                        matriz[linha][coluna] = 'X'
                        atualizatabuleiro()
                        contador += 1
                        verificavencedor()

                    elif contador % 2 != 0:
                        matriz[linha][coluna] = 'O'
                        atualizatabuleiro()
                        contador += 1
                        verificavencedor()
                else:
                    print('Coordenada ocupada!')
                    print('Por favor escolha outra coordenada.')

                # verifica quem é o vencedor
                if vencedor != ' ':
                    if vencedor == 'X':
                        vencedor = Jogador_1
                        perdedor = Jogador_2
                    elif vencedor == 'O':
                        vencedor = Jogador_2
                        perdedor = Jogador_1
                    print('Vencedor: ', vencedor)

                    # atualização de registro do vencedor
                    f = open('{}.txt'.format(vencedor))
                    historico = f.readlines()
                    vitorias = int(historico[0])
                    derrotas = int(historico[1])
                    vitorias +=1
                    f.close()
                    file = open('{}.txt'.format(vencedor), 'w')
                    file.write('{}\n'.format(str(vitorias)))
                    file.write('{}\n'.format(str(derrotas)))
                    file.close()

                    # atualização do registro do perdedor
                    f = open('{}.txt'.format(perdedor))
                    historico = f.readlines()
                    vitorias = int(historico[0])
                    derrotas = int(historico[1])
                    derrotas +=1
                    f.close()
                    file = open('{}.txt'.format(perdedor), 'w')
                    file.write('{}\n'.format(str(vitorias)))
                    file.write('{}\n'.format(str(derrotas)))
                    file.close() 


                    reset()
                    break
                # condição de existencia para coordenadas
            else:
                print('Coordenada inexistente...\n')
                linha = int(input('>> {} <<\n\nLinha: '.format(jogador)))
                coluna = int(input('Coluna: '))
            print()
        else:
            print('Empate!')
    else:
        print('Algum jogador não consta no banco de dados, favor verificar...')
        