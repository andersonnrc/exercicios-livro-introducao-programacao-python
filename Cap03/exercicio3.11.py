# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.

preco = float(input("Informe o preço da mercadoria: "))
desconto = float(input("Informe o percentual do desconto: "))

preco_com_desconto = preco - (preco * desconto) / 100 
valor_desconto = preco * desconto / 100

print(f"Valor do desconto = {valor_desconto:.2f} \nPreço com desconto = {preco_com_desconto:.2f}")
