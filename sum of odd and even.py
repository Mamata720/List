a=[23,14,56,12,19,9,15,25,31,42,43]
i=0
y=[]
k=[]
sum=0
s=0
while i<len(a):
    b=a[i]
    if b%2==0:
        y.append(b)
        sum=sum+b
    else:
        k.append(b)
        s=s+b
    i=i+1
print("even:",y,"sum:",sum)
print("odd:",k,"sum:",s)
