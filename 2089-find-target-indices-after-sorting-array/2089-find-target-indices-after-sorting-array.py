class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        outputarr = []
        
        nums.sort()
        
        if nums.count(target) > 0:
            i = nums.index(target)
            outputarr.append(i)

            j = i + 1
            while (j <= len(nums) - 1) and nums[i] == nums[j]:
                outputarr.append(j)
                j += 1
        
        return outputarr