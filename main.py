from estrutura_dados import Lista

print("--- Sistema de Processamento de Dados ---")
meu_sistema = Lista()

meu_sistema.adicionar(45)
meu_sistema.adicionar(12)
meu_sistema.adicionar(8)
meu_sistema.adicionar(99)


print("Olhando o estado atual da Lista")
meu_sistema.exibir()


print("\nOrdenando com Merge Sort.")
meu_sistema.merge_sort()

print("Resultado final:")
meu_sistema.exibir()
