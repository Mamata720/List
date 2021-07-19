char_list=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
i=0
y=[]

while i<len(char_list):
    j=0
    count=0
    a=[]
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count=count+1
        j=j+1
    a.append(char_list[i])
    a.append(count)
    if a not in y:
        y.append(a)
    i=i+1
print(y)