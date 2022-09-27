class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for num in nums1:
            next_greater_element = -1
            
            for i in range(nums2.index(num), len(nums2)):
                if nums2[i] > num:
                    next_greater_element = nums2[i]
                    break
            
            ans.append(next_greater_element)
            
        return ans