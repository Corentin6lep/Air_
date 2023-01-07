def n(u,v):
    w=v*[""]
    z=v*[u]

    for i in range(1,v):
        w[v-i]=u
        print(' '.join(str(j) for j in w))

    print(' '.join(str(j) for j in z))

n(5,15)