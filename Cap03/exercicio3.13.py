# Escreva um programa que converta uma temperatura digitada em °C em ºF.
# A fórmula é F = (9 x C / 5) + 32

tc = int(input("Informe a temperatura em ºC: "))

tf = (tc * 9 / 5) + 32

print(f"{tc}ºC equivale a {tf}ºF")
