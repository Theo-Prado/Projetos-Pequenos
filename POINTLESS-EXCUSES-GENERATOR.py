import random

nomes = ["O meu cachorro", "A minha gata", "O filho da vizinha","Meu primo"]
verbos = ["comeu o", "destruiu o", "roubou o","ateou fogo no"]
coisas = ["meu dever de casa.","meu documento.", "meu compromisso.","meu trabalho."]

print("Gerador de Desculpas Fúteis")
print()

ciclo = True

while ciclo:
  print("1 - Gerar desculpa")
  print("2 - Sair")
  print()
  try:
    escolha = int(input("Digite sua escolha:"))
    print()
    if escolha == 1:
     aleatorio0 = random.randint(0,5)
     aleatorio1 = random.randint(0,3)
     aleatorio2 = random.randint(0,3)
     aleatorio3 = random.randint(0,3)
     aleatorio4 = random.randint(0,100)
     if aleatorio0 == 1:
      aleatorio5 = random.randint(0,2)
      if aleatorio5 == 0:
        print("Desculpa Especial 1/3: A Estrela da Morte destruiu meu carro, então não pude vir trabalhar.")
        print()
        print("Credibilidade: 100%")
        print()
        print("Resposta: Que a Força esteja com você!")
        print()
      elif aleatorio5 == 1:
        print("Desculpa Especial 2/3: O Super Homem jogou o ônibus que eu estava em um vilão, por isso me atrasei.")
        print()
        print("Credibilidade: 100%")
        print()
        print("Resposta: Por Verdade, Justiça e um Amanhã Melhor!")
        print()
      else:
        print("Desculpa Especial 3/3: Fui convocado para lutar contra Lorde Voldmort, vou ter que faltar alguns dias no trabalho.")
        print()
        print("Credibilidade: 100%")
        print()
        print("Resposta: É leviOsa, não levioSA!")
        print()
     else:
      print(nomes[aleatorio1], verbos[aleatorio2], coisas[aleatorio3])
      print()
      print(f"Credibilidade da desculpa de {aleatorio4}%")
      print()
      if aleatorio4 < 30:
       print("Resposta: Para de mentir!")
      elif aleatorio4 < 70:
       print("Resposta: Sei sei...")
      else:
       print("Resposta: Sério?! Eu sinto muito!")
      print()
    elif escolha == 2:
     ciclo = False
     print("Obrigado por usar o sistema!")
    else:
      print("Digito inválido.")
  except ValueError:
    print("Digito inválido.")
    print()
