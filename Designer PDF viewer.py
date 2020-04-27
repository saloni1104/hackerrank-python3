import string
arr = list(map(int,input().split()))
s = list(input())
a = string.ascii_letters
i = 0
j = 0
Dict = {}
while i < len(arr) :
    
    Dict[a[i]] = arr[i]
    i = i+1
b =[]
while j < len(s) :
    if Dict[s[j]] :
        b.append(Dict.get(s[j]))
    j = j+1
b.sort()
print(len(s)*b[len(b)-1])