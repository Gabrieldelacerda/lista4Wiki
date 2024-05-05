def calcular_soma_quadrados(vetor):
    soma_quadrados = 0

    for numero in vetor:
        soma_quadrados += numero ** 2

    print("A soma dos quadrados dos elementos de vetor é:", soma_quadrados)

vetor = []
print("Digite os 10 números inteiros:")
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

calcular_soma_quadrados(vetor)
