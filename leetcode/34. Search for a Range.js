/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    if(nums.length < 2){
        if(nums[0] === target){
            return [0,0]
        }else{
            return [-1,-1]
        }
    }
    
    return recur(0,nums.length - 1, nums, target)
};

function recur(low,high,nums,target,result){
    if(low > high){
        return [-1,-1]
    }
    let mid = Math.floor((high+low)/2)
    if(nums[mid] > target){
        return recur(low,mid-1,nums,target)
    }else if (nums[mid] < target){
        return recur(mid + 1,high,nums,target)
    }else{
        var left = mid
        var right = mid
        while(nums[left] === target){
            left--
        }
        while(nums[right] === target){
            right++
        }
        return [left + 1, right - 1]
    }
}
