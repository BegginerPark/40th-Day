def bubble(arr):
    for k in range(len(arr)):
        for i in range(len(arr)-k-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

array = [5,3,4,1,2,7,9,6,8]
print(bubble(array))