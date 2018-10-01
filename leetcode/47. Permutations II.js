/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    if(nums.length < 2){
        return [nums];
    }
    nums = nums.sort(function(a, b){return a-b});
    let result = [];
    recur([],[],nums,result);
    return result
    
};

function recur(current, used, nums , result){
    if(current.length === nums.length){
        result.push(current);
    }
    
    for(let i = 0; i< nums.length; i++){
        if(used[i]){
            continue;
        }
        if(i > 0 &&  nums[i] === nums[i-1] &&!used[i-1]){
            continue;
        }
        used[i] = true;
        current.push(nums[i]);
        
        recur(current.slice(),used.slice(),nums,result);
        used[i] = false;
        current.pop();
    }
}
