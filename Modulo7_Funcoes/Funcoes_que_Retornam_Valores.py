def calcular_conta(consumo, taxa_servico, desconto_fidelidade):
    servico = consumo * taxa_servico
    desconto = consumo * desconto_fidelidade
    total = consumo + servico - desconto
    print(f"O valor a ser pago é R$ {total}")


calcular_conta(consumo=100, taxa_servico=0.1, desconto_fidelidade=0.05)


#  Ao invés de imprimir o valor final, podemos retornar a função

def calcular_conta2(consumo2, taxa_servico2, desconto_fidelidade2):
    if taxa_servico2 == 0 and desconto_fidelidade2 == 0:
        return consumo2
#  Isso chama early return, é quando não precisa percorrer o resto da função
    servico2 = consumo2 * taxa_servico2
    desconto2 = consumo2 * desconto_fidelidade2
    total2 = consumo2 + servico2 - desconto2
    return total2

#  O return significa para retornar o valor, mas também para acabar a execução
#  dessa função


total2 = calcular_conta2(consumo2=200, taxa_servico2=0.15,
                         desconto_fidelidade2=0.1)
print(f"O valor a ser pago é R$ {total2}")
