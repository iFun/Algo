/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let result = []
    backTrack(candidates,target,result,[],0)
    return result
};

function backTrack (candidates,target,result,current,sum){
    if(sum >= target){
        if(sum === target){
            result.push(current)
        }
        return
    }
    let index = 0
    if(current.length > 0){
        index = candidates.indexOf(current[current.length - 1])
    }
    
    for (let i = index; i< candidates.length; i++){
        if(target >= candidates[i]){
            current.push(candidates[i])
            sum += candidates[i]
            backTrack(candidates,target,result,current.slice(),sum)
            sum -= candidates[i]
            current.pop()
        }
    }
    
    
}
