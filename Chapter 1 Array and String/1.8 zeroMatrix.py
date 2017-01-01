matrix = [[0,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]


def solution():
    row = [None] * len(matrix)
    col = [None] * len(matrix[0])
    counter = 0
    for i in xrange(0,len(matrix)):
        for j in xrange(0,len(matrix[0])):
            if matrix[i][j] == 0:
                
                row[counter] = i
                col[counter] = j
                counter += 1

    for x in xrange(0,len(row)):
        if row[x] == None:
            break
        for j in xrange(0,len(matrix[0])):
            matrix[row[x]][j] = 0

    for x in xrange(0,len(col)):
        if col[x] == None:
            break
        for j in xrange(0,len(matrix)):
            matrix[j][col[x]] = 0
            

    printMatrix()
    return matrix

def printMatrix():
    for x in xrange(0,len(matrix)):
         print matrix[x]
    print ''


def main():
    rotatedMatrix = solution()
    assert (rotatedMatrix[0] == [0,0,0,0]),"wrong"
    assert (rotatedMatrix[1] == [0,6,7,0]),"wrong"
    assert (rotatedMatrix[2] == [0,10,11,0]),"wrong"
    assert (rotatedMatrix[3] == [0,0,0,0]),"wrong"

    print 'all passed'


if __name__ == '__main__':
    main()