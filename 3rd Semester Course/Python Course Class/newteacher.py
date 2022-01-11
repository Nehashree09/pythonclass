a=float(input('enter the weight in pound')) * 0.45359237
b=float(input('enter the height in inches'))*0.0254
bmi=a/b*b
print(bmi)
if (bmi>=18.5 and bmi<=24.9):
    print('ideal')
elif(bmi>=25 and bmi<=29.9):
    print('overweight')
else:
    print('non')