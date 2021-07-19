name=['snowball','cheway','bubbles','gruff']
animal=['cat','dog','fish','goat']
age=[1,2,2,6]
i=0

b=" "
while i<len(name):
    k=(name[0]+b+"the"+b+animal[0]+b+"is"+b+str(age[0]))
    n=(name[1]+b+"the"+b+animal[1]+b+"is"+b+str(age[1]))
    l=(name[2]+b+"the"+b+animal[2]+b+"is"+b+str(age[2]))
    m=(name[3]+b+"the"+b+animal[3]+b+"is"+b+str(age[3]))
    i=i+1
print(k)
print(n)
print(l)
print(m)
