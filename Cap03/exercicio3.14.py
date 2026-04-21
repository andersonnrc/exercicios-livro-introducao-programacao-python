# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

quant_km = int(input("Informe a quantidade de km percorridos: "))
quant_dias = int(input("Informe a quantidade de dias em que o carro foi alugado: "))

valor_a_pagar = (quant_dias * 60) + (quant_km * 0.15)

print(f"Valor a pagar = {valor_a_pagar:.2f}")
