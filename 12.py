import numpy as np
# solution by Dynamic Programming
# vec[ii,jj] == number of assigments of the '?'s in pat[::ii], 
# that has '#' sequence == seq[::jj], and ends with '.'
# the artificial extra condition "ends with '.'" is meant for the recursive formula to work

ls=open("12.txt").read().splitlines()
res=0
for l in ls:
    pat,seq=l.split()
    pat="?".join([pat]*5) # part B only
    pat+="." # neccesary in order not to miss solutions where pat[-1]=='#'
    seq=np.fromstring(seq,dtype=int,sep=',')
    seq=np.tile(seq,5) # part B only
    vec=np.zeros((len(pat)+1, len(seq)+1),dtype=int)
    vec[0,0]=1
    for ii,c in enumerate(pat):
        # in the ii'th iteration we compute vec[ii+1,:]
        if c=='#': 
            continue # in that case pat[::ii] cannot end with '.' so vec[ii+1,:]=0
        vec[ii+1]+=vec[ii] #  counts solutions where pat[ii]=='.' && pat[ii-1]=='.' after assignments of ?s
        for jj,l in enumerate(seq):
            if '.' not in pat[ii-l:ii]:
                vec[ii+1,jj+1]+=vec[ii-l,jj] #  counts solutions where pat[ii]=='.' && all(pat[ii-l:ii]=='#')
    res+=vec[-1,-1]
print(res)
