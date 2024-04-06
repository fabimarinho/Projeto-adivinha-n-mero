import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while  True:
    palpite = int(input("Adivinhe o número secreto (entre 1 e 100): "))
    tentativas  += 1

    if palpite == numero_secreto:
        print("-"*60)
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("Seu palpite é muito baixo! Tente novamente.")
    else:
        print("Seu palpite é muito alto! Tente novamente.")
