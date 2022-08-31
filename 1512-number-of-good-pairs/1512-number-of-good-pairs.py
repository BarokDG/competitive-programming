class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:                
        nums.sort()
        
        goodpairs = 0
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):                
                if nums[i] == nums[j]:
                    goodpairs += 1
            
        
        return goodpairs