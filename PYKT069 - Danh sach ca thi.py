from datetime import datetime

class CaThi:
    def __init__(self, stt, ngay, gio, phong):
        self.ma = "C{:03d}".format(stt)
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
        self.thoigian = datetime.strptime(ngay + " " + gio, "%d/%m/%Y %H:%M")

    def output(self):
        print(self.ma, self.ngay, self.gio, self.phong)

# Đọc file
with open("e:/Python_PE/CATHI.in") as file:
    t = int(file.readline())
    a = []
    for i in range(t):
        ngay = file.readline().strip()
        gio = file.readline().strip()
        phong = file.readline().strip()
        a.append(CaThi(i + 1, ngay, gio, phong))

a.sort(key=lambda x: (x.thoigian, x.ma))

for i in a:
    i.output()
