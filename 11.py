import numpy as np
def total_dist(A, expansion):
    proj = np.array([A.sum(d) for d in (0,1)])
    cumsum=proj.cumsum(1)
    cumsum2=cumsum[0,-1]-cumsum
    factor=np.where(proj,1,expansion)
    return (factor*cumsum*cumsum2).sum()

A=np.array([[*x] for x in open("11.txt").read().splitlines()])=="#"
for exp in (2,1_000_000):
    print(total_dist(A,exp))
