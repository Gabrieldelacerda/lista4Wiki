def separar_pares_impares():
    numeros = []
    pares = []
    impares = []

    print("Digite 20 números inteiros:")
    for i in range(20):
        numero = int(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    print("\nNúmeros inseridos:")
    print(numeros)
    print("\nNúmeros pares:")
    print(pares)
    print("\nNúmeros ímpares:")
    print(impares)

separar_pares_impares()
