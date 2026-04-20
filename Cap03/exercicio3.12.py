# Escreva um programa que calcule o tempo de uma viagem de carro. 
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia_km = int(input("Informe a distância a ser percorrida: "))
velocidade_media = int(input("Informa a velocidade média em km/h: "))

tempo = distancia_km / velocidade_media

print(f"Tempo da viagem = {tempo:.2f}")
