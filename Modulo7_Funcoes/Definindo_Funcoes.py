#  Ao escrevermos uma função, não estamos executando as instruções dentro dela
#  Estamos dizendo que existe a função, e que posteriormente poderemos usa-lá

def dar_boas_vindas():
    print("Olá.")
    print("Bem vindo ao curso de Python")


dar_boas_vindas()


def bem_vindo(nome_do_curso, nome, sobrenome):  # nome_do_curso é parâmetro
    print("Olá,", nome, sobrenome)
    print("Seja bem vindo ao curso de", nome_do_curso)


bem_vindo("JavaScript", "Sergio", "Sanchez")
#  JavaScript é argumento, é passado no lugar do parâmetro
#  Ou seja, parâmetro é o nome que aquela variável vai ter dentro da função
#  e argumento é o valor efetivamente passado, que podem ser múltiplos
#  Posso utilizar argumentos nomeados (keywords), como se vê abaixo:
bem_vindo(nome="Sergio", nome_do_curso="JavaScript", sobrenome="Sanchez")
#  Lembrando que, se eu nomeei um argumento no começo, tenho que nomear os
#  próximos, enquanto eu nomear somente o último é válido
bem_vindo("JavaScript", nome="Sergio", sobrenome="Sanchez")
#  Ou seja, argumento posicionais não podem aparecer depois de nomeados


def calcular_conta(total, taxa_servico, desconto_fidelidade):
    ...  # Os três pontos é utilizado pra quando quer continuar depois


calcular_conta(90, 0.1, 0.05)  # Veja que só olhando os argumentos fica meio
#  vago, portanto é indicado utilizar keywords
calcular_conta(total=90, taxa_servico=0.1, desconto_fidelidade=0.05)
