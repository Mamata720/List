a=[1,-2,3,-4,5,-5,6,-7,8,-9]
i=0
b=[]
while i<len(a):
    c=a[i]
    if a[i]<0:
        print(a[-i]*0)
    else:
        print(a[i])
        b.append(c)
    i=i+1