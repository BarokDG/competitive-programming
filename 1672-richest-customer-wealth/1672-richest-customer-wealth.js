/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    return accounts.reduce((richestWealth, current) => {
        let currentWealth = current.reduce((sum, balance) => sum + balance, 0)
        return Math.max(richestWealth, currentWealth)
    }, 0)
};