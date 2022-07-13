class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        r = ""

        for char in s:
            if char.isalnum():
                r += char
        
        i = 0
        j = len(r) - 1
        
        for x in range(len(r)):
            if i == j:
                break
            
            if (r[i] != r[j]):
                return False
            
            i += 1
            j -= 1
        
        return True