/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let left = 0
    let right = 0
    let map = {}
    let ans = 0
    while(right < s.length){
        let current = s[right]
        if(map[current]){
            left = Math.max(left, map[current])
        }
        ans = Math.max(right-left+1, ans)
        map[current] = right+1
        right++
    }
    return ans
};
