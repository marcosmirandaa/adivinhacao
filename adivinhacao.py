import random

palpite = 0
secreto = random.randint(1, 100)
tentativas = 0

while palpite != secreto and tentativas < 7:
    try:
        palpite = int(input('Diga seu palpite: '))
    except ValueError:
        print ('Isto não é um número!')
        continue
    tentativas += 1

    if palpite < secreto:
        print('É mais que isto!')
    elif palpite > secreto:
        print('É menos que isso')
    else:
        print('Acertou!')
    if palpite!= secreto:
        diferenca = abs (palpite - secreto)
        if diferenca <= 5:
            print ('Quente')
        elif diferenca <= 15:
            print ('Morno')
        else: 
            print ('Frio')

if palpite == secreto:
    print('Você acertou em', tentativas, 'tentativas')
else:
    print('Você não acertou e acabaram suas tentativas!')
    print(f'O número secreto era: {secreto}')
    