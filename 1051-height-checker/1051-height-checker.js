/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function(heights) {
    let r = 0
    
    let expected = [...heights]
    expected.sort((a, b) => a - b)
    
    for (let i = 0; i < heights.length; i++) {
        if (heights[i] !== expected[i]) {
            r++
        }
    }
    
    return r
};