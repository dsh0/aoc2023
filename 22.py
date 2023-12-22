import numpy as np
import re
pat = r"(\d+),(\d+),(\d+)\~(\d+),(\d+),(\d+)\n"
A=np.array([re.fullmatch(pat,row).groups() for row in open("22.txt")]).astype(int)
zs=np.zeros((10,10),dtype=int)
zview=np.zeros((10,10),dtype=int)-1
support=np.full(len(A),False)

A=A[A[:,2].argsort()]
for ii,(x0,y0,z0,x1,y1,z1) in enumerate(A):
    window=zs[x0:x1+1,y0:y1+1]
    if max_height:=window.max():
        supps={zview[x,y] for x in range(x0,x1+1) for y in range(y0,y1+1) if zs[x,y]==max_height}
        if len(supps)==1:
            support[supps.pop()]=True
    zs[x0:x1+1,y0:y1+1]=max_height+z1-z0+1
    zview[x0:x1+1,y0:y1+1]=ii

print((~support).sum())