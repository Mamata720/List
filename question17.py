num=[10,20,30,40]
num1=[100,200,300,400]
i=0
while i<len(num):
    a=1
    while a<=len(num1):
        print(num[i],num1[-a])
        a=a+1
        i=i+1