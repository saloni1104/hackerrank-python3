n = int(input())
ar = input()
ar1 = ar.split(' ')
for i in range (0,len(ar1)) :
    ar1[i] = int(ar1[i])
ar1.sort()
print(ar1)
i = 0
j = 1
f = 0
while n>0 :
    if i<n and j<n :
        if ar1[i] == ar1[j] :
            f = f+1
            i = i+2
            j = j+2
        else :
            i = i+1
            j = j+1
    else :
        break
print(f)