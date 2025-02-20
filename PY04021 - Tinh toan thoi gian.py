class Time:
    def __init__(self,ma,ten,vao,ra):
        self.ma = ma
        self.ten = ten

        
        self.TimeLeft = (int(ra[0])*60 + int(ra[1])) - (int(vao[0])*60 + int(vao[1]))
        self.gio = self.TimeLeft // 60
        self.phut = self.TimeLeft % 60
        self.TGchoi = str(self.gio) + " gio " + str(self.phut) + " phut "
    def info(self):
        print(self.ma,self.ten,self.TGchoi)        

a = []
for _ in range(int(input())):
    ma = input()
    ten = input()
    vao = input().split(":")
    ra = input().split(":")
    a.append(Time(ma,ten,vao,ra))

a = sorted(a,key = lambda x : x.TimeLeft,reverse= True)
for i in a:
    i.info()
