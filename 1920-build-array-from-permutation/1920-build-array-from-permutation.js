/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function(nums) {
    let ans = []
    
    for (let num of nums) {
        ans.push(nums[num])
    }
    
    return ans
};