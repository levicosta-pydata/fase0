#   --- S1.05: Separação dos algarismos de um inteiro positivo de três dígitos (usando % e //) ---
"""
    Invariante: Um n inteiro positivo é válido quando pertence ao intervalo [100, 999], possuindo
                três dígitos. Já quando n está fora do intervalo, uma nova entrada é solicitada até
                que o n atenda à condição falsa posta no looping while.
    Previsão: Através da aquisição de quocientes e restos pela divisão inteira (//) e aritmética
              modular (%), respectivamente, o código imprime, em ordem, os três algarismos de um
              inteiro positivo são impressos em ordem.
    Custo: Θ(k+1), com número de variando conforme dado k o número de execuções da entrada dentro do 
           while, temos T(k) = 6k + 14 o número de operações totais.
           Θ(1) quando k = 0, resultando num custo fixo T(0) = 14.
"""
n = int(input("Digite um número inteiro positivo de três dígitos: "))
while n < 100 or n >= 1000:
    n = int(input("Entrada inválida. Por favor, tente novamente: "))

a = n // 100
b = (n // 10) % 10
c = n % 10

print(f"\n1º dígito: {a}\n2º dígito: {b}\n3º dígito: {c}")