def partition(arr, low, high):  # declare pivot and divide list
    i = (low-1)         
    pivot = arr[high]
    
    for j in range(low, high):
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)  
  
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
  
arr = []
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)
