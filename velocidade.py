# Programa para verificar a velocidade e calcular a multa
velocidade = float(input("Qual é a velocidade do carro (em km/h)? "))

# Verificar se a velocidade ultrapassa 80 km/h
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 5
    print(f"Você foi multado! Excedeu o limite de velocidade em {excesso:.2f} km/h.")
    print(f"Valor da multa: €{multa:.2f}")
else:
    print("Velocidade dentro do limite permitido. Não há multa.")