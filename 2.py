def ler_e_mostrar_inverso():
    vetor = []

    print("Digite 10 números reais:")
    for i in range(10):
        numero = float(input(f"Digite o {i+1} número: "))
        vetor.append(numero)

    print("Os números digitados, em ordem inversa, são:")
    for numero in reversed(vetor):
        print(numero)

ler_e_mostrar_inverso()
