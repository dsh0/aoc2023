import numpy as np
total = 0
for block in open("13.txt").read().split('\n\n'):
    A = np.array([[*row] for row in block.split()])
    for M,factor in ((A,100),(A.transpose(),1)):
        l = M.shape[0]
        for ii in range(1,l):
            B = M[:2*ii] if 2*ii<l else M[2*(ii-l):]
            if (B!=B[::-1]).sum()==2: # 0 for part A, 2 for part B
                total+=factor*ii
print(total)