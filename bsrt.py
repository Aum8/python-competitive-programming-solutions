arr=[1,2,3,4]
n = len(arr)
 
for i in range(n-1):
    flag=0
    
    for j in range(0, n-i-1):
        if arr[j] > arr[j + 1] :
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            flag=1

    if flag==0:
        break
    
print(arr)
