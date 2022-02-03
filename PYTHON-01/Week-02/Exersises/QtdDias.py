# Reescreva o programa contaSegundos para imprimir também a quantidade de dias,
# faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em
# dias, horas, minutos e segundos. A saída deve estar no formato:
# a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato!
# Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro
#
# Exemplo:
# Por favor, entre com o número de segundos que deseja converter: 178615
#
# Saída de Dados:
# 2 dias, 1 horas, 36 minutos e 55 segundos.

totalSeconds = int(
    input("Por favor, entre com o número de segundos que deseja converter: ")
)

days = totalSeconds // 86400
restDays = totalSeconds % 86400
hours = restDays // 3600
restTime = restDays % 3600
minutes = restTime // 60
restSeconds = restTime % 60

print(f"{days} dias, {hours} horas, {minutes} minutos e {restSeconds} segundos.")
