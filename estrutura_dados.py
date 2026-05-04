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
        self.cabeca = self._quick_sort_recursivo(self.cabeca)

    def _quick_sort_recursivo(self, c):
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
            while temp.proximo:
                temp = temp.proximo
            temp.proximo = pivo

        pivo.proximo = maiores

        return nova_cabeca

    def counting_sort(self):
        if not self.cabeca:
            return

        max_valor = self.cabeca.valor
        atual = self.cabeca
        while atual:
            if atual.valor > max_valor:
                max_valor = atual.valor
            atual = atual.proximo

        contagem = [0] * (max_valor + 1)

        atual = self.cabeca
        while atual:
            contagem[atual.valor] += 1
            atual = atual.proximo

        atual = self.cabeca
        for numero in range(len(contagem)):
            while contagem[numero] > 0:
                atual.valor = numero
                contagem[numero] -= 1
                atual = atual.proximo

    def radix_sort(self):
        if not self.cabeca:
            return

        max_valor = self.cabeca.valor
        atual = self.cabeca
        while atual:
            if atual.valor > max_valor:
                max_valor = atual.valor
            atual = atual.proximo

            exp = 1
            while max_valor // exp > 0:
                self.counting_sort_para_radix(exp)
                exp *= 10

    def _counting_sort_para_radix(self, exp):
        baldes = [Lista() for _ in range(10)]

        atual = self.cabeca
        while atual:
            digito = (atual.valor // exp) % 10
            baldes[digito].adicionar(atual.valor)
            atual = atual.proximo

        nova_cabeca = None
        ultimo = None

        for balde in baldes:
            if balde.cabeca:
                if not nova_cabeca:
                    nova_cabeca = balde.cabeca
                else:
                    ultimo.proximo = balde.cabeca

                temp = balde.cabeca
                while temp.proximo:
                    temp = temp.proximo
                ultimo = temp

        self.cabeca = nova_cabeca
