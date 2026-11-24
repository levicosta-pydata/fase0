#   --- S1.02: Calculadora de IMC e conversor °C <-> °F ---

"""
    --- Parte 1: Calculadora do Índice de Massa Corporal (IMC) ---

    Invariante: imc = peso/(altura)², tal que peso >= 0 e altura > 0, logo imc >= 0.
    Previsão: Calcular o IMC de acordo com peso e altura aplicadas à fórmula e classificar o paciente pelo resultado.
    Custo: O(1), com operações fixas entre 13 a 17 dependendo do IMC dado.
"""
peso = float(input("Seu peso (em kg): "))
altura = float(input("Sua altura (em m): "))
imc = peso / altura ** 2

print(f"\nIMC: {imc:.1f} kg/m²")
print("Status: ", end="")

if imc > 40.0: print("Obesidade grau III")
elif imc >= 35.0: print("Obesidade grau II")
elif imc >= 30.0: print("Obesidade grau I")
elif imc >= 25.0: print("Sobrepeso")
elif imc >= 18.5: print("Adequado")
else: print("Baixo peso")
# ---------------------------------------------------------------------------------------------------------------------
