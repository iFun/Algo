# compress a string 

def solution(s):
    if len(s) < 5:
        return s
    result = ''
    char = ''
    counter = 1
    for i in xrange(0,len(s) - 1):
        if s[i] == s[i+1]:
            char = s[i]
            counter += 1
            if i + 1 == len(s) - 1:
                result = result + char + str(counter)
        else:
            if counter != 1:
                result = result + char + str(counter)
                counter = 1
            else:
                result = result + s[i]

    if s[len(s) - 1] != s[len(s) - 2]:
        result = result + s[len(s) - 1]


    result = s if len(result) >= len(s) else result

    return result



def test():
    assert (solution('dfjklsva') == 'dfjklsva'),"wrong"
    assert (solution(' ') == ' '),"wrong"
    assert (solution('aaaaeeeed') == 'a4e4d'), "wrong"
    assert (solution('aee') == 'aee'),"wrong"
    assert (solution('dfsjklsvaasd') == 'dfsjklsvaasd'),"wrong"
    assert (solution('acdeeee') == 'acde4'),"wrong"
    print 'all passed'

if __name__ == "__main__":
    test()

