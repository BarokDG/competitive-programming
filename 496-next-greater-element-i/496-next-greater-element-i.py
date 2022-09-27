class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        mapping = {}
        stack = []
        
        answer = []
        
        for num in nums2:
            if len(stack) == 0:
                stack.append(num)
                continue
                
            while stack and num > stack[-1]:
                mapping[stack[-1]] = num
                stack.pop()
                
            stack.append(num)
            
        
        for num in nums1:
            if num in mapping:
                answer.append(mapping[num])
            else:
                answer.append(-1)
                
        return answer