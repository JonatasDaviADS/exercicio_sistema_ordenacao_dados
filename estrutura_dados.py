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
        

    def _get_meio(self, cabeca):
        if not cabeca:
            return cabeca

        lento = cabeca
        rapido = cabeca 

        while rapido.proximo and rapido.proximo.proximo:
            lento = lento.proximo 
            rapido = rapido.proximo.proximo

        return lento      
    
    def _mesclar (self, esquerda, direita):

        if not esquerda: 
            return direita 
        if not direita: 
            return esquerda
        
        if esquerda.valor <= direita.valor: 
            resultado = esquerda
            resultado.proximo = self._mesclar(esquerda.proximo, direita)

        else: 
            resultado = direita 
            resultado.proximo = self._mesclar(esquerda, direita.proximo)

            return resultado