M=[0,25,16,9,4,1,0,1,4,9,16,25,36]
D=[0,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
MM=[0,31,28,31,30,31,30,31,31,30,31,30,31]
N=int(input())
R1,R2=map(int,input().split())
R=int(input())
nn,L=N,0
while(nn):
    sum=0
    for m in range(1,13):
        for d in range(1,MM[m]+1):
            s=min(M[m]+D[d],N)
            sum+=min(nn,s)*R2 + (s-min(nn,s))*R1
    if(sum>=R):
        L=nn
        break
    nn-=1
print(N-L)
