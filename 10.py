d={"F":(1,1),"J":(-1,-1),"7":(1,-1),"L":(-1,1),"|":(0,0),"-":(0,0)}
A=open("10.txt").read().split()
x,y,dx,dy,ii,area=19,88,1,0,0,0 # starting point & direction chosen manually
try:
    while True:
        ii+=1
        area+=y*dx
        x,y=x+dx,y+dy
        sx,sy=d[A[x][y]]
        dx,dy=sx+dx,sy+dy
except: # key 'S' not found in d, loop completed
    print(ii//2, abs(area)-ii//2+1)