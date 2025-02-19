import math
class PhanSo:
    def __init__(self,t,m):
        self.t = t
        self.m = m
    
    def rutgon(self):
        chung = math.gcd(self.t,self.m)
        self.t = int(self.t / chung)
        self.m = int(self.m / chung)
    def tong(self,x):
        tu = self.t * x.m + self.m * x.t
        mau = self.m * x.m
        self.t = tu
        self.m = mau
    def In(self):
        print(self.t, "/",self.m,sep ="")

a,b,c,d = [int(x) for x in input().split()]
ps1 = PhanSo(a,b)
ps2 = PhanSo(c,d)

ps1.tong(ps2)
ps1.rutgon()
ps1.In()