meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas = []

for mes in meses:
    temp = float(input(f"Digite a temperatura de {mes}: "))
    temperaturas.append(temp)

media_anual = sum(temperaturas) / len(temperaturas)

print("Temperaturas acima da média anual:")
for i, temp in enumerate(temperaturas):
    if temp > media_anual:
        print(f"{meses[i]}: {temp} graus Celsius")
