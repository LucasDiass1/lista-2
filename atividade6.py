num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
if num1 > num2:
    maior = num1
    diferenca = num1 - num2
else:
    maior = num2
    diferenca = num2 - num1
print("O maior numero eh:", maior)
print("A diferença entre os numeros eh:", diferenca)