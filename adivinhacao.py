from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Pensei em um numero entre 0 e 5, Adivinhe qual é: ')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
sleep(2)
if jogador == computador:
    print('ACERTOU')
else:
    print('PERDEU')
    
print(f'O numero era {computador}')