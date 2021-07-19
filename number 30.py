n=[10,11,12,13,14,17,18,19]
number=30
i=0
y=[]
while i<len(n):
    j=0
    while j<len(n):
        if n[i]+n[j]==number:
            k=([n[i],n[j]])
            y.append(k)
        j=j+1
        
    i=i+1
print(y)
