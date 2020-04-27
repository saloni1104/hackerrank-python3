n = input()
arr = input().split()
for i in range (0,len(arr)) :
    arr[i]=int(arr[i])
arr.sort()
#print(arr)
k=0
d=1
l=0

for x in range (l,len(arr)+1) :
    #print("x", x)
    if x+1<len(arr) :
        if arr[x] == arr[x+1] :
            k = k+1
            #print("k", k)
            l = l+1
        else :
            l = l+1
            k = 0
            
        
    if k>d :
        d = k
        d1 = arr[x]
            
        #print("d", d)
print(d1)
