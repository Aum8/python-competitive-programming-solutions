n=list(map(int,input().split()))
val=0
def s():
    global val
    m=max(n)
    if m==0:return val
    i=n.index(m)
    n[i]=0
    if i!=0:
        if n[i-1]:n[i-1]=0
    if i!=len(n)-1:
        if n[i+1]:n[i+1]=0
    val+=m
    s()
s()
