class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        minePile = 0
        
        piles.sort()
        
        for i in range(len(piles) // 3):            
            minePile += piles[-2 * (i + 1)]
            
        return minePile
