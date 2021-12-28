q=list(input())
l=[]
voteA=0
voteB=0
BS=False
count=0
for i in q:
    l.append(i)
        
for i in range(len(l)):
    if i!=len(l)-1:
        if l[i]=="-":
            count+=1
            continue
        if l[i]=="A":
            if BS==True:
                temp=count//2
                voteA+=temp+1
                voteB+=temp
                BS=False
                continue
            if BS==False:
                 voteA+=count+1
                 continue
        if l[i]=="B":
            if BS==False:
                BS=True
                count=0
                voteB+=1
                continue
            if BS==True:
                voteB+=1+count
                continue

    if i==len(l)-1 and l[i]=="-":
        if BS==True:
            voteB+=1+count
            break
    if i==len(l)-1 and l[i]=="A": 
        if BS==True:
                temp=count//2
                voteA+=temp+1
                voteB+=temp
        if BS==False:
            voteA+=count+1
        break
    if i==len(l)-1 and l[i]=="B": 
        if BS==True:
            voteB+=1+count
            break
        else:voteB+=1

if voteA>voteB:print("A",voteA)
if voteA<voteB:print("B",voteB)
if voteA==voteB:print("-")