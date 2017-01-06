# given two string check if one is a permutation of the other

def solution(str_one,str_two):
    str_one.replace(' ','')
    str_two.replace(' ','')
    if len(str_one) != len(str_two):
        return False
    if len(str_one) == 0 or len(str_one) == 1:
        return str_one == str_two
    if (sorted(str_one) == sorted(str_two)):
        return True
    return False


def test():
    assert (solution('dfjklsva','dfjklsva') == True),"wrong"
    assert (solution('','') == True),"wrong"
    assert (solution('abcdefg','asd') == False),"wrong"
    assert (solution('dfsjklsva','dfjklsvb') == False),"wrong"
    assert (solution('acde1','acde1') == True),"wrong"

test()
