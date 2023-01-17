/**
 * @param {number[]} nums
 * @return {number[]}
 */
var numberOfPairs = function(nums) {
    let pairs = 0
    
    let obj = {}
    
    for (let num of nums) {
        if (obj[num]) {
            delete obj[num]
            pairs++
        } else {
            obj[num] = 1   
        }        
    }
    
    return [pairs, Object.values(obj).length]
};