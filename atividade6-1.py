numero = int(input("Digite qualquer numero. Digite 0 para sair. "))
maior_numero = 0
while numero != 0:
    numero = int(input("Digite um numero: "))
    if numero > maior_numero:
        maior_numero = numero

print(f"O maior numero é {maior_numero} !")
