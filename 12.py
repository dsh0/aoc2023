import numpy as np
# solution by Dynamic Programming
# vec[ii,jj] == number of assigments of the '?'s in pat[::ii] whose '#'-sequence is seq[::jj]
# after assignment of '?'s there are 2 options:
#  (1) line 22 - the last character is '.', the rest of the string has '#'-sequence seq[::jj]
#  (2) line 25 - the last character is '#' - in this case it must end with '.#####' (with seq[jj-1] '#'s, 5 is just an example), and before that it has '#'-sequence seq[::jj-1]

ls=open("12.txt").read().splitlines()
def solve(ls):
    res=0
    for l in ls:
        pat,seq=l.split()
        pat="?".join([pat]*5) # part B only
        seq=np.fromstring(seq,dtype=int,sep=',')
        seq=np.tile(seq,5) # part B only
        vec=np.zeros((len(pat)+1, len(seq)+1),dtype=int)
        vec[0,0]=1
        if '.' not in pat[:seq[0]]:
            vec[seq[0],1]=1 # this is a special case which line 26 doesn't address since there's no '.' before the first block of '#'s
        suff = 0
        for ii,c in enumerate(pat):
            suff+=1
            suff*= c!='.'
            # in the ii'th iteration we compute vec[ii+1,:]
            if c!='#': 
                vec[ii+1]+=vec[ii] #  counts solutions where pat[ii]=='.' after assignment of '?'s
            # TODO: vectorize with numpy the following loop
            for jj,l in enumerate(seq):
                if l<=suff and pat[ii-l]!='#': # if last l symbols can be '#':
                    vec[ii+1,jj+1]+=vec[ii-l,jj] #  counts solutions where pat[ii-l]=='.' && all(pat[ii-l+1:ii+1]=='#')
        res+=vec[-1,-1]
    return res
print(solve(ls))