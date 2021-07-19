num=[[7,9,20],[22,28,8],[40,7,8]]
i=0 
while i<len(num):
    j=0
    k=num[i][0]
    while j<len(num[i]):
        if num[i][j]>k:
            k=num[i][j]
            
        j=j+1
    i=i+1
    print(k)