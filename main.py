from Lista import Lista

l1 = Lista()
while True:
  escolha = input("""Escolha se deseja inserir ou deletar um valor na lista. Insira 1 para inserir , 2 para deletar, e 3 para imprimir a lista em ordem reversa.
  Insira aqui: """)
  if escolha == "1":
    l1.inserir(input( "Insira um valor: " ))
    print("-------------------------------")
    l1.imprimir()
    print("-------------------------------")
  if escolha == "2":
    l1.excluir(input("Escolha um valor para excluir: "))
    l1.imprimir()
    print("-------------------------------")
  if escolha == "3":
    l1.reverter()
    print("-------------------------------")
    l1.imprimir()
    print("-------------------------------")
