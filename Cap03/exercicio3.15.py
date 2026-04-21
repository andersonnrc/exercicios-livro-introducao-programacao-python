# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule
# quantos dias de vida um fumante perderá. Exiba o total em dias.

# Explicação passo a passo

# Entrada: o usuário informa quantos cigarros fuma por dia e há quantos anos fuma.

# Total de cigarros: multiplicamos a quantidade diária por 365 dias e pelo número de anos.

# Minutos perdidos: cada cigarro tira 10 minutos, então multiplicamos o total de cigarros por 10.

# Conversão para dias: dividimos os minutos perdidos por 1440 (minutos em um dia).

# Saída: mostramos o total de dias de vida reduzidos.

cigarros_por_dia = int(input("Informe a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Informe a quantidade de anos como fumante: "))


total_cigarros = cigarros_por_dia * 365 * anos_fumando
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / 1440

print(f"O fumante perderá {dias_perdidos:.0f} dias de vida.")
