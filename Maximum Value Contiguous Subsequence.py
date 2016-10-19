# Given a sequence of n real numbers A(1) ... A(n), 
#determine a contiguous subsequence A(i) ... A(j) 
#for which the sum of elements in the subsequence is maximized.

def solution(inputs):
    result = -999999
    dpsum = len(inputs) * [None]
    dpsum[0] = inputs[0]

    for i in range(1,len(inputs)):
        tmp = inputs[i] + dpsum[i-1]

        if tmp > inputs[i]:
            dpsum[i] = tmp
        else:
            dpsum[i] = inputs[i]
        if result < dpsum[i]:
            result = dpsum[i]

        

    print result




test = [3,4,-2,-3,8,-2,7,-9,-11,2,-3,7,3,-4,-2,3]
solution(test)