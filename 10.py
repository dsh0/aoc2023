d={"F":(1,1),"J":(-1,-1),"7":(1,-1),"L":(-1,1),"|":(0,0),"-":(0,0),"S":(2,2)}
A=open("10.txt").read().split()
x,y,dx,dy,ii,area=19,88,1,0,0,0 # starting point & direction chosen manually
while dx*dy==0:
    ii+=1
    area+=y*dx
    x,y=x+dx,y+dy
    sx,sy=d[A[x][y]]
    dx,dy=sx+dx,sy+dy
print(ii//2, abs(area)-ii//2+1)