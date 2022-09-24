import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:                
        stack = []
                
        for token in tokens:              
            if token in "+-*/":
                op1 = stack.pop()
                op2 = stack.pop()
                
                if token == "+":
                    stack.append(op2 + op1)
                elif token == "-":
                    stack.append(op2 - op1)
                elif token == "*":
                    stack.append(op2 * op1)
                else:                    
                    stack.append(math.trunc(op2 / op1))
            else:
                stack.append(int(token))
 
        return stack.pop()