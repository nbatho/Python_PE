a , K , N = map(int,input().split())
#cong thuc tim so b dau tien
b = (K - (a%K))% K
flag = False
for i in range(b,N-a + 1 , K):
    if (i > 0):
        flag = True
        print(i, end = " ")

if (flag == False): print(-1)

