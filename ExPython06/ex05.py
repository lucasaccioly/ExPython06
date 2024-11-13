def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
def composicao_corporal(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 25:
        return "Peso ideal"
    else:
        return "Sobrepeso"
    def analisar_usuario(nome, idade, peso, altura, sexo):
        maioridade = "maior" if idade >= 18 else "menor"
 imc = calcular_imc(peso, altura)
 composicao = composicao_corporal(imc)
return len(nome), maioridade, imc, composicao
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M ou F): ")
print(f"Seu nome possui {caracteres_nome} caracteres.")
print(f"Você é {idade_status} de idade.")
print(f"Seu IMC é: {imc:.2f}")
print(f"Sua composição corporal é: {composicao}")