def converter_dolar_para_reais(valor_dolar):
    taxa_conversao = 5.09
    valor_reais = valor_dolar * taxa_conversao
    return valor_reais
def calcular_frete(peso_em_gramas):
    taxa_frete_por_100g = 1.99
    peso_em_kg = peso_em_gramas / 1000
    valor_frete = peso_em_kg * taxa_frete_por_100g
    return valor_frete
import funcoes
produto = input("Digite o nome do produto: ")
peso_em_gramas = float(input("Digite o peso do produto em gramas: "))
valor_em_dolar = float(input("Digite o valor do produto em dólares: "))
valor_produto_reais = funcoes.converter_dolar_para_reais(valor_em_dolar)
valor_frete_reais = funcoes.calcular_frete(peso_em_gramas)
valor_total_reais = valor_produto_reais + valor_frete_reais
print(f"Valor do produto em reais: R${valor_produto_reais:.2f}")
print(f"Valor do frete em reais: R${valor_frete_reais:.2f}")
print(f"Valor total da compra em reais: R${valor_total_reais:.2f}")
