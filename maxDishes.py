n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    if i not in l:l.append(i)
count=[0]*(len(l))
for i in l:
    for j in a:
        if i==j:
            count[l.index(i)]+=1
            j+=1
print(l[count.index(max(count))])