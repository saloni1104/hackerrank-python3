n = int(input())
p = int(input())
start = 1
end = 0
if p == 1 or p == n:
    print("0")
else :
    for i in range (2,n,2) :
        #print("i", i)
        if p == i or p == i+1 :
            #print("break")
            break
        elif p != i or p != i+1 :
            start = start+1
            #print("start1", start)
    if n%2 == 0 :
        for j in range (n+1,1,-2) :
            #print("j", j)
            if p == j or p == j-1 :
                #print("break1")
                break
            elif p != j or p != j-1 :
                end = end+1
                #print("end1", end)
    else :
        for j in range (n,1,-2) :
            #print("j", j)
            if p == j or p == j-1 :
                #print("break1")
                break
            elif p != j or p != j-1 :
                end = end+1
                #print("end1", end)
    if start<end :
        print(start)
    else :
        print(end)