/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    let p_triangle = []
    
    for (let i = 1; i <= numRows; i++) {
        let arr = []
        for (let j = 0; j < i; j++) {
            if (j === 0 || j === i - 1) {
                arr.push(1)
            } else {
                arr.push(0)
            }
            
        }
        
        p_triangle.push(arr)
    }
    
    return p_triangle.map((elem, index, array) => {
        if (index === 0 || index === 1) return elem
        
        let previousElem = array[index - 1];
        for (let i = 1; i < elem.length; i++) {
            if (elem[i] !== 0) continue
            
            elem[i] = previousElem[i - 1] + previousElem[i]            
        }
        
        return elem
    })
};