def u(n,w):
    v=[]
    
    if w[0] == "+":
        for i in n:
            v.append(i+int(w[1:]))

    if w[0] == "-":
        for i in n:
            v.append(i-int(w[1:]))
    print(v)

u([1,2,3,4,5],'+10')