w=input()
c=0
l=len(w)
wl=[]
s1=""
s2=""
s3=""

def p():
    global w,c,l,wl,s1,s2,s3
    f=1
    for i in range(c+1,l):
        s=w[c:i+1]
        for j in range(len(s)):
            if s[j]==s[len(s)-1-j]:
                f=1
                continue
            else:
                f=0
                break
        if f==1:
            wl.append(w[c:i+1])
            c=i+1
            if i!=l-1:p()
    if f==0:return 'n'
    s1=wl[0]
    s2=wl[1]
    s3=wl[2]
p()
print(s1)
print(s2)
print(s3)