casos = int(input("Digite o numero de casos: "))

coelinhos = 0
ratos = 0
sapos = 0


for caso in range(casos):
    entrada = input(
        'Digite o numero de cobaias usadas no teste com sua inicial: ')
    valor, letra = entrada.split()
    valor = int(valor)
    if letra == 'C':
        coelinhos += valor
    elif letra == 'R':
        ratos += valor
    elif letra == 'S':
        sapos += valor
    else:
        print('Entrada invalida')


total = coelinhos + ratos + sapos
perc_coelinhos = coelinhos / total * 100
perc_ratos = ratos / total * 100
perc_sapos = sapos / total * 100

print(f'Total: {total} cobaias')
print(f'Total de coelinhos: {coelinhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelinhos: {perc_coelinhos:.2f} %')
print(f'Percentual de ratos: {perc_ratos:.2f} %')
print(f'Percentual de sapos: {perc_sapos:.2f} %')
