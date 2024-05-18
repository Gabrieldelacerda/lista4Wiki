notas = []
valor = 0

while valor != -1:
    valor = float(input("Digite uma nota (-1 para encerrar): "))
    if valor != -1:
        notas.append(valor)

quantidade = len(notas)

print(f"Quantidade de valores lidos: {quantidade}")
print("Valores informados:", end=" ")
for nota in notas:
    print(nota, end=" ")

print("\nValores na ordem inversa:")
for nota in reversed(notas):
    print(nota)

soma = sum(notas)
print(f"Soma dos valores: {soma}")

media = soma / quantidade
print(f"Média dos valores: {media:.2f}")

media_acima = sum(1 for nota in notas if nota > media)
print(f"Quantidade de valores acima da média: {media_acima}")

abaixo_de_sete = sum(1 for nota in notas if nota < 7)
print(f"Quantidade de notas inseridas abaixo de sete: {abaixo_de_sete}")
