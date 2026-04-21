# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação: 
# R para residências, I para indústrias e C para comércios.
# Calcule o preço a pagar de acordo com a tabela a seguir:

# Preço por tipo e faixa de consumo
# Tipo              Faixa               Preço
# Residencial       Até 500             R$ 0,40
# Residencial       Acima de 500        R$ 0,65
# Comercial         Até 1000            R$ 0,55
# Comercial         Acima de 1000       R$ 0,60
# Industrial        Até 5000            R$ 0,55
# Industrial        Acima de 5000       R$ 0,60

tipo_instalacao = input("Informe o tipo de instalação: ").upper()
quant_kwh = int(input("Informe a quantidade de kWh: "))
preco = 0

if tipo_instalacao == 'R':
    if quant_kwh <= 500:
        preco = quant_kwh * 0.40
    else: 
        preco = quant_kwh * 0.65
elif tipo_instalacao == 'C':
    if quant_kwh <= 1000:
        preco = quant_kwh * 0.55
    else:
        preco = quant_kwh * 0.60
elif tipo_instalacao == 'I':
    if quant_kwh <= 5000:
        preco = quant_kwh * 0.55
    else:
        preco = quant_kwh * 0.60
else:
    print("Opção inválida!")
    exit()

print(f"Preço a pagar: R$ {preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
