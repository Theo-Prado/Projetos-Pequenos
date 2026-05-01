def soma(a,b): return a + b
def subtrai(a,b): return a - b
def multiplica(a,b): return a * b
def potencia(a): return a * a
def divide(a,b):
  if b != 0:
    return a / b
  return "Erro: divisão por zero!"

print("Calculadora")
print()

while True:
  print("\n [1] Soma [2] Subtrai [3] Multiplica [4] Divide [5] Potencia [6] Sair")
  print()
  opcao = int(input("Escolha:"))
  print()
  if opcao == 6:
    print("Obrigado por utilizar a calculadora!")
    break
  elif opcao == 5:
    n = float(input("Número:"))
    print()
    print(potencia(n))
    print()
  elif opcao > 0 and opcao < 5:
    n1 = float(input("1º Número:"))
    n2 = float(input("2º Número:"))
    print()
    if opcao == 1:
      print(soma(n1,n2))
      print()
    elif opcao == 2:
      print(subtrai(n1,n2))
      print()
    elif opcao == 3:
      print(multiplica(n1,n2))
      print()
    elif opcao == 4:
      print(divide(n1,n2))
      print()
  else:
    print("Erro: número invalido!")
    print()
