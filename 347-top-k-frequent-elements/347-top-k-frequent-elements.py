class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        if len(nums) == k:
            return nums
        
        uniqueNums = []
        frequencyMap = []
        result = []
        
        for num in nums:
            if num not in uniqueNums:
                uniqueNums.append(num)
                frequencyMap.append(1)
                continue
            
            uniqueNumsIndex = uniqueNums.index(num)
            frequencyMap[uniqueNumsIndex] += 1
            
        for i in range(k):
            maxNumIndex = frequencyMap.index(max(frequencyMap))
            
            result.append(uniqueNums[maxNumIndex])
            frequencyMap[maxNumIndex] = -1
            
        return result
                
        
        
        
                
        
            
