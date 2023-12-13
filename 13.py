from collections import defaultdict
from itertools import combinations
total = 0
for block in open("13.txt").read().split('\n\n'):
    A = block.split()
    AT = [''.join(y) for y in zip(*A)] # A transposed
    for M,factor in ((A,100),(AT,1)):
        collisions = defaultdict(list) # collisions['..#.##']==[1,3,4] means rows 1,3,4 are all '..#.##' 
        for ii,row in enumerate(M):
            collisions[row].append(ii)
        sums = defaultdict(lambda: 0) # sum[x] will be the number of identical rows ii,jj with ii==x-1-jj
        for indices_with_same_row in collisions.values():
            for ii,jj in combinations(indices_with_same_row,2):
                sums[ii+jj+1]+=1
        for sum, count in sums.items():
            if 2*count==min(sum,2*len(M)-sum):
                total+=factor*sum
print(total//2)
