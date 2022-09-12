class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        snums = [int(i) for i in nums]
        snums.sort()
        
        return str(snums[-k])
        