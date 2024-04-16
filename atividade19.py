def tipo_de_triangulo(a, b, c):
    return ("Não é um triângulo" if a >= b + c or b >= a + c or c >= a + b 
            else "Equilátero" if a == b == c 
            else "Escaleno" if a != b != c != a 
            else "Isósceles")
a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))
tipo = tipo_de_triangulo(a, b, c)
print("O triângulo é", tipo)