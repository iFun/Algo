# check if string has all unique characters no additional data structure


def solution(arg):
    if len(arg) == 0:
        return True
    if len(arg) > 128:
        return False
    hashTable = [False] * 128

    for i in xrange(0,len(arg)):
        tmp = ord(arg[i])
        if(hashTable[tmp]):
            return False
        hashTable[tmp] = True
    return True


def test():
    assert (solution('dfjklsva') == True),"wrong"
    assert (solution('') == True),"wrong"
    assert (solution('abcdefg') == True),"wrong"
    assert (solution('dfsjklsva') == False),"wrong"
    assert (solution('acde1') == True),"wrong"

test()

        
