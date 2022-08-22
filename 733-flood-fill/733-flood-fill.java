class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int original = image[sr][sc];
        dfs(image, sr, sc, color, original);
        return image;
    }
    
    void dfs(int[][] image, int sr, int sc, int color, int original) {
        if (sr >= image.length || sc >= image[0].length || sr < 0 || sc < 0) {
            return;
        } else if (image[sr][sc] == color) {
            return;
        }
        
        if (image[sr][sc] == original) {
            image[sr][sc] = color;
            dfs(image, sr - 1, sc, color, original);
            dfs(image, sr + 1, sc, color, original);
            dfs(image, sr, sc - 1, color, original);
            dfs(image, sr, sc + 1, color, original);
        }
    }
}