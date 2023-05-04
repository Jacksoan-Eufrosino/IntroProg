n = float(input())

nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0

moeda_1 = 0
moeda_050 = 0
moeda_025 = 0
moeda_010 = 0
moeda_005 = 0
moeda_001 = 0

nota_100 = int(n // 100)
n = n % 100

nota_50 = int(n // 50)
n = n % 50

nota_20 = int(n // 20)
n = n % 20

nota_10 = int(n // 10)
n = n % 10

nota_5 = int(n // 5)
n = n % 5

nota_2 = int(n // 2)
n = n % 2

moeda_1 = int(n // 1)
n = n % 1

moeda_050 = int(n // 0.50)
n = n % 0.50

moeda_025 = int(n // 0.25)
n = n % 0.25

moeda_010 = int(n // 0.10)
n = n % 0.10

moeda_005 = int(n // 0.05)
n = n % 0.05

moeda_001 = int(n // 0.01)
n = n % 0.01

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(nota_100))
print('{} nota(s) de R$ 50.00'.format(nota_50))
print('{} nota(s) de R$ 20.00'.format(nota_20))
print('{} nota(s) de R$ 10.00'.format(nota_10))
print('{} nota(s) de R$ 5.00'.format(nota_5))
print('{} nota(s) de R$ 2.00'.format(nota_2))


print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(moeda_1))
print('{} moeda(s) de R$ 0.50'.format(moeda_050))
print('{} moeda(s) de R$ 0.25'.format(moeda_025))
print('{} moeda(s) de R$ 0.10'.format(moeda_010))
print('{} moeda(s) de R$ 0.05'.format(moeda_005))
print('{} moeda(s) de R$ 0.01'.format(moeda_001))
