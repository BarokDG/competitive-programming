class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            
            if nums.count(diff) and nums.index(diff) != i:               
                return [i, nums.index(diff)]