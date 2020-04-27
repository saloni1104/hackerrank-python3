n = int(input())
b=[]
b1=[]
while n>0 :
    a = input().split()
    b.append(a[0])
    c = (float(a[1])+float(a[2])+float(a[3]))/3
    b1.append(c)
    
    n = n-1
d = input()
for j in range (0,len(b)) :
    if b[j] == d :
        print("{:.2f}".format(b1[j]))