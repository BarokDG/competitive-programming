/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let x = 0
    
    for (let operation of operations) {
        if (operation === "--X" || operation === "X--") {
            x--
        } else {
            x++
        }
    }
    
    return operations.reduce((x, operation) => {
        if (operation.includes("-")) {
            x--
        } else {
            x++
        }
        
        return x
    }, 0)
};