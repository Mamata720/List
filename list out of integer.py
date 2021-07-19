a=[1,2,3,"12a","13s",12,"sd"]
i=0
b=[]
while i<len(a):
    if type(a[i])==type(i):
        b.append(a[i])

    i=i+1
print(b)
