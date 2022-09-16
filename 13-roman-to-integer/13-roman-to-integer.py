class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        romanMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        prevChar = s[0]
        
        for char in s: 
            if prevChar == "I" and char in ["V", "X"]:
                result += romanMap[char] - (2 * romanMap[prevChar])
            elif prevChar == "X" and char in ["L", "C"]:
                result += romanMap[char] - (2 * romanMap[prevChar])
            elif prevChar == "C" and char in ["D", "M"]:
                result += romanMap[char] - (2 * romanMap[prevChar])
            else:
                result += romanMap[char]
                            
            prevChar = char
                    
        return result