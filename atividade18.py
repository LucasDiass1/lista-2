numero = int(input("Digite um número inteiro: "))
if (numero % 3 == 0 and numero % 5 != 0) or (numero % 3 != 0 and numero % 5 == 0):
    print("O número", numero, "é divisível por 3 ou por 5, mas não simultaneamente pelos dois.")
else:
    print('o numero não atende aos requisitos')