class Solution {
    public int singleNumber(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        } else {
            int unique = 0;
            
            for (int i = 0; i < nums.length; i++) {
                unique ^= nums[i];
            }
            
            return unique;
        }
        
    }
}