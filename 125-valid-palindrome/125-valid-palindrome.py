class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        result = ""

        for char in s:
            if char.isalnum():
                result += char
        
        return result == result[::-1]