while True:

  def somar(x,y):
    return x+y

  def subtrair(x,y):
    return x-y

  def multiplicar(x,y):
    return x*y

  def dividir(x,y):
    return x/y
    
  
  n1 = float(input("Digite um número:\n"))
  n2 = float(input("Digite outro número:\n"))
  print("Digite o número 1 para soma")
  print("Digite o número 2 para subtração")
  print("Digite o número 3 para multiplicação")
  print("Digite o número 4 para divisão")
  print("Digite o número 5 para sair")
  op = input("Escolha a operação")

  if op =='1':
    print(f"O resultado é:\n{somar(n1,n2)}")

  elif op =='2':
    print(f"O resultado é:\n{subtrair(n1,n2)}")

  elif op =='3':
    print(f"O resultado é:\n{multiplicar(n1,n2)}")

  elif op =='4':
    print(f"O resultado é:\n{dividir(n1,n2)}")

  else:
    print("Encerrando")
    break