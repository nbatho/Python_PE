for _ in range(int(input())):
    a, b, c, d = [int(x) for x in input().split()]
    thucC = a*a + a*c - b*b - b*d 
    aoC = a*b + b*c + a*b + a*d 
    thucD = (a + c)*(a + c) - (b + d)*(b + d)
    aoD = 2*(a + c)*(b + d)
    print(thucC, end = '')
    if aoC > 0 :print(' + ',end ='')
    else: print(' - ',end ='')
    print(abs(aoC),'i',sep ='',end ='')
    print(',',thucD,end ='')
    if aoD > 0 :print(' + ',end ='')
    else: print(' - ',end ='')
    print(abs(aoD),'i',sep ='')

