/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {    
    let maxBalance = 0
    
    function sumBankBalances(account) {
        let sum = 0;
        
        for (let bankBalance of account) {
            sum += bankBalance
        }
        
        return sum
    }
    
    for (let account of accounts) {
        maxBalance = Math.max(maxBalance, sumBankBalances(account))
    }
    
    return maxBalance
};