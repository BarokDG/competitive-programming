class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        outputarr = []
        
        nums.sort()
        
        count = nums.count(target)
        index = 0
                
        if count > 0:
            index = nums.index(target)
            outputarr.append(index)

        if count > 1:
            for i in range(count-1):
                outputarr.append(index + (i + 1))
        
        return outputarr