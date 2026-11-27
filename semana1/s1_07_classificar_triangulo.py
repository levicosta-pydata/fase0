#   --- S1.07: Classificar um triângulo (equilátero, isósceles, escaleno, inexistente) ---

"""
    Invariante: 'a, b, c > 0', pois não há lado geométrico menor ou igual a zero. Atendida a
                condição, o código segue para a verificação da tupla (a, b, c).
    Previsão: Classificar a natureza do triângulo (a, b, c). Se uma das condições 'c < a + b',
              'b < a + c' ou 'a < b + c' não for atendida, o triângulo é inexistente.
    Custo: Θ(N), com o número variando conforme dado 'N = n_a + n_b + n_c' a soma de entradas
           inválidas, onde 'n_a' refere-se ao número de entradas inválidas da variável 'a', 
           'n_b' ao do 'b' e 'n_c' ao do 'c'. Além disso, seja T(N) = 4N + 12 + C, sendo C o
           número de operações que depende da análise de operações na tupla (a, b, c) válida
           tal que 3 <= C <= 17.
"""
 
a = int(input("Digite o valor do 1º lado (maior que zero): "))
while a <= 0:      a = int(input("Entrada inválida. Por favor, tente novamente: "))
b = int(input("Digite o valor do 2º lado (maior que zero): "))
while b <= 0:    b = int(input("Entrada inválida. Por favor, tente novamente: "))
c = int(input("Digite o valor do 3º lado (maior que zero): "))
while c <= 0:    c = int(input("Entrada inválida. Por favor, tente novamente: "))

if (a >= b + c) or (b >= a + c) or (c >= a + b):
    print(f"\nTriângulo ({a}, {b}, {c}): Inexistente.")
elif (a != b) and (b != c) and (a != c):
    print(f"\nTriângulo ({a}, {b}, {c}): Escaleno.")
elif (a == b) and (b == c):
    print(f"\nTriângulo ({a}, {b}, {c}): Equilátero.")
else:
    print(f"\nTriângulo ({a}, {b}, {c}): Isósceles.")