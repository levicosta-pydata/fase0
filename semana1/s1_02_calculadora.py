#   --- S1.02: Calculadora de IMC e conversor °C <-> °F ---

"""
    --- Parte 1: Calculadora do Índice de Massa Corporal (IMC) ---

    Invariante: Não se aplica, pois o código não possui estrutura repetitiva.
    Previsão: Calcular o IMC de acordo com peso e altura aplicadas à fórmula e classificar o paciente pelo resultado.
    Custo: O(1), com operações fixas entre 13 a 17 dependendo do IMC dado.
"""
peso = float(input("Seu peso (em kg): "))       # Peso em quilogramas
altura = float(input("Sua altura (em m): "))    # altura em metros
imc = peso / altura ** 2                        # IMC

print(f"\nIMC: {imc:.1f} kg/m²")
print("Status: ", end="")

if imc >= 40.0: print("Obesidade grau III")
elif imc >= 35.0: print("Obesidade grau II")
elif imc >= 30.0: print("Obesidade grau I")
elif imc >= 25.0: print("Sobrepeso")
elif imc >= 18.5: print("Adequado")
else: print("Baixo peso")
# ---------------------------------------------------------------------------------------------------------------------
"""
    --- Parte 2: Conversor de temperatura (°C <-> °F) ---

    Invariante: Não se aplica, pois o código não possui estrutura repetitiva.
    Previsão: Converter temperaturas entre celsius e fahrenheit.
    Custo: O(1), com operações fixas entre 15 e 16 dependendo da conversão escolhida.
"""
def c_f():
    global c, f
    c = float(input("Temperatura dada (em °C): "))    # Graus celsius
    f = 9/5 * c + 32                                  # Graus fahrenheit
    return f
def f_c():
    global c, f
    f = float(input("Temperatura dada (em °F): "))    # Graus fahrenheit
    c = 5/9 * (f - 32)                                # Graus celsius
    return c

escolha = int(input("\nConversor de temperatura:\n1: °C -> °F\n2: °F -> °C\nDígito: "))
match escolha:
    case 1: c_f(); print(f"\n{c:.1f} °C equivale a {f:.1f} °F")
    case 2: f_c(); print(f"\n{f:.1f} °F equivale a {c:.1f} °C")
