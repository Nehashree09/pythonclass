class A:
    print("welcome")
class B(A):
    print("to python")
obj2=B()    

#simple inheritance 
class Point:
    def Set_cordinates(self,x,y):
        self.x=x
        self.y=y
class Newpoint(Point):
    def draw(self):
      print('locate x point x= ',self.x)
      print('locate y point y= ',self.y)
bo3=Newpoint()
bo3.Set_cordinates(5,15)
bo3.draw()

#multilevel inhheritance
class E:
    name=''
    age=0
class F(E):
    height =''
class G(F):
    weight=''

    def Read(self):
      print('please enter the following values')
      self.name=(input('enter name '))
      self.age=(int(input('enter age ')))
      self.height=(input('enter height '))
      self.weight=(input('enter weight '))
    def Display(self):
        print('the input values are as followes')
        print('name is ',self.name)
        print('age is ',self.age)
        print('height is ',self.height)
        print('weight is ',self.weight)

ob4=G()
ob4.Read()
ob4.Display()


#multiple inheritance
class A:
    a=0
class B:
    b=0
class C(A,B):
    c=0

    def read(self):
        self.a=(int(input('enter value for a: ')))
        self.b=(int(input('enter value for b: ')))
        self.c=(int(input('enter value for c: ')))

    def display(self):
        print('a= ',self.a)
        print('b= ',self.b)
        print('c= ',self.c)


ob5=C()
ob5.read()
ob5.display()        