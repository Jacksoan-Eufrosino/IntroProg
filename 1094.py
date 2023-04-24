casos = int(input())

coelhos = 0
ratos = 0
sapos = 0


for caso in range(casos):
    entrada = input()
    valor, letra = entrada.split()
    valor = int(valor)
    if letra == 'C':
        coelhos += valor
    elif letra == 'R':
        ratos += valor
    elif letra == 'S':
        sapos += valor
    else:
        print('Entrada invalida')


total = coelhos + ratos + sapos
perc_coelhos = coelhos / total * 100
perc_ratos = ratos / total * 100
perc_sapos = sapos / total * 100

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(coelhos))
print('Total de ratos: {}'.format(ratos))
print('Total de sapos: {}'.format(sapos))
print('Percentual de coelhos: {:.2f} %'.format(perc_coelhos))
print('Percentual de ratos: {:.2f} %'.format(perc_ratos))
print('Percentual de sapos: {:.2f} %'.format(perc_sapos))
