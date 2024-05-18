import random

def lancamento_dados():
    return random.randint(1, 6)

resultados = [0, 0, 0, 0, 0, 0]

for _ in range(100):
    resultado = lancamento_dados()
    resultados[resultado - 1] += 1

print("Resultados dos lançamentos:")
for i in range(6):
    print(f"Número {i+1}: {resultados[i]} vezes")
