/**
 * @param {number[]} heights
 * @return {number}
 */
var heightChecker = function(heights) {
    let r = 0
    
    let expected = [...heights]
    expected.sort((a, b) => a - b)
    
    heights.forEach((height, index) => {
        if (expected[index] !== height) {
            r++
        }
    })
    
    return r
};