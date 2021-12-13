class Solution {
    public int majorityElement(int[] nums) {
        // x holds count, result holds the number
        int x = 0;
        int result = 0;
        
        /*
        enhanced for loop checks if count is 0. 
        if it is, it sets the result to the number to be searched.
        */
    
        for (int num : nums) {
            if (x == 0) {
                result = num;
            } 
            
            if (result == num) {
                x++;
            } else {
                x--;
            }
        }
        
        return result;
    }
}