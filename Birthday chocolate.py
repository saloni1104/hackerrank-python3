n = int(input())
a = input().split()
for i in range (0,len(a)) :
    a[i] = int(a[i])
d,m = input().split()
d = int(d)
m = int(m)
b = 0
c = 0
for x in range (0,len(a)) :
    b = 0
    #print("x", x)
    for y in range (x,x+m) :
        if y<len(a) :
            #print("y", y)
            b = b+a[y]
        #print("b", b)
    if b == d :
        c = c+1
        #print("c", c)
print(c)