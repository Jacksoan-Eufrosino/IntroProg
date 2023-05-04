entrada = int(input())
print(entrada)

n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0

n100 = entrada // 100
entrada = entrada % 100

n50 = entrada // 50
entrada = entrada % 50

n20 = entrada // 20
entrada = entrada % 20

n10 = entrada // 10
entrada = entrada % 10

n5 = entrada // 5
entrada = entrada % 5

n2 = entrada // 2
entrada = entrada % 2

n1 = entrada//1
entrada = entrada % 1


print(n100, 'nota(s) de R$ 100,00')
print(n50, 'nota(s) de R$ 50,00')
print(n20, 'nota(s) de R$ 20,00')
print(n10, 'nota(s) de R$ 10,00')
print(n5, 'nota(s) de R$ 5,00')
print(n2, 'nota(s) de R$ 2,00')
print(n1, 'nota(s) de R$ 1,00')
