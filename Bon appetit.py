n,k = input().split()
k = int(k)
bill = input().split()
for i in range (0,len(bill)) :
    bill[i] = int(bill[i])
bill.remove(bill[k])
x = 0
for j in range(0,len(bill)) :
    x = x+bill[j]
actual = int(input())
if x/2 == actual :
    print("Bon Appetit")
else :
    print(int(actual - (x/2)))