class Luong:
    def __init__(self,ma,ten,phong_ban,pl,nam,cong,lcb):
        self.ma = ma
        self.ten = ten
        self.phong_ban = phong_ban
        self.pl = pl
        self.hs = self.gt_bang(self.pl)
        if nam >= 1 and nam <= 3:
            hsn = self.hs[0]
        elif nam >= 4 and nam <= 8:
            hsn = self.hs[1]
        elif nam >= 9 and nam <= 15:
            hsn = self.hs[2]
        else: hsn = self.hs[3]

        self.luong = lcb*cong*hsn*1000

    def gt_bang(self,pl):
        if pl == "A":
            a = 10
            b = 12
            c = 14
            d = 20
        elif pl == "B":
            a = 10
            b = 11
            c = 13
            d = 16
        elif pl == "C":
            a = 9
            b = 10
            c = 12
            d = 14
        elif pl == "D":
            a = 8
            b = 9
            c = 11
            d = 13
        return a,b,c,d
    def output(self):
        print(self.ma,self.ten,self.phong_ban,self.luong)
so_phong_ban = int(input())
ls = []
for _ in range(so_phong_ban):
    s = input().split()
    ma_phong = s[0]
    ten_phong = ""
    for i in range(1,len(s)-1):
        ten_phong += s[i] + " "
    ten_phong += s[len(s)-1]
    ls.append((ma_phong,ten_phong))

so_nhan_vien = int(input())
ans = []
for _ in range(so_nhan_vien):
    ma_nv = input()
    pl = ma_nv[0]
    nam = ma_nv[1:3]
    ma_phong_ban = ma_nv[3:]
    ten_nv = input()
    lcb = input()
    cong = input()
    for i in ls:
        if ma_phong_ban == i[0]:
            phong_ban = i[1]
    ans.append(Luong(ma_nv,ten_nv,phong_ban,pl,int(nam),int(cong),int(lcb)))


for i in ans:
    i.output()