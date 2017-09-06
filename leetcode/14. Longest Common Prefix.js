/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if(strs.length === 0){
        return ""
    }
    if(strs.length === 1){
        return strs[0]
    }
    
    let result = strs[0]
    
    for(let i  = 1; i< strs.length; i++){
        if(!strs[i].startsWith(result)){
            result = result.slice(0,-1)
            while(!strs[i].startsWith(result)){
                result = result.slice(0,-1)
                if(result === ""){
                    return result
                }
            }
        }
    }
    return result
    
};
