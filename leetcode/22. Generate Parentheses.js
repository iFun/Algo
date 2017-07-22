/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    var result = [];
    backtrack(0,0,"",n,result);
    return result;
};

function backtrack (open,close,str,max, result){
    //total is n*2
    if(str.length == max*2){
        result.push(str);
        return;
    }
    
    //add as much as (
    if(open < max){
        backtrack(open+1, close, str+"(", max, result);
    }
    //after adding ( start to add ), but if close number is = or > then open stop adding
    if(close < open){
        backtrack(open, close+1, str+")", max, result);
    }
    return;
}
