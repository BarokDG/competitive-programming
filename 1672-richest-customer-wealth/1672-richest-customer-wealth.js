/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {    
    let totalBalances = []
    
    function sumBankBalances(account) {
        let sum = 0;
        
        for (let bankBalance of account) {
            sum += bankBalance
        }
        
        return sum
    }
    
    for (let account of accounts) {
        totalBalances.push(sumBankBalances(account))
    }
    
    return Math.max(...totalBalances);
};