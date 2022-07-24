class Solution {
    public void rotate(int[][] matrix) {
                int matrixLength = matrix.length;
        int rowLength = matrix[0].length;
        Queue<Integer> queue = new LinkedList<>();

        if (matrixLength == 0 || rowLength == 0) {
            System.out.println("ERROR: matrix has invalid dimensions.");
        }

        int column = 0;
        while (column < matrixLength) {
            for (int i = matrixLength - 1; i >= 0; i--) {
                queue.add(matrix[i][column]);
            }
            column++;
        }

        for (int i = 0; i < matrixLength; i++) {
            for (int j = 0; j < matrixLength; j++) {
                matrix[i][j] = queue.poll();
            }
        }

    }
}