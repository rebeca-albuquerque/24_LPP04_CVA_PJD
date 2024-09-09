# Solicita que o usuário digite o ano de nascimento
ano = int(input("Digite o ano de nascimento: "))

idade = 2024 - ano

print("A sua idade é:", idade)

# Verifica a faixa etária e imprime a mensagem correspondente
if idade >= 65:
    print("És um sénior")
elif idade >= 18:
    print("És um adulto")
else:
    print("És uma criança")
