# check if two string is one edit away (add,remove,replace)

def solution(str_one,str_two):
    str_one = str_one.replace(' ','')
    str_two = str_two.replace(' ','')

    if len(str_one) == 0 and len(str_two) == 0:
        return True
    if len(str_one) == 1 and len(str_two) == 1:
        return True    

    #more than one edit away
    if len(str_one) - len(str_two) > 1 or len(str_one) - len(str_two) < - 1:
        return False

    maxLength = len(str_one) if len(str_one) >= len(str_two) else len(str_two)
    hashTable = [0] * 128
    foundDifference = False
    for i in xrange(0,maxLength):
        if i < maxLength - 1 or len(str_one) == len(str_two):
            if str_one[i] != str_two[i]:
                if foundDifference:
                    return False
                foundDifference = True
        else:
            if foundDifference and len(str_one) != len(str_two):
                return False

    return True


def test():
    assert (solution('dfjklsva','dfjklsva') == True),"wrong"
    assert (solution('','') == True),"wrong"
    assert (solution('aed','asd') == True),"wrong"
    assert (solution('aee','asd') == False),"wrong"
    assert (solution('dfsjklsvaasd','dfjklsvb') == False),"wrong"
    assert (solution('acde','acde1') == True),"wrong"
    print 'all passed'

test()
