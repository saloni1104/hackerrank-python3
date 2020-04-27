s = list(input())
k = int(input())
n = len(s)/k
a=[]
b=[]
#while n>0 :
for i in range (0,len(s),k) :
       #print("i", i)
       if i<=len(s)-k :
           for j in range(i,i+k) :
               #print("j1", j)
               if j<len(s) :
                   if s[j] in a :
                       continue
                   else :
                       a.append(s[j])
                       #print("s[j]", s[j])
               #print("a", a)
           b.append(''.join(a))
           #print("b", b)
           a=[]
   
print('\n'.join(b))