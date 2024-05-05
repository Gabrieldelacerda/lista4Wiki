def contar_alunos_altura_inferior(idades, alturas):
    soma_alturas = 0
    contagem_alunos_13_anos = 0

    for idade, altura in zip(idades, alturas):
        if idade > 13:
            soma_alturas += altura
            contagem_alunos_13_anos += 1

    if contagem_alunos_13_anos > 0:
        media_alturas = soma_alturas / contagem_alunos_13_anos
    else:
        return 0

    contagem_alunos_altura_inferior = 0

    for idade, altura in zip(idades, alturas):
        if idade > 13 and altura < media_alturas:
            contagem_alunos_altura_inferior += 1

    return contagem_alunos_altura_inferior

idades = [14, 12, 13, 15, 16, 11, 14, 13, 14, 12, 15, 13, 14, 16, 13, 12, 14, 15, 13, 14, 13, 14, 15, 12, 16, 13, 14, 15, 13, 12]
alturas = [1.60, 1.55, 1.70, 1.62, 1.68, 1.50, 1.65, 1.58, 1.72, 1.53, 1.67, 1.61, 1.69, 1.75, 1.59, 1.52, 1.71, 1.66, 1.63, 1.68, 1.57, 1.73, 1.65, 1.56, 1.74, 1.60, 1.70, 1.64, 1.58, 1.55]

resultado = contar_alunos_altura_inferior(idades, alturas)

print(f"A quantidade de alunos com mais de 13 anos e altura inferior à média: {resultado}")
