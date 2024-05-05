def intercalar_vetores(vetor1, vetor2):
    vetor_intercalado = []

    for i in range(len(vetor1)):
        vetor_intercalado.append(vetor1[i])
        vetor_intercalado.append(vetor2[i])

    return vetor_intercalado

def ler_vetor():
    vetor = []
    print("Digite 10 números inteiros:")
    for i in range(10):
        num = int(input(f"Digite o {i+1}º número: "))
        vetor.append(num)
    return vetor

vetor1 = ler_vetor()
vetor2 = ler_vetor()

vetor_intercalado = intercalar_vetores(vetor1, vetor2)

print("\nVetor intercalado:", vetor_intercalado)
