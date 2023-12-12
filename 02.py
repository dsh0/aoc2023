import re
ls=open("02.txt").read().split('\n')
mlai=[('red',12),('green',13),('blue',14)]

res=0
for ii,l in enumerate(ls,1):
    if all(int(x)<=lim for col,lim in mlai for x in re.findall(fr'(\d+) {col}',l)):
            res+=ii
print(res)

res=0
for l in ls:
    prod=1
    for col,_ in mlai:
        prod*=max(int(x) for x in re.findall(fr'(\d+) {col}',l))
    res+=prod
print(res)