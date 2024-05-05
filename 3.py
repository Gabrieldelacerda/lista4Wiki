def calcular_media_notas():
    notas = []

    print("Digite as 4 notas:")
    for i in range(4):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)

    media = sum(notas) / len(notas)

    print("\nNotas inseridas:")
    for i, nota in enumerate(notas):
        print(f"Nota {i+1}: {nota}")
    print(f"Média das notas: {media:.2f}")

calcular_media_notas()
