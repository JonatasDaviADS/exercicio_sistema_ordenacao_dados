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

    def _mesclar(self, esquerda, direita):

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

    def merge_sort(self):
        self.cabeca = self.merge_sort_recursivo(self.cabeca)

    def _merge_sort_recursivo(self, c):
        if c is None or c.proximo is None:
            return c

        meio = self._get_meio(c)
        proximo_do_meio = meio.proximo

        meio.proximo = None

        esquerda = self._merge_sort_recursivo(c)
        direita = self._merge_sort_recursivo(proximo_do_meio)

        lista_ordenada = self._mesclar(esquerda, direita)
        return lista_ordenada

    def quick_sort(self):
        self.cabeca = self._quick_sort_recursivo (self.cabeca)

    def _quick_sort_recursivo (self, c):
        if not c or not c.proximo:
            return c

        pivo = c 
        menores_cabeca = None 
        maiores_cabeca = None 

        atual = c.proximo
        pivo.proximo = None 

        while atual:
            proximo_nodo = atual.proximo 

            if atual.valor < pivo.valor:
                atual.proximo = menores_cabeca
                menores_cabeca = atual 

            else:
                atual.proximo = maiores_cabeca
                maiores_cabeca = atual 

            atual = proximo_nodo

        menores_ordenados = self._quick_sort_recursivo(menores_cabeca)
        maiores_ordenados = self._quick_sort_recursivo(maiores_cabeca) 

        return self._conectar(menores_ordenados, pivo, maiores_ordenados)
    
    def _conectar(self, menores, pivo, maiores):
        nova_cabeca = menores if menores else pivo 

        if menores: 
            temp = menores
            while tem.proximo:
                temp = temp.proximo 
            temp.proximo = pivo

        pivo.proximo = maiores 

        return nova_cabeca



