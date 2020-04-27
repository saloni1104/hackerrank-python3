b,n,m = input().split()
b = int(b)
kb = input().split()
for i in range (0,len(kb)) :
    kb[i] = int(kb[i])
usb = input().split()
for j in range (0,len(usb)) :
    usb[j] = int(usb[j])
sum = 0
max = 0
for x in range (0,len(kb)) :
    for y in range (0,len(usb)) :
        sum = kb[x] + usb[y]
        if sum<=b and sum>max :
            max = sum
if max>0 :
    print(max)
else :
    print("-1")