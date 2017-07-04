/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function (list1, list2) {
  let result = [];
  const hsMap = new Map();
  let minSum = 9999999;

  for (var i = 0; i < list1.length; i++) {
    hsMap.set(list1[i], i);
  }
  for (var j = 0; j < list2.length; j++) {
    if (hsMap.has(list2[j]) && j + hsMap.get(list2[j]) <= minSum) {
      if (minSum == j + hsMap.get(list2[j])) {
        result.push(list2[j]);
      } else {
        result = [list2[j]];
        minSum = j + hsMap.get(list2[j]);
      }

    }
  }
  return result;

};
