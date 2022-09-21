class Solution:      
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        
        
        def flipArraySlice(k: int, arraySlice: List[int]):
            arr[:k] = arraySlice[::-1]
            flips.append(k)
            
        
        placeCurrentElemAt = len(arr) - 1
        currentElem = len(arr)
        
        while placeCurrentElemAt > 0:
            currentElemIndex = arr.index(currentElem)
            
            if currentElemIndex == placeCurrentElemAt:
                placeCurrentElemAt -= 1
                currentElem -= 1
                continue
            
            if currentElemIndex != 0:
                # place CurrentElem at arr[0]
                flipArraySlice(currentElemIndex + 1, arr[:currentElemIndex + 1])
                
            # place currentElem at sortedPosition
            flipArraySlice(placeCurrentElemAt + 1, arr[:placeCurrentElemAt + 1])
                                
            placeCurrentElemAt -= 1
            currentElem -= 1
            
        return flips