def u(n):
    a=n[0]
    b=n[1]
    n[0]=b

    for i in range(1,len(n)-1):
        b=n[i+1]
        n[i]=n[i+1]
        n[i+1]=b

    n[len(n)-1]=a

    print(n)

u(["Michel","Albert","Therese","Benoit","Thomas","Louis"])
