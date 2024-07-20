import random
x=random.randint(1,50)

print(x)
y=eval(input('請猜一個數字'))
if x==y:
    print('bingo')
else:
    print('oops! do it agin ')
