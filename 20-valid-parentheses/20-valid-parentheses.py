class Solution:
    def isValid(self, s: str) -> bool:
        if s.count("(") != s.count(")"): return False
        if s.count("{") != s.count("}"): return False
        if s.count("[") != s.count("]"): return False
        
        stack = []
        
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if (len(stack) != 0): # check if there's open parantheses
                    if char == ")" and stack[-1] != "(":
                        return False
                    elif char == "}" and stack[-1] != "{":
                        return False
                    elif char == "]" and stack[-1] != "[":
                        return False
                    else:
                        stack.pop()
                else:
                    return False
                    
        return True