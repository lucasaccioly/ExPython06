def letra_para_valor(letra):
    letra = letra.lower()
     valor_a = ord('a')
    valor_letra = ord(letra)
     posicao = valor_letra - valor_a + 1
    return posicao
def numeros_pares_ou_impares(valor):
   if valor % 2 == 0:
        
        return list(range(2, valor + 1, 2))
    else:
        # Se o valor for ímpar
        return list(range(1, valor + 1, 2))
   letra = input("Digite uma letra do alfabeto: ")
valor = letra_para_valor(letra)
numeros = numeros_pares_ou_impares(valor)
if valor % 2 == 0:
    print(f"Os valores pares de 2 até {valor} são: {numeros}")
else:
    print(f"Os valores ímpares de 1 até {valor} são: {numeros}")


