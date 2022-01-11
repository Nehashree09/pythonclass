class hello:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
p=hello()
p.add(1,2,0)    


#class welcome:
 #   result =0
  #  def ad(self,instanceof=None,*args):
   #     if instanceof=='int':
    #        self.result=0
     #   if instanceof=='str':
      #      self.result=''
       # for i in args:
        #    self.results=self.result+1
        #return self.result
#o1=welcome()
#print (o1.ad('int',1,2,3)) 
#print(o1.ad('str','this','useless','existiance'))

#operation overloading

class Addovloding:
    def __init__(self,x):
        self.x=x

    def __addi__(self,other):
        print('the value of ob1=',self.x)
        print('the value of ob2=',other.x)
        print('addiyion of two obj:=',end='')
        return((self.x+other.x))
ob1=Addovloding(5)
ob2=Addovloding(10)
#ob3=ob1+ob2
#print(ob3)


#method overriding
class ABC:
    i=0
    def display(self):
        print('ecchi method')
class BCD(ABC):
    i=0
    def display(self):
        print('ni method')

ob6=BCD()
ob6.display()


#resolved
class ABC:
    i=0
    def display(self):
        print('ecchi method')
class BCD(ABC):
    i=0
    def display(self):
        print('ni method')
        super.display()
ob6=BCD()
ob6.display()

        
        