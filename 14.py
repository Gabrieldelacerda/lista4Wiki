perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []

for pergunta in perguntas:
    resposta = input(f"{pergunta} (sim/não): ").lower()
    if resposta == 'sim':
        respostas.append(True)
    else:
        respostas.append(False)

numero_de_respostas_positivas = sum(respostas)

if numero_de_respostas_positivas == 2:
    print("Suspeita")
elif 3 <= numero_de_respostas_positivas <= 4:
    print("Cúmplice")
elif numero_de_respostas_positivas == 5:
    print("Assassino")
else:
    print("Inocente")
