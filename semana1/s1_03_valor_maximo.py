#   --- S1.03: Valor máximo dentre três números (sem função 'max') ---

"""
    Invariante: Não se aplica, pois o código não possui estrutura repetitiva.
    Previsão: Dados três números reais quaisquer, obteremos o maior dentre eles.
    Custo: O(1), com número de execuções fixas entre 14 a 16 dependendo das aprovações condicionais.
"""
a = float(input("Digite o 1º número: "))
b = float(input("Digite o 2º número: "))
c = float(input("Digite o 3º número: "))

maior = a

if b >= maior:
    maior = b
if c >= maior:
    maior = c

print(f"\nValor máximo: {maior}")