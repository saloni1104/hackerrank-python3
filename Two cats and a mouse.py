n = int(input())
output = []
for i in range (0,n) :
    x,y,z = input().split()
    x = int(x)
    y = int(y)
    z = int(z)
    a = abs(x-z)
    b = abs(y-z)
    if a>b :
        output.append("Cat B")
    elif b>a :
        output.append("Cat A")
    elif a==b :
        output.append("Mouse C")
def convert(list) :
    return "\n".join(list)
print(convert(output))