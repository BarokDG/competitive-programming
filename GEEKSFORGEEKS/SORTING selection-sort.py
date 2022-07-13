class Solution: 
    def select(self, arr, i):
        ind = i
        
        for x in range(i, len(arr)):
            if arr[x] < arr[ind]:
                ind = x
        
        return ind
    
    def selectionSort(self, arr, n):
        for i in range(n):
            se = self.select(arr, i)
            arr[i], arr[se] = arr[se], arr[i]