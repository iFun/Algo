class Solution {
    public void setZeroes(int[][] matrix) {
        boolean firstRow = false;
        boolean firstCol = false;
        int row = matrix.length;
        int col = matrix[0].length;
        
        for(int i = 0; i < row; i++){
            for(int j = 0; j< col; j++){
                if(i == 0 && matrix[i][j] == 0){
                    firstRow = true;
                }
                if(j == 0 && matrix[i][j] == 0){
                    firstCol = true;
                }
                
                if(matrix[i][j] == 0){
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        for(int i = row - 1; i > 0; i--){
            for(int j = col - 1; j > 0; j--){
                if(matrix[0][j] == 0 || matrix[i][0] == 0){
                    matrix[i][j] = 0;
                }
            }
        }
        if (firstRow) for (int i = 0; i < col; ++i) matrix[0][i] = 0;
        if (firstCol) for (int i = 0; i < row; ++i) matrix[i][0] = 0;
        
    }
}
//use first row and col to store status
