r,c=map(int,input().split())
x,y=map(int,input().split())
g=[]
for i in range(r):
    temp=list(input().split())
    g.append(temp)

time=[[0 for i in range(r)]for i in range(c)]
def count(row,col,curtime):
    if row<0 or row>r-1 or col<0 or col>c-1:return
    if g[row][col]=='W':return
    if time[row][col]!=0 and curtime>=time[row][col]:return
    time[row][col]=curtime
    count(row+1,col,curtime+1)
    count(row-1,col,curtime+1)
    count(row,col+1,curtime+1)
    count(row,col-1,curtime+1)
    count(row+1,col+1,curtime+1)
    count(row+1,col-1,curtime+1)
    count(row-1,col+1,curtime+1)
    count(row-1,col-1,curtime+1)
count(x-1,y-1,1)
ans=0
for i in range(r):
    for j in range(c):
        if ans<time[i][j]:
            ans=time[i][j]
print(ans)