def ler_e_mostrar_vetor():
    vetor = []

    print("Digite 5 números inteiros:")
    for i in range(5):
        numero = int(input(f"Digite o {i+1}º número: "))
        vetor.append(numero)

    print("Os números digitados são:")
    for numero in vetor:
        print(numero)

ler_e_mostrar_vetor()
