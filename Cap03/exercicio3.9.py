# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
# Calcule o total em segundos

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade em horas: "))
minutos = int(input("Digite a quantidade em minutos: "))
segundos = int(input("Digite a quantidade em segundos: "))

total_segundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

print(f"Total em segundos = {total_segundos}")
