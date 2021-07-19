num=input("enter something as your wish:")
i=0
while i<len(num):
    if num[i]==" ":
        num=num[:i] + num[i+1:]
    else:
        i=i+1
print(num)