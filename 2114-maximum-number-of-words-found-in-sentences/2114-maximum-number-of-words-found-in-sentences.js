/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
  let maxWordsInASentence = 0;
    
  for (let sentence of sentences) {
      let wordsInSentence = sentence.split(" ").length
      maxWordsInASentence = Math.max(wordsInSentence, maxWordsInASentence);
  }
    
  return maxWordsInASentence
};