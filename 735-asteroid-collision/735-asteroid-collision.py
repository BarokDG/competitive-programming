class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:        
        stack = []
        
        for asteroid in asteroids:
            if len(stack) == 0:
                stack.append(asteroid)
                continue
            
            if asteroid > 0:
                stack.append(asteroid)
            else:                
                cancel = False
                
                while len(stack) > 0 and stack[-1] + asteroid <= 0:
                    cancel = stack[-1] + asteroid == 0
                    
                    if stack[-1] < 0:
                        stack.append(asteroid)
                        break
                    elif cancel:
                        stack.pop()
                        break
                    
                    stack.pop()
                    
                if len(stack) == 0 and not cancel:
                    stack.append(asteroid)
                
        return stack
            