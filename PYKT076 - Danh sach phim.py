class Movie:
    def __init__(self,id,theloai,date,ten,tap):
        if (id < 10):
            self.ma = "P00" + str(id)
        elif (id < 100):
            self.ma = "P0" + str(id)
        else:
            self.ma = "P" + str(id) 
        self.theloai = theloai
        self.date= date
        self.ngay = date[:2]
        self.thang = date[3:5]
        self.nam = date[6:]
        self.ten = ten
        self.tap = tap
    
    def info(self):
        print(self.ma,self.theloai,self.date,self.ten,self.tap)
n , m = [int(x) for x in input().split()]
ls = []
ls_the_loai = []
for i in range(n):
    x = input()
    ls_the_loai.append(x)

for i in range(m):
    ma_the_loai = input()
    date = input()
    ten = input()
    tap = int(input())
    idx = int(ma_the_loai[2:]) - 1
    theloai = ls_the_loai[idx]
    ls.append(Movie(i+1,theloai,date,ten,tap))
ls = sorted(ls, key = lambda x : (x.nam, x.thang, x.ngay, x.ten, -x.tap))
for i in ls:
    i.info()