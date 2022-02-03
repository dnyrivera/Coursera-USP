# Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado
# calcule e imprima (saída de dados) seu perímetro e sua área.
# Observação: a saída deve estar no formato: "perímetro: x - área: y"

ladoQuadrado = int(input("Digite o valor correspondente ao lado de um quadrado:"))
perimetroQuadrado = ladoQuadrado * 4
areaQuadrado = ladoQuadrado**2
print(f"perímetro: {perimetroQuadrado} - área: {areaQuadrado}")
