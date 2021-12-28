test=int(input())
def sol():
    n,d,c,m=map(int,input().split())
    s=list(input())
    for i in s:
        if i=='D':
            if d==0 or c<0:
                return "NO"
            d-=1
            c+=m
            m=0
        else:
            c-=1
    return "YES"
for t in range(test):
    print('Case #%d: %s'%(t+1,sol()))