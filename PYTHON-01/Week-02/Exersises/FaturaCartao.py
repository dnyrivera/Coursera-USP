# Escreva um programa que receba o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura
# e imprima (saída de dados) a mensagem com os dados recebidos, no mesmo formato da mensagem acima.
# Note que o programa imprime a saída em duas linhas diferentes.
# Note também que, como não é preciso realizar cálculos, o valor não precisa ser convertido para número,
# pode ser tratado como texto.
# Entrada:
# Digite o nome do cliente: Fulano de Tal
# Digite o dia de vencimento: 9
# Digite o mês de vencimento: Janeiro
# Digite o valor da fatura: 350,00
# Saida:
# Olá, Fulano de Tal
# A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.

nomeCliente = input("Digite o nome do cliente: ")
diaVencimento = input("Digite o dia de vencimento: ")
mesVencimento = input("Digite o mês de vencimento: ")
valorFatura = input("Digite o valor da fatura: ")

print(f"Olá, {nomeCliente}")
print(
    f"A sua fatura com vencimento em {diaVencimento} de {mesVencimento} "
    f"no valor de R$ {valorFatura} está fechada."
)
