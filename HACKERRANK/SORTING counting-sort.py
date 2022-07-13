def countingSort(arr):
    # Write your code here
    newArr = [0 for i in range(100)]
                
    for el in arr:
        newArr[el] += 1
        
    return newArr