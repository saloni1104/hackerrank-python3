n = int(input())
b = []
a1 = 0
b1 = 0
for i in range(0,n) :
    a = list(map(int,input().split()))
    a1 = a1+ a[i]
    b1 = b1+ (a[n-i-1])
if a1>b1 :
    print(a1-b1)
else :
    print(b1-a1)