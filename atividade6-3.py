while True:
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        print(f"{numero} é par !!")
    else:
        print(f"{numero} é impar !!")

    escolha = input("Digite S para sair ou C para continuar: ")

    if escolha == 'S':
        break
    elif escolha == 'C':
        continue
