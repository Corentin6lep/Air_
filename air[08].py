def fusion(n,v):
    for i in v:
        n.append(i)
    
    for i in range(0,len(n)):
        for j in range(0,len(n)):
            if n[j]>n[i]:
                a=n[i]
                n[i]=n[j]
                n[j]=a
    print(n)

fusion([10,20,30,40,50,60,70,90],[33,4])