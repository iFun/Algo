# check if string has all unique characters no additional data structure

import unittest

def solution(input):
    if len(input) == 0:
        return True
    strarry = sorted(input)
    for i in xrange(0,len(strarry) - 1):
        if strarry[i] == strarry[i+1]:
            return False
    return True


def test():
    assert (solution('dfjklsva') == True),"wrong"
    assert (solution('') == True),"wrong"
    assert (solution('abcdefg') == True),"wrong"
    assert (solution('dfsjklsva') == False),"wrong"
    assert (solution('acde1') == True),"wrong"

test()

        
