"""
    i. Deve conter uma classe 'usuário',
    ii. Classe 'usuario' deve ter um construtor que recebe 'nome' e 'email',
    iii. Classe 'usuario' deve possuir um método de instância 'imprime_usuario'
que imprime: "Gabriel (gabriel@exemplo.com)", para uma instância com
'nome' = "Gabriel" e 'email' = "gabriel@exemplo.com",
    iv. Classe 'usuario' deve possuir um atributo de classe 'quantidade' que
armazena a quantidade de instâncias criadas, sejam instâncias de 'usuario' ou
de qualquer classe que estenda 'usuario'. Por exemplo: Administrador(usuario)
"""


class Usuario:
    quantidade = 0

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.quantidade = Usuario.quantidade
        Usuario.quantidade += 1

    def imprime_usuario(self):
        print(f"{self.nome} ({self.email})")
