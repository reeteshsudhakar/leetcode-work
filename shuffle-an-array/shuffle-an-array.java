class Solution {
    
    private int[] nums;
    private Random random;

    public Solution(int[] nums) {
        this.nums = nums;
        this.random = new Random();
    }
    
    public int[] reset() {
        return this.nums;
    }
    
    public int[] shuffle() {
        int[] shuffled = new int[this.nums.length];
        
        for (int i = 0; i < nums.length; i++) {
            shuffled[i] = nums[i];
        }
        
        for (int i = nums.length - 1; i > 0; i--) {
            int randomIdx = this.random.nextInt(i + 1);
            
            int temp = shuffled[i];
            shuffled[i] = shuffled[randomIdx];
            shuffled[randomIdx] = temp;
        }
        
        return shuffled;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */