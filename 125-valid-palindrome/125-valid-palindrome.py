class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for char in s.lower():
            if char.isalnum():
                newStr += char
        
        return newStr == newStr[::-1]