def u(a,b):
    j=0
    
    C=[]
    G=[]
    F=[]
    for i in a:
        j=j+1
        if i == " ":
            C.append(j-1)
    print(a)        
    print(C)

    G.append(a[0:C[0]])

    for i in range (0,len(C)-1):
        G.append(a[C[i]:C[i+1]])

    G.append(a[C[len(C)-1]:])

    
    
    HP=[]
    HA=[]
    JP=["",""]
    j=0
    for i in range(0,len(G)):
        if G[i]==b:
            j=i

    for i in range(0,j):
        HP.append(G[i])  
    for i in range(j,len(G)):
        HA.append(G[i])
    
    for i in range(0,len(HP)):
        JP[0]=JP[0]+HP[i]

    
    for i in range(0,len(HA)):
        JP[1]=JP[1]+HA[i]
    
    for x in JP:
        print(x)

u("Bonjour les gars comment ça va ici il fait froid"," il")
