class Solution {
    public void rotate(int[] nums, int k) {
        
        if (k % nums.length == 0) {
            return;
        }
        
        int[] newNums = nums.clone();
        
        for (int i = 0; i < nums.length; i++) {
            nums[(i + k) % nums.length] = newNums[i];
        }
        
        
    }
}