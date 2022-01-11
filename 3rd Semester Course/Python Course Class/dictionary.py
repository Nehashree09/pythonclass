dict={'india':'delhi','china':'beijing'}
for x in dict:
    print(x,end=",")

first ={0:'hello',1:'こんにちは',2:'안녕'}
print(first[1])
print(first.get(2))
first[0]='你好'
print(first)
first[4]='สวัสดี'
print(first)
#first.clear()
#print(first)
#coping to another variable
b=first.copy
print (b)
print(first.values())
#get all the keys
print(first.keys())
#converting to list
print(first.items())
print(first.pop(4))
