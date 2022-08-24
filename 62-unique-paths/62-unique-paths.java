class Solution {
    public int uniquePaths(int m, int n) {
        if (m == 1 || n == 1) {
            return 1;
        }
        
        int[][] dp = new int[m][n];
        
        for (int i = 0; i < m; i++) {
            Arrays.fill(dp[i], -1);
        }
        
        dp[0][0] = 0;
        
        return pathFinder(m - 1, n - 1, dp);
    }
    
    public int pathFinder(int m, int n, int[][] dp) {
        if (m == 0 || n == 0) {
            return 1;
        }
        
        if (dp[m][n] != -1) {
            return dp[m][n];
        }
        
        dp[m][n] = pathFinder(m - 1, n, dp) + pathFinder(m, n - 1, dp);
        
        return dp[m][n];
    }
}