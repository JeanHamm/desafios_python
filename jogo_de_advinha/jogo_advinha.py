import random
from write_hello import well_write

well_write('Bem vindo')

jogo = True
while(jogo == True):
    secret_number = random.randrange(1, 11)
    for i in range(0,3):
        
        number = int(input('Choice a number '))
        while(number < 0 or number > 10):
            number = int(input('Choice another number between 0 and 10 '))

        if(number == secret_number):
            print('você acertou')
            break
        else:
            print('Você errou!')

    status = int(input('\n\nQuer jogar novamente?\ndigite 1 se sim e 2 se não : '))
    if(status == 1):
        jogo == False
    else:
        print('\nFim de jogo!')
