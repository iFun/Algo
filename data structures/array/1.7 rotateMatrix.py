matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


def solution():

    for layer in xrange(0,len(matrix)):
        first = layer
        last = len(matrix) - 1 - first
        for i in xrange(first,last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset]= matrix[i][last]
            matrix[i][last] = top
            

    printMatrix()
    return matrix

def printMatrix():
    for x in xrange(0,len(matrix)):
         print matrix[x]
    print ''


def main():
    rotatedMatrix = solution()
    assert (rotatedMatrix[0] == [13,9,5,1]),"wrong"
    assert (rotatedMatrix[1] == [14,10,6,2]),"wrong"
    assert (rotatedMatrix[2] == [15,11,7,3]),"wrong"
    assert (rotatedMatrix[3] == [16,12,8,4]),"wrong"

    print 'all passed'


if __name__ == '__main__':
    main()