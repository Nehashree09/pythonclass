import math
class Circle:
    def __init__(self,radius=1):
        self.radius=radius
    def getpara(self):
        return 2*self.radius*math.pi
    def getarea(self):
        return self.radius*self.radius*math.pi
    def setradius(self,radius):
        self.radius=radius
#creating an object
c=Circle(5)
print(c.radius)
print(c.getpara())
print(c.getarea())
c1=Circle(20)
print(c1.radius)
print(c1.getpara())
print(c1.getarea())

class Triangle:
    def __initi__(self,l1=1,l2=1,l3=1):
        self.l1=l1
        self.l2=l2
        self.l3=l3
    def getparam(self):
        return self.l1+self.l2+self.l3
    def lenghts(self):
        return self.l1, self.l2, self.l3
t=Triangle(2,3,4)
print(t.getparam())