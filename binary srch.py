def srch(n,list):
    for i in range(len(list)-1):
        min=i
    for j in range(i,len(list)):
        if list[min]>list[j]:
            list[min],list[j]=list[j],list[min]
            min=j
            
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if n==list[mid]:
            print("found at:",mid)
            break
        else:
            if list[mid]<n:l=mid
            else:u=mid
    else:
        print("not found")
