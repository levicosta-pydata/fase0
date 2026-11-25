#   --- S1.04: Troca de duas variáveis, sem e com variável auxiliar ---

"""
    --- Parte 1: Sem variável auxiliar (Uso das operações de soma e subtração) ---

    Invariante: Não se aplica, pois o código não possui estrutura repetitiva.
    Previsão: Realizar a troca do par de inteiros (a, b) ---> (b, a) SEM variável auxiliar.
    Custo: O(1), com 14 operações fixas.
""" 
a = int(input("Digite o 1º número inteiro (a): "))    # Variável a
b = int(input("Digite o 2º número inteiro (b): "))    # Variável b

print(f"\nPar inicial: (a, b) = ({a}, {b})")

a = a + b    # (a, b) ---> (a+b, b)
b = a - b    # (a+b, b) ---> (a+b, a)
a = a - b    # (a+b, b) ---> (b, a)

print(f"Par final: (a, b) = ({a}, {b})")
# ---------------------------------------------------------------------------------------------------------------------
"""
    --- Parte 2: Com variável auxiliar ---

    Invariante: Não se aplica, pois o código não possui estrutura repetitiva.
    Previsão: Realizar a troca do par de inteiros (a, b) ---> (b, a) COM variável auxiliar.
    Custo: O(1), com 11 operações fixas.
"""
a = int(input("\nDigite o 1º número inteiro (a): "))    # Variável a
b = int(input("Digite o 2º número inteiro (b): "))      # Variável b

print(f"\nPar inicial: (a, b) = ({a}, {b})")

temp = a    # (a, b, temp) ---> (a, b, a)
a = b       # (a, b, a) ---> (b, b, a)
b = temp    # (b, b, a) ---> (b, temp, a), equivalente a (b, a, a)

print(f"Par final: (a, b) = ({a}, {b})")