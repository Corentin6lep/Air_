
def n(u):

    for j in range(0,len(u)):
        for i in range(0,len(u)):
            if u[j]<u[i]:
                a=u[j]
                u[j]=u[i]
                u[i]=a
                
            print(u)

n([6,5,4,3,2,1])

