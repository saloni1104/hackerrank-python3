m,n = input().split()
n = int(n)
arr = input().split()
for i in range(0,len(arr)) :
    arr[i]=int(arr[i])

k = 0
for x in range(0,len(arr)-1) :
    for y in range (x+1,len(arr)) :
        if x<len(arr) and y<len(arr) :
            #print("x", arr[x])
            #print("y", arr[y])
            if (arr[x]+arr[y])%n == 0 :
                k = k+1
            #print("k", k)
            
print(k)