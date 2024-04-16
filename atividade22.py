def calcular_preco_final(valor_produto, estado):
    impostos = {'MG': 0.07, 'SP': 0.12, 'RJ': 0.15, 'MS': 0.08}

    if estado in impostos:
        taxa_imposto = impostos[estado]
        preco_final = valor_produto * (1 + taxa_imposto)
        return preco_final
    else:
        return None
valor_produto = float(input("Digite o valor do produto: "))
estado_destino = input("Digite a sigla do estado destino (MG, SP, RJ, MS): ").upper()
preco_final = calcular_preco_final(valor_produto, estado_destino)
if preco_final is not None:
    print(f"O preço final do produto para o estado {estado_destino} é R${preco_final:.2f}.")
else:
    print("Erro: Estado inválido.")