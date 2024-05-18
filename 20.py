salarios = []
abonos = []

while True:
    salario = float(input("Salário: "))
    if salario == 0:
        break
    salarios.append(salario)

for salario in salarios:
    abono = max(100, salario * 0.2)
    abonos.append(abono)

print("\nProjeção de Gastos com Abono")
print("============================\n")
print("Salário    - Abono")
for salario, abono in zip(salarios, abonos):
    print(f"R$ {salario:8.2f} - R$ {abono:8.2f}")

total_funcionarios = len(salarios)
total_abonos = sum(abonos)
funcionarios_abono_minimo = sum(1 for abono in abonos if abono == 100)
maior_abono = max(abonos)

print(f"\nForam processados {total_funcionarios} colaboradores")
print(f"Total gasto com abonos: R$ {total_abonos:.2f}")
print(f"Valor mínimo pago a {funcionarios_abono_minimo} colaboradores")
print(f"Maior valor de abono pago: R$ {maior_abono:.2f}")
