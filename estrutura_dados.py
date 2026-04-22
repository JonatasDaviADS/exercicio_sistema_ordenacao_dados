class Nodo:
    def __init__(self, valor):
        self.valor = valor 
        self.proximo = None


class Lista: 
    def __init__(self):
        self.cabeca = None

    def adicionar(self, valor):
        novo_nodo = Nodo(valor)
        if not self.cabeca:
            self.cabeca = novo_nodo

        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def exibir(self, valor):
        atual = self.cabeca
        while atual: 
            print(atual.valor, end="->")
            atual = atual.proximo
        print("None")    
        