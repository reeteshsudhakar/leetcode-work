class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
        
        Arrays.fill(result, 1);
        
        int curr = 0;
        
        while (curr < result.length) {
            for (int i = 0; i < nums.length; i++) {
                if (curr == i) {
                    continue;
                } else {
                    result[curr] *= nums[i];
                }
            }
            curr++;
        }
        return result;
    }
}

// this solution works, it's just less efficient -> doesn't use the division operator but it does run in O(n^2) time)
