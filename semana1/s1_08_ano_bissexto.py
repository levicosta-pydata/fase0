#   --- S1.08: Identificação de ano bissexto ---

"""
    Invariante: A condição 'ano' >= 0 é necessária para a estrutura condicional ser
                executada. Caso contrário, será solicitada uma nova entrada para a
                variável.
    Previsão: Dado um inteiro 'ano' >= 0, o código retornará se o respectivo ano é
              bissexto ou não, baseando-se nas condições matemáticas relacionadas:
              (ano ≡ 0 (mod 4) ∧ ano ≢ 0 (mod 100)) ∨ (ano ≡ 0 (mod 4))
    Custo: Θ(N), dado N o nímero de entradas inválidas dentro do while, onde o total
           de operações do código é calculado pela fórmula T(N) = 4N + K, onde K per-
           tence a {7, 9, 12} a depender da estrutura condicional dada. Melhor caso
           ocorrido quando N = 0, resultando em T(0) = K constante.
"""
ano = int(input("Insira o ano referente: "))
while ano < 0:
    ano = int(input("Entrada inválida. Por favor, tente novamente: "))

if ano % 400 == 0:                           # 'ano' ≡ 0 (mod 4)
    print(f"\nO ano {ano} é bissexto.")
elif (ano % 4 == 0) and (ano % 100 != 0):    # 'ano' ≡ 0 (mod 4) ∧ 'ano' ≢ 0 (mod 100)
    print(f"\nO ano {ano} é bissexto.")
else:
    print(f"\nO ano {ano} não é bissexto.")
