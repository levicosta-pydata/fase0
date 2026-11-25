#   --- S1.04: Troca de duas variáveis, sem e com vaariável auxiliar ---

"""
    --- Parte 1: Sem variável auxiliar (Uso das operações de soma e subtração) ---

    Invariante: Não se aplica, pois o código não possui estrutura repetitiva.
    Previsão: Realizar a troca do par de inteiros (a, b) ---> (b, a) SEM variável auxiliar.
    Custo:
""" 
a = int(input("Digite o 1º número inteiro (a): "))    # Variável a
b = int(input("Digite o 2º número inteiro (b): "))    # Variável b

print(f"\nPar inicial: (a, b) = ({a}, {b})")

a = a + b    # (a, b) ---> (a+b, b)
b = a - b    # (a+b, b) ---> (a+b, a)    (a, b) ---> (b, a)
a = a - b    # (a+b, b) ---> (b, a)

print(f"Par final: (a, b) = ({a}, {b})")
