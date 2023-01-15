/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    let m = 0
    
    for (let i = 0; i < candies.length; i++) {
        m = Math.max(m, candies[i])
        candies[i] += extraCandies
    }
    
    return candies.map((k) => k >= m)
};