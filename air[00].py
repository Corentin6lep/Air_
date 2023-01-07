def u(a,b):
    j=0
    C=[]
    for i in a:
        j=j+1
        if i in b:
            C.append(j-1)

    print(a[0:C[0]])

    for i in range (0,len(C)-1):
        print(a[C[i]:C[i+1]])

    print(a[C[len(C)-1]:])

u("Bonjour les gars comment ça va ici il fait froid"," ")