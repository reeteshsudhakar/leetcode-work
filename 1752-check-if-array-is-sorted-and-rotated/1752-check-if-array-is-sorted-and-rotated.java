class Solution {
    public boolean check(int[] nums) {
        int count = 0;
        int n = nums.length;
        
        // checks if each item is greater than the previous
        for (int i = 1; i < n; i++) {
            if (nums[i - 1] > nums[i]) {
                count++;
            }
        }
        
        // checks that a rotation is possible
        if (nums[n - 1] > nums[0]) {
            count++;
        }
        
        // if both checks increment count, it cannot be rotated 
        return count <= 1;
    }
}