/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    if(nums == null){
        return nums;
    }
    var result = []
    recur(nums,result, [], 0)
    return result
    
};

function recur(nums, result, current, index){
    result.push(current.slice()) // so it is not pass by pointer
    
    for(let i = index; i < nums.length; i++){
        current.push(nums[i]);
        recur(nums,result, current, i+1)
        current.pop()
    }
}
