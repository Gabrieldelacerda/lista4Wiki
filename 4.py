def contar_e_imprimir_consoantes():
    caracteres = []

    print("Digite 10 caracteres:")
    for i in range(10):
        caractere = input(f"Digite o {i+1}º caractere: ")
        caracteres.append(caractere)

    consoantes = "bcdfghjklmnpqrstvwxyz"

    contador_consoantes = 0

    consoantes_encontradas = []

    for caractere in caracteres:
        if caractere.lower() in consoantes:
            contador_consoantes += 1
            consoantes_encontradas.append(caractere)

    print(f"\nForam encontradas {contador_consoantes} consoantes.")
    if contador_consoantes > 0:
        print("Consoantes encontradas:")
        print(" ".join(consoantes_encontradas))
    else:
        print("Nenhuma consoante foi encontrada.")

contar_e_imprimir_consoantes()
