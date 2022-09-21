class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequencyMap = {}
        arrSizeLimit = len(arr) // 2
        
        for num in arr:
            if num in frequencyMap:
                frequencyMap[num] += 1
            else:
                frequencyMap[num] = 1
                
        fMapValues = []
        for key in frequencyMap:
            fMapValues.append(frequencyMap[key])
        
        fMapValues.sort()

        output = 0
        
        while arrSizeLimit > 0:
            arrSizeLimit -= fMapValues.pop()
            output += 1
        
        return output