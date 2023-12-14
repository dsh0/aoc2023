import numpy as np
L=100
input = ['#'*L] + open("14.txt").read().split() + ['#'*L]
A=np.array([[*row] for row in input]).transpose() # transpose is needed since np.where results are ordered by rows
rocks=np.where(A=="#")
rolls=(A=="O").cumsum(1)[rocks]
rd=rolls[1:]-rolls[:-1]
x=rocks[1][:-1]
res=(x!=L+1)*((L-x)+(L-x-rd+1))*rd
print(res.sum()//2)