with open("usuarios.txt", "r") as arquivo:
    usuarios = arquivo.readlines()

espacos = [int(usuario.strip().split()[1]) for usuario in usuarios]
total_espaco = sum(espacos)
espaco_medio = total_espaco / len(usuarios)

with open("relatorio.txt", "w") as relatorio:
    relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
    relatorio.write("------------------------------------------------------------------------\n")
    relatorio.write("Nr.  Usuário        Espaço utilizado     % do uso\n")

    for i, usuario in enumerate(usuarios, start=1):
        nome, espaco = usuario.strip().split()
        espaco_utilizado = int(espaco) / (1024 ** 2)
        percentual = (int(espaco) / total_espaco) * 100
        relatorio.write(f"{i:<4} {nome:<15} {espaco_utilizado:>10.2f} MB {percentual:>20.2f}%\n")

    relatorio.write("\nEspaço total ocupado: {:.2f} MB\n".format(total_espaco / (1024 ** 2)))
    relatorio.write("Espaço médio ocupado: {:.2f} MB".format(espaco_medio / (1024 ** 2)))
