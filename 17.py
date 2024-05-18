while True:
    nome = input("Atleta: ")
    if not nome:
        break

    saltos = []
    for i in range(5):
        salto = float(input(f"{i + 1}º Salto: "))
        saltos.append(salto)

    media_saltos = sum(saltos) / 5

    print(f"\nResultado final:")
    print(f"Atleta: {nome}")
    print(f"Saltos: {' - '.join(map(str, saltos))}")
    print(f"Média dos saltos: {media_saltos:.1f} m\n")
