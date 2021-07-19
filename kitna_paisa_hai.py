kitna_paisa_hai=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
i=0
x=[]
y=[]
z=[]
while i<len(kitna_paisa_hai):
     if kitna_paisa_hai [i]>=10000000:
         x.append(kitna_paisa_hai[i])
     elif kitna_paisa_hai [i]>=1000000:
        y.append(kitna_paisa_hai[i])
     else:
        z.append(kitna_paisa_hai[i])
     i=i+1
print("crorepati hai",x)
print("lakhpati hai",y)
print("dilwale hai",z)