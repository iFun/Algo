/**
 * @param {number[]} nums
 * @return {number[]}
 */

// Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

// Find all the elements that appear twice in this array.

// Could you do it without extra space and in O(n) runtime?
var findDuplicates = function(nums) {
    if(nums.length == 0 || nums === null){
        return [];
    }
    var result = [];
    for(var i = 0; i < nums.length; i++){
        var location = Math.abs(nums[i]) - 1;
        if(nums[location] > 0){
            nums[location] = - nums[location];
        }else{
            //duplicate already visited
            result.push(Math.abs(nums[i]));
        }
    }
    return result;
};