import re
lines=open("1.txt").read().split()
d={str(ii):ii for ii in range(10)}
digits = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
d.update({dig:ii for ii,dig in enumerate(digits)}) # part B only
pat = '|'.join(d)
s=[sum(d[re.search(pat[::j],l[::j]).group()[::j]] for l in lines) for j in (1,-1)]
print(10*s[0]+s[1])