class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slis = list(s)
        tlis = list(t)
        
        slis.sort()
        tlis.sort()
        
        sd = [i for i in slis]
        td = [i for i in tlis]
        
        return sd == td