import random
class Jogador():
    def __init__(self, nome, jogada):
        self.nome = nome
        self.jogada = jogada
        self.jogada_nome = ''
        pass

    def __int__(self, jogada):
        return self.jogada
    def __eq__(self, jogada):
        return self.jogada
    def __str__(self, nome):
        return self.nome
    
    #faz o nome da jogada virar String
    def convertendo_jogada_em_nome(self):
        if(self.jogada == 1):
            self.jogada_nome = 'Pedra'
        elif(self.jogada == 2):
            self.jogada_nome = 'Papel'
        elif(self.jogada == 3):
            self.jogada_nome = 'Tesoura'
    
    #chama a jogada do player
    def jogada_da_vez(self):
        jogada = int(input('Escolha qual jogar:\n\n1 - Pedra\n2 - Papel\n3 - Tesoura\n\nQual sua escolha? : '))
        while(jogada < 1 or jogada > 3):
            jogada = int(input('Escolha novamente qual jogar:\n\n1 - Pedra\n2 - Papel\n3 - Tesoura\n\nQual sua escolha? : '))
        self.jogada = jogada
        self.convertendo_jogada_em_nome()
    
    #chama a jogada da maquina
    def jogada_da_maquina(self):
        jogada = random.randrange(1,4)
        self.jogada = jogada
        self.convertendo_jogada_em_nome()

#validador de quem ganhou
def validacao(player, computador):
    #pedra x papel
    if(player == 2 and computador == 1):
        return player
    elif(player ==1 and computador == 2):
        return computador
    #papel x tesoura
    elif(player == 3 and computador == 2):
        return player
    elif(player == 2 and computador == 3):
        return computador
    #tesoura x pedra
    elif(player == 1 and computador == 3):
        return player
    elif(player == 3 and computador == 1):
        return computador
    
def get_jogadas(player, computador):
    print(f'\nO {player.nome} jogou {player.jogada_nome}\n\nE o {computador.nome} jogou {computador.jogada_nome}')
    
def validacao_final(player, computador):
    ganhou = validacao(player, computador)
    if(ganhou == True):
        print(f'\n{ganhou.nome} ganhou!')
    else:
        print('Deu empate!')


player = Jogador('Jogador', 0)
computador = Jogador('Computador', 0)

player.jogada_da_vez()
computador.jogada_da_maquina()
get_jogadas(player, computador)

ganhador = validacao_final(player, computador)

print('')







        
    



    