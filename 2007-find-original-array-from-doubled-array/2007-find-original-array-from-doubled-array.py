class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        frequencyMap = {}
        
        for num in changed:
            if num in frequencyMap:
                frequencyMap[num] += 1
            else:
                frequencyMap[num] = 1
                
        changed.sort()
        
        og = []
        
        for num in changed:
            if frequencyMap[num] > 0:
                frequencyMap[num] -= 1
                
                if num * 2 in frequencyMap and frequencyMap[num * 2] > 0:
                    frequencyMap[num * 2] -= 1
                    og.append(num)

            if len(changed) // 2 == len(og):
                return og
        
        return []
                
                