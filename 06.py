# l=open("06.txt").read().split() # part A
l=open("06.txt").read().replace(" ","").replace(":"," ").split() # part B
res=1
for t,d in zip(l[1:],l[len(l)//2+1:]):
    t=int(t); d=int(d)
    s=((t/2)**2-d)**.5
    res*= 1+2*int(s) if t%2==0 else 2*int(s+.5)
print(res)