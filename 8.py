def ler_e_imprimir_inverso():
    idades = []
    alturas = []

    for i in range(5):
        idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
        altura = float(input(f"Digite a altura, em metros, da {i+1}ª pessoa: "))
        idades.append(idade)
        alturas.append(altura)

    print("\nIdades e alturas na ordem inversa:")
    for i in range(4, -1, -1):
        print(f"Idade: {idades[i]}, Altura: {alturas[i]} metros")

ler_e_imprimir_inverso()
