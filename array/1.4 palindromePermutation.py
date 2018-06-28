# given a string check if its palindromePermutation

def solution(s):
    s = s.replace(' ','')
    if len(s) == 0 or len (s) == 1:
        return True
    if len(s) == 2:
        return s[0] == s[1]
    hashTable = [0] * 128

    for i in xrange(0,len(s)):
        tmp = ord(s[i])
        if hashTable[tmp] == 0:
            hashTable[tmp] = 1
        else:
            hashTable[tmp] = 0

    return sum(hashTable) < 2


def test():
    assert (solution('dfjklsva   ') == False),"wrong"
    assert (solution('') == True),"wrong"
    assert (solution('abcde  fg') == False),"wrong"
    assert (solution('dfsjk ls  va') == False),"wrong"
    assert (solution('acd eacd  e') == True),"wrong"
    print 'All Passed'

if __name__ == "__main__":
    test()
