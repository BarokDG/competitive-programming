/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let maxWealth = 0

    for (let account of accounts) {
        let currentAccountWealth = account.reduce((sum, current) => sum + current);

        maxWealth = Math.max(maxWealth, currentAccountWealth)
    }

    return maxWealth;
};