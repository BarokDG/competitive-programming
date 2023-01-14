/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    return operations.reduce((x, operation) => {
        if (operation[1] === "-") {
            x--
        } else {
            x++
        }
        
        return x
    }, 0)
};