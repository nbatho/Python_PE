import math
tc = int(input())
for i in range (0, tc):
    n , x , m = map(float,input().split())
    # m = n*(1 + x%)^i

    res = math.log(m/n , 1 + x/100)
    print(int(res) + 1)
