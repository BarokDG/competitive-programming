class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(" ")
        ptracker = [0 for el in arr]
        
        for el in arr:
            ind = int(el[-1]) - 1
            ptracker[ind] = el
            
            
        result = ""
        for el in ptracker:
            el = el[:-1]
            result += el + " "
            
        return result.rstrip()
        
        
            
            