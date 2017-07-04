/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function (s) {
  if (s.length < 2) {
    return 1;
  }

  let max = 0;
  const map = new Map();
  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i])) {
      max += 2;
      map.delete(s[i]);
    } else {
      map.set(s[i], true);
    }
  }
  if (max < s.length) {
    max++;
  }
  return max;

};
