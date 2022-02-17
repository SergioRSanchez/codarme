#  Valor padrão é quando eu coloco aqui em cima no PARÂMETRO
#  Se eu passo o valor no ARGUMENTO, ele ignora o valor padrão
#  Porém se eu não passo nada, ele calcula baseado no Valor Padrão
def calcular_conta(consumo, taxa_servico=0.1, desconto_fidelidade=0):
    servico = consumo * taxa_servico
    desconto = consumo * desconto_fidelidade
    total = consumo + servico - desconto
    print(f"O valor a ser pago é R$ {total}")


calcular_conta(consumo=100)
#  Só passou o consumo, mas calculou conforme o valor padrão

#  Vale observar que igual as keywords, se eu passei um parâmetro com padrão,
#  os próximos parâmetros tem que ter padrão também (default argument)
