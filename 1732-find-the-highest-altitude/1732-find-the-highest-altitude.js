/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    let m = 0
    let p = m
    
    for (let g of gain) {
        p += g
    
        if (p > m) {
            m = p
        }
    }
    
    return m
};