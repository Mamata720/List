elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
y=[]
k=[]
while i<len(elements):
    b=elements[i]
    if b%2==0:
        y.append(b)
    else:
        k.append(b)
    i=i+1
print("even:",y)
print("odd:",k)
