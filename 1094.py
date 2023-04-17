casos = int(input("Digite o numero de casos: "))

coelhos = 0
ratos = 0
sapos = 0


for caso in range(casos):
    entrada = input('Digite o numero de cobaias usadas no teste com sua inicial: ')
    valor, sigla = entrada.split()
    valor = int(valor)
    if sigla == 'C':
        coelhos += valor
    elif sigla == 'R':
        ratos += valor
    elif sigla == 'S':
        sapos += valor
    else:
        print('Entrada invalida')

total = coelhos + ratos + sapos
perc_coelhos = coelhos / total * 100
perc_ratos = ratos / total * 100
perc_sapos = sapos / total * 100

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {perc_coelhos:.2f} %')
print(f'Percentual de ratos: {perc_ratos:.2f} %')
print(f'Percentual de sapos: {perc_sapos:.2f} %')
