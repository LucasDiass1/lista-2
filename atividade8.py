nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
    media = (nota1 + nota2) / 2
    print("a media das notas eh:", media)
else:
    print("Nota invalida. As notas devem ser entre 0.0 e 10.0.")