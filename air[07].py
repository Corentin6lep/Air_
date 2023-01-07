def u(n,v):
    n.append(v)
    for i in range(0,len(n)):
        for j in range(0,len(n)):
            if n[j]>n[i]:
                a=n[i]
                n[i]=n[j]
                n[j]=a
    print(n)

u([10,20,30,40,50,60,70,90],33)