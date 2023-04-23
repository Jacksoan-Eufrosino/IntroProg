nota = int(input("digite sua nota: "))
notas_invalidas = 0
while nota <= 0 or nota >= 100:
   notas_invalidas += 1 
   nota = int(input("digite um nota válida: "))
   
print(f"{nota} é uma nota válida !")
print(f"voce digitou um total de {notas_invalidas} notas invalidas !")
