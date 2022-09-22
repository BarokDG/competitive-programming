class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequencyMap = {}
        halfArraySize = len(arr) // 2
        
        for num in arr:
            if num in frequencyMap:
                frequencyMap[num] += 1
            else:
                frequencyMap[num] = 1
                
        fMapValues = sorted(frequencyMap.values())
        
        setSize = 0
        
        while halfArraySize > 0:
            halfArraySize -= fMapValues.pop()
            setSize += 1
        
        return setSize