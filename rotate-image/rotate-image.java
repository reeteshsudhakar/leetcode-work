class Solution {
    public void rotate(int[][] matrix) {
        ArrayList<Integer> holder = new ArrayList<>();
        
        int column = 0;
        
        while (column < matrix.length) {
            for (int i = matrix.length - 1; i >= 0; i--) {
                holder.add(matrix[i][column]);
            }
            column++;
        }
            
        column = 0;
        
        while (column < matrix.length) {
            for (int j = 0; j < matrix.length; j++) {
                matrix[column][j] = holder.remove(0);
            }
            
            column++;
        }
    }
}