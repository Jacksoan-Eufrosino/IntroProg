contador = 0

for i in range(10):
    num = float(input("Digite um numero: "))
    contador += num

media = contador / 10

print(f'{media:.2f}')
