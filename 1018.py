valor = int(input())

resto = 0
novo_valor = valor

nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0
nota_1 = 0

if valor >= 100:
    resto = valor % 100
    nota_100 = valor // 100

if resto >= 50:
    nota_50 = resto // 50
    resto = resto % 50

if resto >= 20:
    nota_20 = resto // 20
    resto = resto % 20

if resto >= 10:
    nota_10 = resto // 10
    resto = resto % 10

if resto >= 5:
    nota_5 = resto // 5
    resto = resto % 5

if resto >= 2:
    nota_2 = resto // 2
    resto = resto % 2

if resto >= 1:
    nota_1 = resto // 1
    resto = resto % 1

print(valor)
print(nota_100, 'nota(s) de R$ 100,00')
print(nota_50, 'nota(s) de R$ 50,00')
print(nota_20, 'nota(s) de R$ 20,00')
print(nota_10, 'nota(s) de R$ 10,00')
print(nota_5, 'nota(s) de R$ 5,00')
print(nota_2, 'nota(s) de R$ 2,00')
print(nota_1, 'nota(s) de R$ 1,00')
