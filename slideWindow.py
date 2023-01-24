def slideWindow(arr, windowSize):
    arraySize = len(arr)
    if arraySize <= windowSize:
        print("Invalid operation")
        return -1

    windowSum = sum([arr[i] for i in range(windowSize)])
    maxSum = windowSum

    for i in range(arraySize - windowSize):
        windowSum = windowSum - arr[i] + arr[i + windowSize]
        maxSum = max(windowSum, maxSum)
      
    return maxSum

arr = [80, -50, 90, 100]
k = 2
answer = slideWindow(arr, k)
print(answer)