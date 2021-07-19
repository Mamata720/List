a=[2,3,4,5,6,7,8,9,10]
i=1
n=a[0]
k=[]
while i<len(a):
    s=a[i]
    j=s-n
    k.append(j)
    n=s
    i=i+1
print(k)