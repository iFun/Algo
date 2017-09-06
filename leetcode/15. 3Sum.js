/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  if (nums.length < 3) {
    return []
  }
  let result = []
  nums = nums.sort(function (a, b) {
    return a - b
  })
  for (let i = 0; i < nums.length - 2; i++) {
    let sum = -nums[i]
    let low = i + 1
    let high = nums.length - 1
    ////skip duplicate
    if (i == 0 || (i > 0 && nums[i - 1] !== nums[i])) {
      while (low < high) {
        if (nums[low] + nums[high] === sum) {
          let tmp = []
          tmp.push(nums[low])
          tmp.push(nums[high])
          tmp.push(nums[i])
          result.push(tmp)
          //skip duplicate
          while (low < high && nums[low] == nums[low + 1]) {
            low++
          }
          ////skip duplicate
          while (low < high && nums[high] == nums[high - 1]) {
            high--
          }

          low++
          high--
        }
        if (nums[low] + nums[high] > sum) {
          high--
        }
        if (nums[low] + nums[high] < sum) {
          low++
        }
      }
    }

  }
  return result

};
