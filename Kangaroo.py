x1,v1,x2,v2 = input().split()
x1 = int(x1)
v1 = int(v1)
x2 = int(x2)
v2 = int(v2)
a = 5000
d1 = x1
d2 = x2
if x1<x2 and v1<v2 :
    print("NO")
else :
    while a>0 :
        d1 = d1 + v1
        d2 = d2 + v2
        if d1 == d2 :
            print("YES")
            break
        a = a-1
    if d1 != d2 :
        print("NO")
    