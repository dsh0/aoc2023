import numpy as np
A=[*open("21.txt")]
# A is 131x132, start at (65,65)
visited=np.full((131,132),False)
l=[(65,65)]
for _ in range(65):
    l2=[]
    for x,y in l:
        if A[x][y]!='#' and not visited[x,y]:
            visited[x,y]=True
            l2+=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    l=l2[:]
checkmarks = (1+np.arange(132)+np.arange(131)[:,np.newaxis])%2
print((visited*checkmarks).sum())