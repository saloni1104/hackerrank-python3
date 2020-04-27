a = list(map(int,input().split()))
b = list(map(int,input().split()))
a1 = 0
b1 = 0
for i in range(0,3) :
    if a[i]>b[i] :
        a1 = a1+1
    elif a[i]<b[i] :
        b1 = b1+1
print(str(a1)+" "+str(b1))