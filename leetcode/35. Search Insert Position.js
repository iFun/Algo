/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    if(nums.length === 1){
        if(nums[0] >= target){
            return 0
        }else{
            return 1
        }
    }
    return binarySearch(nums,target,0,nums.length-1)
};

function binarySearch(nums,target,low,high){
    let mid = Math.floor((low + high)/2)
    if(nums[mid] === target){
        return mid
    }else if(low > high){
        if(nums[high] > target){
            return high - 1
        }else{
            return high + 1
        }
    }else{
        if(nums[mid] > target){
            return binarySearch(nums,target,low,mid-1)
        }else{
            return binarySearch(nums,target,mid+1,high)
        }
    }
}
