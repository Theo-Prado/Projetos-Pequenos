import random
nomes_masculinos = ["Theo","Pedro","Paulo","Francisco","Leonard","Georgie","Henry"]
nomes_femininos = ["Ada","Maria","Ester","Mandy","Paige","Grace","Penny"]
sobrenomes = ["Prado","Silva","Potter","Skywalker","Hofstadter","Cooper"]
adjetivo_masculino = ["Sábio","Corajoso","Especialista","Mago","Poderoso","Leal","Desbravador"]
adjetivo_feminino = ["Sábia","Corajosa","Especialista","Maga","Poderosa","Leal","Desbravadora"]
print("Criador de Nomes")
print()
while True:
  escolha1 = random.randint(0,6)
  escolha2 = random.randint(0,6)
  escolha3 = random.randint(0,6)
  print("[1] Criar nome masculino [2] Criar nome feminino [3] Sair")
  print()
  escolha4 = int(input("Digite sua escolha:"))
  print()
  if escolha4 == 3:
    break
    print("Obrigado por utilizar o programa!")

  elif escolha4 == 1:
    print("Seu nome é:", nomes_masculinos[escolha1],sobrenomes[escolha2],"o",adjetivo_masculino[escolha3])
    print()
  elif escolha4 == 2:
    print("Seu nome é:",nomes_femininos[escolha1],sobrenomes[escolha2],"a",adjetivo_feminino[escolha3])
    print()
  else:
    print("Erro: número inválido!")
    print()
