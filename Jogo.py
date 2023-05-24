import time
import random
print('Bem-vindos aos Zombie Dice!')
time.sleep(0)
print('Hoje vamos comer muitos CÉREBROS!!!')
time.sleep(0)
qtdjog = int(input('Quantos jogadores irão participar? '))
jogadores = []
for cont in range(0, qtdjog):
    jogadores.append(str(input('Digite o nome do jogador: ')))
print('O jogador {} gritou como um zumbi legítimo e irá iniciar o jogo.'.format(jogadores[random.randint(0, 4)]))
print(jogadores[0])
print(jogadores[1])
print(jogadores[2])
print(jogadores[3])
