n = int(input())
s = input()
s1 = s.split(' ')
for i in range(0,len(s1)) :
    s1[i] = int(s1[i])
#print(s1)
N = 0
i = 0
while n>0 :
    #for i in range (0,len(s1)) :
        if (i+2)<len(s1) and s1[i+2] == 0:
            #if s1[i+2] == 0 :
                N = N+1
                #print("N1", N)
                i = i+2
                #print("i1",i)
        elif (i+1)<len(s1) and s1[i+1] == 0:  
            #if s1[i+1] == 0 :
                N = N+1
                #print("N2", N)
                i = i+1
                #print("i2",i)
            
        n = n-1
print(N)