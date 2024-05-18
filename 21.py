modelos = ["FUSCA", "GOL", "UNO", "VECTRA", "PEUGEOUT"]
consumo = [7, 10, 12.5, 9, 14.5]

consumo_ideal = min(consumo)
modelo_mais_economico = modelos[consumo.index(consumo_ideal)]

preco_gasolina = 2.25
distancia = 1000

print("Comparativo de Consumo de Combustível\n")
for i in range(len(modelos)):
    litros_necessarios = distancia / consumo[i]
    custo = litros_necessarios * preco_gasolina
    print(f"{i+1} - {modelos[i]:<15} - {consumo[i]:>5.1f} - {litros_necessarios:>6.1f} litros - R$ {custo:.2f}")

print("\nRelatório Final")
print(f"O menor consumo é do {modelo_mais_economico.lower()}.")
