n,m = input().split()
n = int(n)
m = int(m)
a = input().split()
for i in range(0,len(a)) :
    a[i] = int(a[i])
b = input().split()
for j in range(0,len(b)) :
    b[j] = int(b[j])
k = 0
z = 0
w = 0
while True :
    for l in range (max(a),min(b)+1) :
        #print("l", l)
        z = 0
        w = 0
        for x in range (0,len(a)) :
            if l%a[x] == 0 :
              z = z+1
        if z == len(a) :
            for y in range (0,len(b)) :
                if b[y]%l == 0 :
                    w = w+1
            if w == len(b) :
                k = k+1
                #print("k", k)
            
    break
        #break
            
    
    
print(k)