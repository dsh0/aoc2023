import numpy as np
shapes={"F":(1,1),"J":(-1,-1),"7":(1,-1),"L":(-1,1)}
A=np.array([[*x] for x in open("10.txt").read().split()])
x,y=(t[0] for t in np.where(A=='S'))
print(f"{x=},{y=}")
