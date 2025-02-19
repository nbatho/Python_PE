import math
class PhanSo:
    def __init__(self,t,m):
        self.t = t
        self.m = m
    def rutgon(self):
        chung = math.gcd(self.t,self.m)
        self.t = int(self.t / chung)
        self.m = int(self.m / chung)
    def output(self):
        print(self.t,'/',self.m,sep ="")

tu,mau = [int(x) for x in input().split()]
ps = PhanSo(tu,mau)
ps.rutgon()
ps.output()