from heapq import heappop,heappush
import numpy as np

def dijkstra(A,min_steps,max_steps):
    L=len(A)
    visited=np.full((L,L,2),False)
    heap=[(0,(0,0,0)),(0,(0,0,1))] # starting position & direction
    while True:
        val,(*xy,dim)=heappop(heap)
        if visited[*xy,dim]:
            continue
        visited[*xy,dim]=True
        if xy==[L-1,L-1]:
            return val
        for dir in (1,-1): # dir = direction (+ or -)
            xy0,val0=[*xy],val
            for ii in range(1,max_steps+1):
                xy0[dim]+=dir
                if min(xy0)<0 or max(xy0)>=L:
                    break
                val0+=int(A[xy0[0]][xy0[1]])
                if ii>=min_steps and not visited[*xy0,1-dim]:
                    heappush(heap,(val0,(*xy0,1-dim)))

A=[*open("17.txt")]
print(dijkstra(A,1,3),dijkstra(A,4,10))