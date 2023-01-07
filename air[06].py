def u(n,w):
    for i in range (0, len(n)):
        if w not in n[i] and w.upper() not in n[i]:
            print(n[i])

u(["Michel","Albert","Therese", "Benoit"],'t')