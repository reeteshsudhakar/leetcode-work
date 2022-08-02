class Solution {
    public int maxProduct(int[] nums) {
        
        // keeping track of the current product and the maximum result  
        int product = 1;
        int result = Integer.MIN_VALUE;
        
        // iterating forwards through the array 
        for (int i = 0; i < nums.length; i++) {
            product *= nums[i];
            result = Math.max(product, result);
            if (product == 0) {
                product = 1;
            }
        }
        
        // resetting the running product
        product = 1;
        
        // iterating backwards through the array 
        for (int i = nums.length - 1; i >= 0; i--) {
            product *= nums[i];
            result = Math.max(product, result);
            if (product == 0) {
                product = 1;
            }
        }
        
        return result;
    }
}