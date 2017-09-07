/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    let result = []
    backtrack(nums,[],result)
    return result
};

function backtrack(nums,current,result){
    if(current.length === nums.length){
        result.push(current)
        return
    }else{
        for(let i = 0; i< nums.length; i++){
            if(!current.includes(nums[i])){
                current.push(nums[i])
                backtrack(nums,current.slice(),result) // slice makes a copy of array
                current = current.slice(0,-1) // remove last element, since all the permuation of that element has being genereated by recursion call
            }
        }
    }
}
