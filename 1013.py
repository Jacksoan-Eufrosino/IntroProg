a,b,c = input().split()
a,b,c = int(a), int(b), int(c)

maiorAB = (a+b+abs(a-b))/2
maiorABC = int((maiorAB+c+abs(maiorAB-c))/2)
print(maiorABC,'eh o maior')
