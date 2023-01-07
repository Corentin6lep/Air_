def u(A,B):
    for i in range(0,len(A)):
        
        del B[i]
        for j in range(0,len(A)):
            if A[i] not in B:
                c=A[i]
            
        B.insert(i,A[i])
    print(c)

u(['bonjour','monsieur','bonjour'],['bonjour','monsieur','bonjour'])