import math
class Circle(object):
  def __init__(self,R):
    self.bankinh=R
  def chuvi(self):
    return float(self.bankinh*2*math.pi)
  def dientich(self):
    return float(self.bankinh*self.bankinh*2*math.pi)
R=float(input("ban kinh hinh tron:"))
chuviHT=Circle(R)
dientichHT=Circle(R)
if R<=0:
    print("ban kinh khong hop le")
else:
    print("chu vi hinh tron:",chuviHT.chuvi())
    print("dien tich hinh tron:",dientichHT.dientich())