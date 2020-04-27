s = list(input())
total_stuart = 0
total_kevin = 0
for i in range(len(s)) :
    if s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U' :
        total_kevin = total_kevin+len(s)-i

for i in range(len(s)) :
    if s[i] != 'A' and s[i] != 'E' and s[i] != 'I' and s[i] != 'O' and s[i] != 'U' :
        total_stuart = total_stuart+len(s)-i

if total_kevin>total_stuart :
    print("Kevin" , total_kevin)
elif total_kevin == total_stuart :
    print("Draw")
else :
    print("Stuart" , total_stuart)