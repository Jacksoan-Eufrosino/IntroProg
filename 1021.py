n = float(input())

n100 = n / 100
resto = round(n % 100, 2)

n50 = resto / 50
resto = round(resto % 50, 2)

n20 = resto / 20
resto = round(resto % 20, 2)

n10 = resto / 10
resto = round(resto % 10, 2)

n5 = resto / 5
resto = round(resto % 5, 2)

n2 = resto / 2
resto = round(resto % 2, 2)

m1 = resto / 1
resto = round(resto % 1, 2)

m50 = resto / 0.50
resto = round(resto % 0.50, 2)

m25 = resto / 0.25
resto = round(resto % 0.25, 2)

m10 = resto / 0.10
resto = round(resto % 0.10, 2)

m05 = resto / 0.05
resto = round(resto % 0.05, 2)

m01 = resto / 0.01
resto = round(resto % 0.01, 2)

print("NOTAS:")
print(int(n100), "nota(s) de R$ 100.00")
print(int(n50), "nota(s) de R$ 50.00")
print(int(n20), "nota(s) de R$ 20.00")
print(int(n10), "nota(s) de R$ 10.00")
print(int(n5), "nota(s) de R$ 5.00")
print(int(n2), "nota(s) de R$ 2.00")
print("MOEDAS:")
print(int(m1), "moeda(s) de R$ 0.01")
print(int(m50), "moeda(s) de R$ 1.00")
print(int(m25), "moeda(s) de R$ 0.50")
print(int(m10), "moeda(s) de R$ 0.25")
print(int(m05), "moeda(s) de R$ 0.10")
print(int(m01), "moeda(s) de R$ 0.05")
