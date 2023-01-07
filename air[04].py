def u (n):
    C=[]
    D=[]
    for i in n:
        C.append(i)
        
    j=0

    for i in range(0,len(C)-1):
        if C[i] != C[i+1]:
            D.append(C[i])
        else:
            j=j+1
    print("".join(D))


u("Hello miilady,  bien ou quoii ??")
