n = input()
arr1 = sorted(set(map(int,input().strip().split())))
m = int(input())
arr2 = list(map(int,input().strip().split()))
i=0
j=0
while i<len(arr2) :
    while j<len(arr1) :
        if arr2[i]<arr1[j] :
            print(len(arr1)-j+1)
            break
        elif arr2[i]>=arr1[len(arr1)-1] :
            print("1")
            break
        j = j+1
    i = i+1