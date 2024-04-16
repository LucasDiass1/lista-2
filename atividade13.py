laboratorio = float(input("Digite a nota do trabalho de laboratório (0 a 10): "))
semestral = float(input("Digite a nota da avaliação semestral (0 a 10): "))
final = float(input("Digite a nota do exame final (0 a 10): "))
pesoL = 2
pesoS = 3
pesoF = 5
media = (laboratorio * pesoL + semestral * pesoS+ final * pesoF) / (pesoL + pesoS + pesoF)
if media >= 0 and media <= 2.9:
    situacao = "REPROVADO   "
elif media >= 3 and media <= 4.9:
    situacao = "Em recuperação"
else:
    situacao = "Aprovado"
print("Média do aluno:", media)
print("Situação:", situacao)