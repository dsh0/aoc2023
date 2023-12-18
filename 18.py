xy,L,A=[0,0],0,0
for l in open("18.txt"):
    # part A:
    ## steps=int(l[2:-11]) * (1 if l[0] in "DR" else -1)
    ## dim=0 if l[0] in "UD" else 1
    # part B:
    steps=int(l[-8:-3],16) * (1 if l[-3] in "01" else -1)
    dim=0 if l[-3] in "13" else 1
    L+=abs(steps)
    A+=dim*xy[0]*steps
    xy[dim]+=steps

print(abs(A)+L//2+1)