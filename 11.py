import numpy as np
def total_dist(proj,expansion=2):
    cumsum=proj.cumsum()
    cumsum2=proj.sum()-cumsum
    factor=np.where(proj,1,expansion)
    return (factor*cumsum*cumsum2).sum()

A=np.array([[*x] for x in open("11.txt").read().splitlines()])=="#"
print("A part:", total_dist(A.sum(0))+total_dist(A.sum(1)))
print("B part:", total_dist(A.sum(0),1e6)+total_dist(A.sum(1),1e6))