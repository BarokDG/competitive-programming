def insertionSort1(n, arr):
    # Write your code here
    i = arr[n - 1]
    
    def printArray():
        for num in arr:
            print(num, end=" ")
        print()
    
    for index in range(n - 2, -1, -1):        
        if arr[index] < i:
            arr[index + 1] = i
            printArray()
            return
            
        else:
            arr[index + 1] = arr[index]
            printArray()
    
    arr[0] = i
    printArray()