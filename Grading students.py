n = int(input())
a = []
while n>0 :
    original = int(input())
    if original<38 :
        a.append(str(original))
    elif original%5 == 0 :
        a.append(str(original))
    elif original%5 == 2 :
        a.append(str(original))
    elif original%5 == 1 :
        a.append(str(original))
    elif original%5 == 3 :
        a.append(str(original+2))
    elif original%5 == 4 :
        a.append(str(original+1))
        
    n = n-1
    
def convert(list) :
    return '\n'.join(list)
print(convert(a))