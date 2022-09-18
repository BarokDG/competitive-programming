class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        h = {}
        ts = 0
        
        for n in nums:
            if k - n in h and h[k - n] > 0:
                h[k - n] -= 1
                ts += 1
            
            elif n not in h:
                h[n] = 1
            
            else:
                h[n] += 1
            
        
        return ts