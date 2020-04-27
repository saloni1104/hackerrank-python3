if __name__ == '__main__':
    a = []
    b=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        a.append(name)
        a.append(score)
    #print(a)
    min = a[1]
    if a[3] != min :
        next_min = a[3]
    else:
        for i in range (3,len(a),2) :
            if a[i] != min :
                next_min = a[i]
    for j in range(3,len(a),2) :
        if a[j]<min :
            next_min = min
            min = a[j]
        elif a[j]<next_min and a[j]>min :
            next_min = a[j]
        elif a[j] == min :
            continue
    for k in range(0,len(a)) :
        if a[k] == next_min :
            b.append(a[k-1])
    c=sorted(b)
    print('\n'.join(c))