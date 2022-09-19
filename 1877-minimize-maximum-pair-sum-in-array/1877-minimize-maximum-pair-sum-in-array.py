class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        maxSum = 0
        l, r = 0, len(nums) - 1
               
        nums.sort()
        
        while l < r:           
            maxSum = max(maxSum, nums[l] + nums[r])
            l += 1
            r -= 1
            
            
        return maxSum