class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reds = []
        whites = []
        blues = []
        
        for el in nums:
            if el == 0:
                reds.append(el)
            elif el == 1:
                whites.append(el)
            else:
                blues.append(el)
                
        nums.clear()
        nums.extend(reds)
        nums.extend(whites)
        nums.extend(blues)

        