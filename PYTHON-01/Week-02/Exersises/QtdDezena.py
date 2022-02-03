# Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.
# Exemplo 1:
# Digite um número inteiro: 78615
# Saída de Dados:
# O dígito das dezenas é 1
#
# Exemplo 2:
# Digite um número inteiro: 2
# Saída de Dados:
# O dígito das dezenas é 0
#
# Dica: O operador "//" faz uma divisão inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor.
# O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado
# ou seja, tudo que é maior ou igual ao divisor.

numero = int(input("Digite um número inteiro: "))

unidade = int(numero % 10)
dezena = int(((numero - unidade) / 10) % 10)

print(f"O dígito das dezenas é {dezena}")
