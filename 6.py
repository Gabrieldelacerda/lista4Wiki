def calcular_medias_e_contar_aprovados():
    medias = []

    for aluno in range(1, 11):
        print(f"\nAluno {aluno}:")
        notas = []
        for i in range(1, 5):
            nota = float(input(f"Digite a {i}ª nota: "))
            notas.append(nota)

        media_aluno = sum(notas) / len(notas)
        medias.append(media_aluno)

    aprovados = sum(1 for media in medias if media >= 7.0)

    print("\nNúmero de alunos com média maior ou igual a 7.0:", aprovados)

calcular_medias_e_contar_aprovados()
