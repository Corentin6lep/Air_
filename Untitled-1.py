a="12 * ( 5 - 7 + 5 ) + 7 - 5 + 3 "
b=[]
c=[]
for i in range(0, len(a)):
    if a[i] == " ":
        c=a[i-2]+a[i-1]
        b.append(c)

d=[] #matrice comprenant les valeurs avec opérations dans les parenthèses
e=[] #matrice expression avant les parenthèses
z=[] #matrice expression après parenthèses
j=0
m=0
for i in range(0,len(b)):
    j=j+1
    if b[i]== " (":
        g=j
        while b[i] != " )":
            d.append(b[i])
            i=i+1
            m=m+1
del d[0]


for i in range(0,g):
    if b[i] != " (" :
            e.append(b[i])
            i=i+1

for i in range(m+2+len(e),len(b)):
    z.append(b[i])
    i=i+1



for i in range(0,len(d)-1):
    if (d[i] == " *" or d[i] == " /" or d[i] == " %" or d[i] == ' +' or d[i] == " -" ) :
        d[i-1]=int(d[i-1])
        d[i+1]=int(d[i+1])



for i in range(0,len(e)):
    if (e[i] == " *" or e[i] == " /" or e[i] == " %" or e[i] == ' +' or e[i] == " -" ) :
        e[i-1]=int(e[i-1])
      
for i in range(0,len(z)):
    if (z[i] == " *" or z[i] == " /" or z[i] == " %" or z[i] == ' +' or z[i] == " -" ) :
        z[i-1]=int(z[i-1])
        z[i+1]=int(z[i+1])

f=[]

if d[1]!= " *" and d[1] != " /" and d[1] != " %" :
        d[0]=int(d[0])
        f.append(d[0])

if d[len(d)-2]!= " *" and d[len(d)-2] != " /" and d[len(d)-2] != " %" :
        d[len(d)-1]=int(d[len(d)-1])
        f.append(d[len(d)-1])

for i in range(0,len(d)-2):
    if d[i] == " +" and d[i+2] != " *" and d[i+2] != " /" and d[i+2] != " %" :
        f.append(b[i+1])
    if d[i] == ' -' and d[i+2] != " *" and d[i+2] != " /" and d[i+2] != " %" :
        f.append(-d[i+1])

for i in range(2,len(d)):
    if d[i] == ' *' and d[i-2]!=" -":
        c=d[i-1]*d[i+1]
        f.append(c)

    if d[i] == ' *' and d[i-2]==" -":
        c=d[i-1]*d[i+1]
        f.append(-c)

    if d[i] == ' /' and d[i-2]!=" -":
        f.append(d[i-1] / d[i+1])
    if d[i] == ' /' and d[i-2]==" -":
        f.append(-d[i-1] / d[i+1])

    if d[i] == ' %' and d[i-2]!=" -":
        f.append((d[i-1] % d[i+1]))

    if d[i] == ' %' and d[i-2]==" -":
        f.append((-d[i-1] % d[i+1]))
    



l=[]
print(e)
if e[1]!= " *" or e[1] != " /" or e[1] != " %" :
        e[0]=int(e[0])
        l.append(e[0])

for i in range(0,len(e)):
    if e[i] == " +" and (e[i+2] != " *" or e[i+2] != " /" or e[i+2] != " %" ):
        l.append(e[i+1])
    if e[i] == ' -' and (e[i+2] != " *" or e[i+2] != " /" or e[i+2] != " %" ):
        l.append(-e[i+1])

if len(e)>2:    
    for i in range(2,len(e)):
        if e[i] == ' *' and e[i-2]!=" -":
            c=e[i-1]*e[i+1]
            l.append(c)

        if e[i] == ' *' and e[i-2]==" -":
            c=e[i-1]*e[i+1]
            l.append(-c)

        if e[i] == ' /' and e[i-2]!=" -":
            l.append(e[i-1] / e[i+1])
        if e[i] == ' /' and e[i-2]==" -":
            l.append(-e[i-1] / e[i+1])

        if e[i] == ' %' and e[i-2]!=" -":
            l.append((e[i-1] % e[i+1]))

        if e[i] == ' %' and e[i-2]==" -":
            l.append((-e[i-1] % e[i+1]))



v=[]

if z[1]!= " *" and z[1] != " /" and z[1] != " %" :
        z[0]=int(z[0])
        v.append(z[0])

if z[len(z)-2]!= " *" and z[len(z)-2] != " /" and z[len(z)-2] != " %" :
        z[len(z)-1]=int(z[len(z)-1])
        v.append(z[len(z)-1])



if len(z)>3:
    for i in range(0,len(z)-2):
        if z[i] == " +" and z[i+2] != " *" and z[i+2] != " /" and z[i+2] != " %" :
            v.append(z[i+1])
        if z[i] == ' -' and z[i+2] != " *" and z[i+2] != " /" and z[i+2] != " %"  or z[i+2]== " ":
            v.append(-z[i+1])
else:
    if z[1] == " +":
        v.append(z[2])
    if z[1] == ' -':
        v.append(-z[2])


for i in range(2,len(z)):
    if z[i] == ' *' and z[i-2]!=" -":
        c=z[i-1]*z[i+1]
        v.append(c)

    if z[i] == ' *' and z[i-2]==" -":
        c=z[i-1]*z[i+1]
        v.append(-c)

    if z[i] == ' /' and z[i-2]!=" -":
        v.append(z[i-1] / z[i+1])
    if z[i] == ' /' and z[i-2]==" -":
        v.append(-z[i-1] / z[i+1])

    if z[i] == ' %' and z[i-2]!=" -":
        v.append((z[i-1] % z[i+1]))

    if z[i] == ' %' and z[i-2]==" -":
        v.append((-z[i-1] % z[i+1]))

S1=0
for i in f:
    S1=S1+i

S2=0
for i in l:
    S2=S2+i
S3=0
for i in v:
    S3=S3+i

if e[len(e)-1] == " +" and b[m+1+len(e)] == " *":
    C1=S2*S3
    C1=C1+S1
    print(C1)
if e[len(e)-1] == " +" and b[m+1+len(e)] == " /":
    C1=S2/S3
    C1=C1+S1
    print(C1)
if e[len(e)-1] == " +" and b[m+1+len(e)] == " %":
    C1=S2%S3
    C1=C1+S1
    print(C1)
if e[len(e)-1] == " +" and b[m+1+len(e)] == " +":
    print(S1+S2+S3)
if e[len(e)-1] == " +" and b[m+1+len(e)] == " -":
    C1=S1+S2-S3
    print(C1)

if e[len(e)-1] == " -" and b[m+1+len(e)] == " *":
    C1=S1-S2*S3
    print(C1)
if e[len(e)-1] == " -" and b[m+1+len(e)] == " /":
    C1=S1-S2/S3
    print(C1)
if e[len(e)-1] == " -" and b[m+1+len(e)] == " %":
    C1=S1-S2%S3
    print(C1)
if e[len(e)-1] == " -" and b[m+1+len(e)] == " -":
    C1=S1-S2-S3
    print(C1)
if e[len(e)-1] == "-" and b[m+1+len(e)] == " +":
    C1=S1-S2+S3
    print(C1)
if e[len(e)-1] == " *" and b[m+1+len(e)] == " +":
    C1=S1*S2+S3
    print(C1)
if e[len(e)-1] == " *" and b[m+1+len(e)] == " *":
    C1=S1*S2*S3
    print(C1)
if e[len(e)-1] == " *" and b[m+1+len(e)] == " /":
    C1=S1*S2/S3
    print(C1)
print(f)
print(l)
print(v)

