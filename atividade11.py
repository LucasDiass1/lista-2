import math
numero = int(input("Digite um número inteiro: "))
if numero < 0:
    print("Número inválido")
else:
    logaritmo = math.log(numero)
    print("O logaritmo de", numero, "é:", logaritmo)