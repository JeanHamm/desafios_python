import random
#Bem vindo
def well_come(mensagem):
    print('-------------------')
    print(mensagem)
    print('-------------------')

#Escolhendo palavra secreta
def escolhendo_palavra_secreta():
    secret_word = ['Jaca', 'Banana', 'Maça', 'Uva']
    secret_word_number = random.randrange(0, len(secret_word))
    return secret_word[secret_word_number]

#gerador da palavra escondida
def gerando_o_quadro(secret_word):
    word_now = []
    for letra in secret_word:
        word_now.append('_')
    return word_now

def resultado_final(secret_word, erros, acertos):
    if(erros == 3):
        print(f'\n Você perdeu! a palavra secreta era {secret_word.capitalize()}\n')
    elif(acertos == len(secret_word)):
        print(f'\n Você ganhou! a palavra secreta era {secret_word.capitalize()}\n')
def corpo_do_jogo(secret_word, word_now):
    chance = False
    acerto = False
    erros = 0
    acertos = 0
    while(chance == False and acerto == False):
    #recebe o chute
        print(word_now)
        kick = input('Qual o seu chute?: ')

    #verifica o chute
        contador = 0
        mudanca = False
        for letra in secret_word:
            if(kick.capitalize() == letra.capitalize()):
                word_now[contador] = kick.capitalize()
                mudanca = True
                acertos += 1
            contador += 1
        
    #verificação de while
        if(mudanca == False):
            erros += 1
        if(erros == 3):
            chance = True
            print(word_now)
        elif(acertos == len(secret_word)):
            acerto =True
            print(word_now)

    resultado_final(secret_word, erros, acertos)

well_come('Jogo da forca!')
secret_word = escolhendo_palavra_secreta()

word_now = gerando_o_quadro(secret_word)

corpo_do_jogo(secret_word, word_now)
    
