def moveZeros(arr):
    if not arr: return []

    length = len(arr)
    j = 0

    for num in arr:
        if num != 0:
            arr[j] = num
            j += 1
    
    for i in range(j, length):
        arr[i] = 0
    
    return arr

arr = [0, 1, 0, 3, 12]
answer = moveZeros(arr)
print(answer)