class hinhchunhat(object):
    def __init__(self,d,r):
        self.dai=d
        self.rong=r
    def area(self):
        return self.dai*self.rong

d=int(input("chieu dai:"))
r=int(input("chieu rong:"))
dientichHCN=hinhchunhat(d,r)
print("dien tich hinh chu nhat:",dientichHCN.area())