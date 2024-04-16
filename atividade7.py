num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
if num1 == num2:
    print("Numeros iguais")
else:
    maior = max(num1, num2)
    print("O maior numero eh:", maior)