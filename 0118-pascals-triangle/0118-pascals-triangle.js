/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {    
    if (numRows === 1) return [[1]]
    if (numRows === 2) return [[1], [1, 1]]
    
    let p_triangle = [[1], [1, 1]]
    for (let i = 2; i < numRows; i++) {
        let row = []
        
        for (let j = 0; j <= i; j++) {
            if (j === 0 || j === i) {
                row.push(1)
                continue
            }
            
            let result = p_triangle[i - 1][j] + p_triangle[i - 1][j - 1]
            row.push(result)
        }
        
        p_triangle.push(row)
    }
    
    return p_triangle
};