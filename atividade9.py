salario = float(input("Digite o salário do trabalhador: "))
emprestimo = float(input("Digite o valor da prestação do empréstimo: "))
prestacao = 0.2 * salario
if emprestimo > prestacao:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")