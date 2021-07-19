marks=[
    [78,76,94,86,88],
    [91,71,98,65],
    [95,45,78]
]
i=0
sum=0
while i<len(marks):
    j=0
    x=0
    while j<len(marks[i]):
        x=x+(marks[i][j])
        j=j+1
    sum=sum+x
    i=i+1
print(sum)