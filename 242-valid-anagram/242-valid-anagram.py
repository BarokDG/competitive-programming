class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slis, tlis = list(s), list(t)
        
        if len(slis) == len(tlis):
            slis.sort()
            tlis.sort()

            return slis == tlis
        
        return False