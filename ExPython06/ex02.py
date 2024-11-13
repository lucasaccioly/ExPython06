valores = []
while True:
    valor_str = input("Digite um valor inteiro (ou 'parar' para encerrar): ")
    if valor_str.lower() == "parar":
        break
try:
    valor = int(valor_str)
    valores.append(valor)
except ValueError:
        print("Por favor, digite um valor inteiro válido.")
        soma = sum(valores)
        print(f"A soma dos valores inseridos é: {soma}")
