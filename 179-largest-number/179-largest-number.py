class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        snums = [str(i) for i in nums]
        
        snums.sort()
        snums.reverse()
        
        for i in range(len(snums)):
            for j in range(len(snums)):
                if snums[i] + snums[j] > snums[j] + snums[i]:
                    snums[i], snums[j] = snums[j], snums[i]
        
        
        return "0" if snums[0] == "0" else "".join(snums)