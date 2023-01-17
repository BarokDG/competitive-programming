/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let [smaller, larger] = nums1.length < nums2.length ? [nums1, nums2] : [nums2, nums1];
    let intersection = {}
       
    for (let num of smaller) {        
        if (larger.includes(num)) {
            intersection[num] = 1
        }
    }
    
    return Object.keys(intersection)
};