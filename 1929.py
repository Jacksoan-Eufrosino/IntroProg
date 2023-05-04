a,b,c,d = input().split()
a,b,c,d = int(a),int(b),int(c),int(d)

#a,b,c
if a + b > c and a + c > b and b + c > a:
    print('S')
#a,b,d
elif a + b > d and a + d > b and b + d > a:
    print('S')
#a,c,d
if a + c > d and a + d > c and d + c > a:
    print('S')
#b,c,d
if b + c > d and b + d > c and d + c > b:
    print('S')
else:
    print('N')



