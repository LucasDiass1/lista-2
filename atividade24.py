import math

def calcular_preco_estacionamento(chegada, partida):
    chegada_minutos = chegada[0] * 60 + chegada[1]
    partida_minutos = partida[0] * 60 + partida[1]
    duracao_em_minutos = partida_minutos - chegada_minutos
    
    if duracao_em_minutos <= 120:
        preco = math.ceil(duracao_em_minutos / 60) * 1.00
    elif duracao_em_minutos <= 240:
        preco = 2 * 1.00 + math.ceil((duracao_em_minutos - 120) / 60) * 1.40
    else:
        preco = 2 * 1.00 + 2 * 1.40 + math.ceil((duracao_em_minutos - 240) / 60) * 2.00
    
    return preco
chegada = tuple(map(int, input("Digite o momento de chegada (horas minutos): ").split()))
partida = tuple(map(int, input("Digite o momento de partida (horas minutos): ").split()))
preco = calcular_preco_estacionamento(chegada, partida)
print("O preço cobrado pelo estacionamento é R$ {:.2f}".format(preco))