class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        hashset = set()
        
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
            
        return False
        