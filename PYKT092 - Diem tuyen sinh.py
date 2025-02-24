class Diem:
    def __init__(self,stt,ten,diem,dt,kv):
        self.id = f"TS{stt:02d}"
        self.ten = ten
        self.diem = diem

        if kv == 1:
            self.diem += 1.5
        elif kv == 2:
            self.diem += 1
        else: self.diem += 0
        
        if dt != "Kinh":
            self.diem += 1.5

        if self.diem >= 20.5: self.tt = "Do"
        else: self.tt = "Truot"
    def info(self):
        print(self.id,self.ten,self.diem,self.tt)
    
def ChuanHoa(s):
    xau = ""
    xau += s[0].upper()
    for i in range(1,len(s)):
        xau += s[i].lower()
    return xau

a = []
for i in range(0,int(input())):
    ten = input().split()
    diem = float(input())
    dt = input()
    kv = int(input())
    tenCH = ""
    for word in ten:
        tenCH += ChuanHoa(word)
        tenCH += " "
    a.append(Diem(i + 1, tenCH.strip(), diem, dt, kv))
a = sorted(a,key = lambda x: -x.diem)
for i in a:
    i.info()
