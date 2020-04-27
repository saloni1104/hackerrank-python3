n = int(input())
score = input().split()
for i in range (0,len(score)) :
    score[i] = int(score[i])
min = score[0]
max = score[0]
min1 = 0
max1 = 0
for j in range (1,len(score)) :
    if score[j]<min :
        min = score[j]
        min1 = min1+1
    elif score[j]>max :
        max = score[j]
        max1 = max1+1
print(str(max1) +" "+ str(min1))