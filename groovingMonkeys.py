s=list(map(int,input().split()))
s2=[1,2,3,4,5,6]
t=[0,0,0,0,0,0]
t2=[1,2,3,4,5,6]
chk=True
cnt=0
while chk:
    for i in range(len(s)):
        t[s[i]-1]=s2[i]
    cnt+=1
    if t==t2:
        chk=False
        break
    else:
        s2=t
        t=[0,0,0,0,0,0]
        continue
print(cnt)