a=[23,14,56,12,19,15,25,31,42,43]
i=0
c=0
d=0
y=[]
k=[]
sum=0
sum1=0
while i<len(a):
    b=a[i]
    if b%2==0:
        y.append(b)
        sum=sum+b
        c=sum/len(y)
    else:
        k.append(b)
        sum1=sum1+b
        d=sum1/len(k)
    i=i+1
print("even avereage:",c)
print("odd avereage:",d)