/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let prev = nums[0]
    
    for (let i = 1; i < nums.length; i++) {
        nums[i] += prev
        prev = nums[i]
    }
    
    return nums
};