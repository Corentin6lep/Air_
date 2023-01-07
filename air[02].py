def u(*argv,b):
    B=[]
    C=""
    for x in argv:
        B.append(x)
         
    for i in range(0, len(argv)):
        C=C+B[i]
        C=C+b
    print(C)
    
u('comment','ca','va', b=" ")