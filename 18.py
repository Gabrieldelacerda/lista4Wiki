def calcular_percentual(votos_jogador, total_votos):
    return (votos_jogador / total_votos) * 100

votos = [0] * 23
total_votos = 0

while True:
    num_jogador = int(input("Número do jogador (0 para terminar): "))
    if num_jogador == 0:
        break
    if 1 <= num_jogador <= 23:
        votos[num_jogador - 1] += 1
        total_votos += 1
    else:
        print("Informe um valor entre 1 e 23 ou 0 para sair.")

print("\nResultado da votação:\n")
print(f"Foram computados {total_votos} votos.\n")
print("Jogador votos     %")

for i in range(23):
    if votos[i] > 0:
        percentual = calcular_percentual(votos[i], total_votos)
        print(f"{i + i:2}    {votos[i]:2}        {percentual:5.1f}%")

melhor_jogador = max(range(23), key=lambda i: votos[i])
percentual_melhor = calcular_percentual(votos[melhor_jogador], total_votos)

print(f"\nO melhor jogador foi o de número {melhor_jogador + 1}, com {votos[melhor_jogador]} votos, correspondendo a {percentual_melhor:.1f}% do total de votos.")

with open("resultado_votacao.txt", "w") as arquivo:
    arquivo.write("Resultado da votação:\n\n")
    arquivo.write(f"Foram computados {total_votos} votos.\n\n")
    arquivo.write("Jogador votos      %n")
    for i in range(23):
        if votos[i] > 0:
            percentual = calcular_percentual(votos[i], total_votos)
            arquivo.write(f"{i + 1:2}      {votos[i]:2}      {percentual:5.1f}%\n")
    arquivo.write(f"\nO melhor jogador foi o de número {melhor_jogador + 1} com {votos[melhor_jogador]} votos, correspondendo a {percentual_melhor:.1f}% do total de votos.\n")
