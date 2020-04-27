y = int(input())
if y>=1700 and y<=1917 :
    if y%4 == 0 :
        print('12.09.%d' %(y))
    else :
        print ('13.09.%d' %(y))
elif y>1918 :
    if y%400 == 0 or (y%4 == 0 and y%100 !=0):
        print ('12.09.%d' %(y))
    else :
        print ('13.09.%d' %(y))
elif y == 1918 :
    print('26.09.1918')