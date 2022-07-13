#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        snum = arr[i]
        ind = i
        
        for x in range(i, len(arr)):
            if arr[x] < snum:
                snum = arr[x]
                ind = x
        
        return ind
    
    def selectionSort(self, arr, n):
        #code here
        for i in range(n):
            se = self.select(arr, i)
            arr[i], arr[se] = arr[se], arr[i]
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends