from itertools import permutations
def x():
    a,b=map(int,input().split())
    a=list(str(a))
    a=sorted(permutations(a))
    
    for i in list(a):
        s=""
        for j in i:s+=j
        if int(s)>b:return s
    return -1
print(x())