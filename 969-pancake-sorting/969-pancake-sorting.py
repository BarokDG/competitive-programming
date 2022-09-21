class Solution:      
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        
        def flipArraySlice(k: int, arraySlice: List[int]):
            arr[:k] = arraySlice[::-1]
            flips.append(k)
        
        pos = len(arr) - 1
        currentElem = len(arr)
                
        while pos > 0:
            currentElemIndex = arr.index(currentElem)
            if currentElemIndex != pos:
                if currentElemIndex != 0:
                    flipArraySlice(currentElemIndex + 1, arr[:currentElemIndex + 1])
                
                # flip again
                flipArraySlice(pos + 1, arr[:pos + 1])
                                
            pos -= 1
            currentElem -= 1
            
        return flips