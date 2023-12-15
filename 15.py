from collections import Counter
l=open("15.txt").read()[:-1].split(',')
def hash(s):
    return sum((16*ii+1)*ord(c) for ii,c in enumerate(s[::-1],1))%256
print(sum(hash(s) for s in l))
d={} # This solution uses the orderi-preserving property of dictionaries, formally added in Python 3.7
for ins in l:
    if ins[-1]=='-':
        try:
            del d[ins[:-1]]
        except:
            pass
    else:
        d[ins[:-2]]=int(ins[-1])
counter=Counter()
total=0
for key in d:
    counter[h:=hash(key)]+=1
    total+=(h+1)*counter[h]*d[key]
print(total)