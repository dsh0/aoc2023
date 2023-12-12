import numpy as np
ls=open("12.txt").read().splitlines()
res=0
for l in ls:
    pat,seq=l.split()
    pat="?".join([pat]*5) # part B only
    pat+="."
    seq=np.array([int(x) for x in seq.split(',')])
    seq=np.tile(seq,5) # part B only
    vec=np.zeros((len(pat)+1, len(seq)+1),dtype=int)
    vec[0,0]=1
    for ii,c in enumerate(pat):
        if c=='#': 
            continue
        vec[ii+1]+=vec[ii]
        for jj,l in enumerate(seq):
            if '.' not in pat[ii-l:ii]:
                vec[ii+1,jj+1]+=vec[ii-l,jj]
    res+=vec[-1,-1]
print(res)
