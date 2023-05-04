peca1, n_peca1, val_peca1 = input().split()
peca1, n_peca1, val_peca1 = int(peca1), int(n_peca1), float(val_peca1)
peca2, n_peca2, val_peca2 = input().split()
peca2, n_peca2, val_peca2 = int(peca2), int(n_peca2), float(val_peca2)

valor_toal = (n_peca1 * val_peca1) + (n_peca2 * val_peca2)

print('VALOR A PAGAR: R$ {:.2f}'.format(valor_toal))
