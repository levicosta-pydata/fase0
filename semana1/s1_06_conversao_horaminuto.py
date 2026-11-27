#   --- S1.06: Conversor de minutos totais de filme para h:min ---

"""
    Invariante: A variável min que guarda a quantidade de minutos totais sempre deve ser maior
                ou igual a zero, pelo contrário ela permanecerá no while até que atenda o pré-
                -requisito dado.
    Previsão: Converter o número inteiro positivo de minutos totais de um filme para o
              padrão hora-minuto.
    Custo: Θ(k+1), com número de variando conforme dado k o número de execuções da entrada dentro do 
           while, temos T(k) = 4k + 9 o número de operações totais.
           Θ(1) quando k = 0, resultando num custo fixo T(0) = 9.
"""
min = int(input("Insira o número de minutos totais do filme: "))
while min < 0:
    min = int(input("Entrada inválida. Por favor, tente novamente: "))

hora = min // 60
min %= 60

print(f"Tempo (h:min) do filme: {hora}h {min}min")