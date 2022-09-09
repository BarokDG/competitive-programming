class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slis, tlis = list(s), list(t)
        
        slis.sort()
        tlis.sort()
        
        return slis == tlis