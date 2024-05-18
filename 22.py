situacoes = {
    "necessita da esfera": 0,
    "necessita de limpeza": 0,
    "necessita troca do cabo ou conector": 0,
    "quebrado ou inutilizado": 0
}

total_mouses = 0

while True:
    identificacao = int(input("Identificação do mouse (0 encerra): "))
    if identificacao == 0:
        break
    situacao = input("Situação do mouse: ")
    situacoes[situacao] += 1
    total_mouses += 1

print("\nRelatório Final")
print("Quantidade de mouses:", total_mouses)
print("\nSituação                        Quantidade              Percentual")
for situacao, quantidade in situacoes.items():
    percentual = (quantidade / total_mouses) * 100
    print(f"{situacao:<30} {quantidade:<24} {percentual:>6.1f}%")
