import random
numero_secreto = random.randint(1,100)
tentativas = 0
max_tentativas = 7
print("............Jogo da Adivinhação............")
print()
print(".......Adivinhe o número de 1 a 100!.......")
print("..........Você tem",max_tentativas,"tentativas!...........")

print()

while tentativas < max_tentativas:
  palpite = int(input("Digite seu palpite:"))
  print()
  tentativas += 1
  if 1 > palpite or palpite > 100:
    tentativas -= 1
   print("Número inválido, o número deve ser de 1 a 100. As tentativas restantes não foram alteradas.")
  elif palpite == numero_secreto:
    print("Parabéns, você acertou em apenas",tentativas,"tentativa(s)!")
    break
  elif palpite < numero_secreto:
    print("O número secreto é maior! Restam",max_tentativas - tentativas,"tentativas.")
  else:
    print("O número secreto é menor! Restam",max_tentativas - tentativas,"tentativas.")
  if tentativas == max_tentativas and palpite != numero_secreto:
    print("Fim de jogo!")
    print("O número era",numero_secreto)
    print("Obrigado por jogar!")
  print()
