def binSearch(arr, key, start, end):
    if start > end:
        return start
    mid = (start + end) // 2
    if (key > arr[mid]):
        binSearch(arr, key, mid + 1, end)   
    else:
        binSearch(arr, key, start, mid-1)
    

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        loc = binSearch(arr, key, 0, i- 1)
        arr[loc+1: i + 1] = arr[loc: 1]
        arr[loc] = key


a = [23, 4, 56, 34, 454, 2]

print(a)
insertionSort(a)
print(a)