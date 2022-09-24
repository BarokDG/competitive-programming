import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:                
        stack = []
                
        for token in tokens:              
            if token in "+-*/":
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "-":
                    op1 = stack.pop()
                    op2 = stack.pop()
                    
                    stack.append(op2 - op1)
                elif token == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    op1 = stack.pop()
                    op2 = stack.pop()
                        
                    stack.append(math.trunc(op2 / op1))
            else:
                stack.append(int(token))
 
        return stack.pop()