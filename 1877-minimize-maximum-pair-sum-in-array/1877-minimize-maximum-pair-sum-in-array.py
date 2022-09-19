class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        maxSum = 0
        l = 0
        r = len(nums) - 1
        
        nums.sort()
        
        for i in range(len(nums)):
            if l == r:
                break
            
            maxSum = max(maxSum, nums[l] + nums[r])
            l += 1
            r -= 1
            
            
        return maxSum