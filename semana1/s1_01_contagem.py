#   --- S1_01 - Contagens e tabuada ---

"""
    --- Parte 1: Imprimir de 1 a 20 ---
    
    Invariante: 1 <= i <= 21.
    Previsão: Imprime os números inteiros de 1 a 20.
    Custo: O(1), com 82 operações fixas.
"""
i = 1
while i <= 20:
    print(i, end=', ' if i < 20 else '\n')
    i += 1
# ---------------------------------------------------------------------------------------------------------------------
"""
    --- Parte 2: Imprimir os pares de 1 a 50 ---
    
    Invariante: 1 <= 2*i <= 52.
    Previsão: Imprime os números pares de 1 a 50.
    Custo: O(1), com 77 operações fixas.
"""
i = 1
while 2*i <= 50:
    print(2*i, end=', ' if 2*i < 50 else '\n')
    i += 1
