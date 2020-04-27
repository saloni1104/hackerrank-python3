n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
a = 0
if k<arr[len(arr)-1] :
    a = arr[len(arr)-1]-k
print(a)