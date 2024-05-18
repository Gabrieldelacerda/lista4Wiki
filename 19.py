def calcular_percentual(votos_sistema, total_votos):
    return (votos_sistema / total_votos) * 100

opcoes = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
votos = [0] * 6
total_votos = 0

while True:
    voto = int(input("Qual o melhor Sistema Operacional para uso em servidores? (0=fim): "))
    if voto == 0:
        break
    if 1 <= voto <= 6:
        votos[voto - 1] += 1
        total_votos += 1
    else:
        print("Informe um valor entre 1 e 6 ou 0 para sair!")

print("\nSistema Operacional     Votos   %")
print("-------------------     -----   ---")
for i in range(6):
    percentual = calcular_percentual(votos[i], total_votos)
    print(f"{opcoes[i]:<20} {votos[i]:>6}   {percentual:>5.1f}%")
print("-------------------     -----")
print(f"Total                  {total_votos:>6}\n")

melhor_sistema_index = max(range(6), key=lambda i: votos[i])
melhor_sistema = opcoes[melhor_sistema_index]
votos_melhor_sistema = votos[melhor_sistema_index]
percentual_melhor_sistema = calcular_percentual(votos_melhor_sistema, total_votos)

print(f"O Sistema Operacional mais votado foi o {melhor_sistema}, com {votos_melhor_sistema} votos, correspondendo a {percentual_melhor_sistema:.1f}% dos votos.")
