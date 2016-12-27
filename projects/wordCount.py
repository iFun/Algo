# this small project count how many words in one txt file

import sys

def processFile(filename):
    f = open(filename,'r')
    hashTable = {}
    text = f.readline()
    count = 0
    if not text:
        print 'word count: 0'
        return 0
    while text:
        words = text.split()
        for word in words:
            if word:
                word = word.lower()
                lastword = word[-1:]
                if not lastword.isalpha() and not lastword.isdigit():
                    word = word[:len(word) - 2]

                if word in hashTable:
                    hashTable[word] += 1
                else:
                    hashTable[word] = 1
                count+=1
        text = f.readline()

    f.close()
    print count
        
    

     


     


def main():
    if len(sys.argv) == 1 or not sys.argv[1]:
        print 'please input filename'
    else:
        processFile(sys.argv[1])
    



if __name__ == '__main__':
    main()