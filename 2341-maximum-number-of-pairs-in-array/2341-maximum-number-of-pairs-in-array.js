/**
 * @param {number[]} nums
 * @return {number[]}
 */
var numberOfPairs = function(nums) {
    let pairs = 0
    let leftover = 0
    
    let obj = {}
    
    for (let num of nums) {
        if (obj[num]) {
            obj[num]++   
        } else {
            obj[num] = 1   
        }        
    }
    
    for (let num in obj) {        
        pairs += Math.floor(obj[num] / 2)
        leftover += obj[num] % 2
    }
    
    return [pairs, leftover]
};