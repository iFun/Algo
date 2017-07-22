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
    if(str.length == max*2){
        result.push(str);
        return;
    }
    
    if(open < max){
        backtrack(open+1, close, str+"(", max, result);
    }
    if(close < open){
        backtrack(open, close+1, str+")", max, result);
    }
    return;
}
