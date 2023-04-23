numero = int(input("Digite um numero inteiro: (0 ou um numero < que 0 para sair)"))
qtd_numeros = 0

while numero > 0:
    for i in range(1, numero+1):
        if numero % i == 0:
            print(f"{i} é divisor de {numero}")
    qtd_numeros += 1
    numero = int(input("Digite um novo numero: "))

print(f"Foram informados {qtd_numeros} numeros !")
