class Solution {
    public int missingNumber(int[] nums) {
        int[] result = new int[nums.length + 1];
        result[0] = 1;
        
        for (int i = 0; i < nums.length; i++) {
            result[nums[i]] = nums[i];
        }
        
        for (int i = 0; i < result.length; i++) {
            if (i == 0) {
                if (result[i] != 0) {
                    return 0;
                }
            } else {
                if (i != result[i]) {
                    return i;
                }
            }
        }
        
        return 0;
    }
}