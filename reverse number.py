def rev(n):
    revnum=0
    while n>0:
        r=n%10
        revnum=revnum*10+r
        n//=10
    print(revnum)
rev(35)
