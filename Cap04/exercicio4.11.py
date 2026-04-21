# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário. 
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input(f"Informe o valor da casa: "))
salario = float(input("Informe o salário: "))
quant_anos = int(input("Informe a quantidade de anos a pagar: "))

quant_meses = quant_anos * 12
valor_prestacao = valor_casa / quant_meses
limite = salario * 0.30

if valor_prestacao <= limite:
    print(f"Empréstimo aprovado. Prestação mensal = {valor_prestacao:.2f}")
else:
    print(f"Empréstimo negado. Prestação mensal = {valor_prestacao:.2f}")


