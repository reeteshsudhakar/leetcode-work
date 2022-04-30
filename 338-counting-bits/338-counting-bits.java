class Solution {
    public int[] countBits(int n) {
        int[] arr = new int[n + 1];
        
        for (int i = 0; i <= n; i++) {
            arr[i] = hammingWeight(i);
        }
        
        return arr;
    }
    
    public int hammingWeight(int n) {
        int counter = 0;
        while (n != 0) {
            if ((n & 1) == 1) {
                counter++;
            }
            
            n = n >>> 1; 
        }
        
        return counter;
    }
}