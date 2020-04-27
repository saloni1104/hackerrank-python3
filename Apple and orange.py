s,t = input().split()
s = int(s)
t = int(t)
a,b = input().split()
a = int(a)
b = int(b)
k = 0
l = 0
m,n = input().split()
apples = input().split()
for i in range (0,len(apples)) :
    apples[i] = int(apples[i])+a
    if apples[i] >= s and apples[i] <= t :
        k = k+1
oranges = input().split()
for j in range (0,len(oranges)) :
    oranges[j] = int(oranges[j])+b
    if oranges[j] >= s and oranges[j] <= t :
        l = l+1
print(k)
print(l)