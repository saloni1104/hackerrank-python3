if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    for j in range(0,len(arr)) :
        arr[j] = int(arr[j])
    arr.sort()
    max = arr[0]
    next_max = 0
    for i in range(1,len(arr)) :
        if arr[i]>max :
            next_max = max
            max = arr[i]
    print(next_max)