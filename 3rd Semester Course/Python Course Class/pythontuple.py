sid=()
print(type(sid))
ss="hello",
print(ss)
sss=(1,2,3,4,5)
print(sss[0],sss[2])
print(sss[:])
print(sss[::-1])
print(sss[1:])

list=[1,2,3,4]
tup=(1,2,3,4)
list.append(5)
print(list)

city=("Darjeeling","Jhapa")
pincode=(12345,34567)
print(city+pincode)

rep=("Nanami",)*3
print(rep)


tpl=(1,2,3,4)
print(tpl)
#del tpl
#print (tpl)
    

tpl2=(1,23,45,6,24,78,6)
print(tpl2)
a=max(tpl2)
b=min(tpl2)
print(a)
print(b)
c=tpl2.count(6)
print(c)
d=len(tpl2)
e=sum(tpl2)
print(d)
print(e)

#list to tuple
list1=[1,2,3,4]
print(type(list1))
tupl=tuple(list1)
print(tupl)
print(type(tupl))

#nesting tuples in a list
list2=[(1,2,3),(2,3,4)]
print(list2)

#add some values(append)
list2.append("a")
print(list2)
#removeing
list2.remove((1,2,3))
print(list2)

#nesting list in a tuple
ttpl=([1,2,3],[3,4,5])
print(ttpl)
ttpl[0].append('z')
print(ttpl)
ttpl[0].remove('z')
print(ttpl)