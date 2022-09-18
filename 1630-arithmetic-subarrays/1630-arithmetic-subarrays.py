class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        results = []
        
        for i in range(len(l)):
            temp = nums.copy()[l[i]:r[i] + 1]
            
            if len(temp) < 3:
                results.append(True)
                continue
            
            temp.sort()
            
            change = temp[1] - temp[0]
            
            skipOuter = False
            
            for i in range(1, len(temp) - 1):
                if temp[i + 1] - temp[i] != change:
                    results.append(False)
                    skipOuter = True
                    break
                
            if skipOuter == False:
                results.append(True)
            
        return results
        