# Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

salario = float(input("Digite o valor do salário: "))
porcentagem = float(input("Digite a porcentagem: "))

novo_salario = (salario * porcentagem) / 100 + salario
valor_aumento = salario * porcentagem / 100

print(f"Valor do aumento = {valor_aumento:.2f} \nNovo salário = {novo_salario:.2f}")
