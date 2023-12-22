import numpy as np
import queue

def calc_distances(A,sources):
    q=queue.Queue()
    dist=np.where(A==".",-1,-2) 
    lx,ly=A.shape
    for x,y in sources:
        q.put((x,y,0))
        dist[x,y]=0
    while q.qsize():
        x,y,v=q.get()
        for x0,y0 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=x0<lx and 0<=y0<ly and dist[x0,y0]==-1:
                dist[x0,y0]=v+1
                q.put((x0,y0,v+1))
    return dist

A=np.array([[*row[:-1]] for row in open("21.txt")])
# A.shape==(131,131), A[65,65]=='S', first/middle/last row & columns are free. The thick obstacle-free diamond has not apparent value.
# WARNING: A has an unreachable points ((98, 9), (100, 63), (102, 99), (128, 8) for my personal input), be careful!

# part A
t=calc_distances(A,[(65,65)])
print(((0<=t)&(t<=64)&(t%2==0)).sum())

# part B
total_steps=26501365
B=202300
L=len(A)
assert(B*L + L//2 == total_steps) # making sense of the seemingly random number 26501365
t2=calc_distances(A,[(0,0),(0,L-1),(L-1,0),(L-1,L-1)])
# print("unreachable points:",[*zip(*np.where(t==-1))]) 
even,odd = (((0<=t)&(t%2==x)).sum() for x in [0,1])
substract = ((t%2==1)*(65<t)).sum()
add = ((0<=t2)&(t2<=64)&(t2%2==0)).sum()
result = even*B**2 + odd*(B+1)**2 - (B+1)*substract + B*add
print(result)