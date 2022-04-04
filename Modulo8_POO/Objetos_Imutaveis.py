""" Economiza memória, pois novos símbolos vão ser atribuídos ao mesmo objeto.
Vamos supor que tenhamos a variável x = 10.
O que acontece por baixo dos panos é que "x" é um SÍMBOLO que está apontando
para um OBJETO na memória, com posição 0, e que armazena o valor 10.
Quando tu imprimi x na tela, ele vai pegar a variável x, ver qual objeto ela
aponta/referencia e pegar o valor que está armazenado na memória. Depois passa
pra função print, que vai imprimir na tela.

Agora vamos supor que criamos a variável y = 10.
O Python sabe que 10 é um valor imutável (10 é 10, e não muda), portanto, ao
invés de criar outro objeto na memória, ele só adiciona o símbolo "y" na
memória, e referencia ele para o mesmo objeto inteiro com valor 10.

E o que acontece quando fazemos x = x + 1?
O interpretador vai pegar o valor da direita, vai calcular e ver que é igual a
11, então na memória ele vai criar outro objeto do tipo inteiro com valor 11,
ou seja, aquele objeto com valor 10 ainda vai ficar lá na memória, mas o x
agora aponta para o OBJETO na memória com posição 1. """

x = 10
print(id(10))  # Para mostra o endereço na memória do objeto que armazena 10
print(id(x))  # Observe que o endereço é o mesmo
print(id(10) == id(x))

y = x
print(id(y))  # Todos referenciaram o mesmo endereço

x = x + 1
print(id(x))  # Observe que o endereço de x mudou
print(id(11))  # Mesmo endereço de x, pois x agora vale 11
print(id(11) == id(x))
