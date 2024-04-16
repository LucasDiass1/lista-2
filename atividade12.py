nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
peso1 = 1
peso2 = 2
media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
aprovacao = 70
if media >= aprovacao:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"
print("Média do aluno:", media)
print("Situação:", situacao)