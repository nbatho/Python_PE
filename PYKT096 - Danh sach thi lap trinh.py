class ICPC:
    def __init__(self,mts,ten,team,truong):
        self.ma = "C{:03d}".format(mts)
        self.ten = ten
        self.team = team
        self.truong = truong
    def output(self):
        print(self.ma,self.ten,self.team,self.truong)

ans = []
so_team = int(input())
ls = []
for _ in range(so_team):
    ten_team = input()
    ten_truong = input()
    ls.append((ten_team,ten_truong))
so_thi_sinh = int(input())
for i in range(so_thi_sinh):
    ten = input()
    ma_team = input()
    hs = int(ma_team[4:])
    for j in range(len(ls)):
        if j == (hs-1):
            team = ls[j][0]
            truong = ls[j][1]
    ans.append(ICPC(i+1,ten,team,truong))
ans = sorted(ans,key= lambda x: x.ten)
for i in ans:
    i.output()