def classificar_atleta_bocha(idade):
    if 5 <= idade <= 7:
        return "Infantil A"
    elif 8 <= idade <= 10:
        return "Infantil B"
    elif 11 <= idade <= 13:
        return "Juvenil A"
    elif 14 <= idade <= 17:
        return "Juvenil B"
    else:
        return "Sênior"
idade = int(input("Digite a idade do atleta: "))
categoria = classificar_atleta_bocha(idade)
print(f"O atleta está na categoria {categoria}.")