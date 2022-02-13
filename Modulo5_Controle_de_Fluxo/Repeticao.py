i = 1
while i <= 10:
    print(i)
    i += 1

print("Fim")
print(i)


total = 0
while True:
    valor = float(input("Digite o valor da compra: \n"))
    total = total + valor

    continuar = input("Deseja continuar? [s/n] ")
    if continuar != "s":
        break

print("O valor total da compra é:", total)
