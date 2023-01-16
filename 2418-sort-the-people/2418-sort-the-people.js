/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 */
var sortPeople = function(names, heights) {
  let hash = {}
    
  for (let i = 0; i < names.length; i++) {
      hash[heights[i]] = names[i]
  }  
    
  heights.sort((a, b) => b - a)

  return heights.map(height => hash[height])
};