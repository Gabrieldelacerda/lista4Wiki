def calcular_soma_multiplicacao(vetor):
    soma = sum(vetor)

    multiplicacao = 1
    for num in vetor:
        multiplicacao *= num

    print("Números inseridos:", vetor)
    print("Soma dos números:", soma)
    print("Multiplicação dos números:", multiplicacao)

vetor = []
print("Digite 5 números inteiros:")
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

calcular_soma_multiplicacao(vetor)
