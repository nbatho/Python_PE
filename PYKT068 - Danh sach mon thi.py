class MonThi:
    def __init__(self,ma,ten,hinhthuc):
        self.ma = ma
        self.ten = ten
        self.hinhthuc = hinhthuc
    
    def info(self):
        print(self.ma,self.ten,self.hinhthuc)


a = []
for _ in range(int(input())):
    ma = input()
    ten = input()
    hinhthuc = input()
    a.append(MonThi(ma,ten,hinhthuc))

a = sorted(a,key = lambda x: x.ma)

for i in a:
    i.info()
