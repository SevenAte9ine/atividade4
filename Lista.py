from No import No

class Lista:
  def __init__(self):
    self.inicio = None

  def inserir(self,data):
    if self.inicio is None:
      novo = No(data)
      self.inicio = novo
      return
    n = self.inicio
    while n.proximo is not None:
      n = n.proximo
    novo = No(data)
    n.proximo = novo
    novo.anterior = n

  def imprimir(self):
    if self.inicio is None:
      print("Lista não possui elementos.")
      return
    else:
      n = self.inicio
      while n is not None:
        print(n.item , " ")
        n = n.proximo

  def excluir(self, x):
      if self.inicio is None:
          print("Esta lista não possui elementos para excluir")
          return 
      if self.inicio.proximo is None:
          if self.inicio.item == x:
              self.inicio = None
          else:
              print("Item not found")
          return 

      if self.inicio.item == x:
          self.inicio = self.inicio.proximo
          self.inicio.anterior = None
          return

      n = self.inicio
      while n.proximo is not None:
          if n.item == x:
              break;
          n = n.proximo
      if n.proximo is not None:
          n.anterior.proximo = n.proximo
          n.proximo.anterior = n.anterior
      else:
          if n.item == x:
              n.anterior.proximo = None
          else:
              print("Elemento não encontrado.")

  def reverter(self):
      rever = None
      atual = self.inicio
 
      while atual is not None:
          rever = atual.anterior
          atual.anterior = atual.proximo
          atual.proximo = rever
          atual = atual.anterior
 
      if rever is not None:
          self.inicio = rever.anterior
