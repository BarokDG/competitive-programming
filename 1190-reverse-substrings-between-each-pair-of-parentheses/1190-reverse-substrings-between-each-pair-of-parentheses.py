class Solution:
    def reverseParentheses(self, s: str) -> str:
        r = ""
        stack = []
        
        for char in s:
            if char == "(":
                stack.append(r)
                r = ""
            elif char == ")":                    
                r = stack[-1] + r[::-1]
                stack.pop()
            else:
                r += char
                
        return r