class Solution {
    public int findMin(int[] nums) {
        // if the size is just 1, return that value 
        if (nums.length == 1) {
            return nums[0];
        }
        
        // initializing start and end indices
        int start = 0;
        int end = nums.length - 1;
        
        /*
        if the end is greater than the start, 
        then the array has either not been rotated
        or has been rotated n times, so you can return
        the first value in the array.
        */
        if (nums[end] > nums[start]) {
            return nums[0];
        }
        
        /*
        binary search 
        */
        while (start <= end) {
            // initializing the middle index
            int mid = start + (end - start) / 2;
            
            /* 
            if the middle is greater than the number on its right, 
            then the array isn't increasing and the value on the
            right is the minimum. Return that value.
            */
            if (nums[mid] > nums[mid + 1]) {
                return nums[mid + 1];
            }
            
            /*
            if the middle is less than the number on its left, 
            then the array isn't increasing and the current value 
            at the middle index is the minimum. Return that value.
            */
            if (nums[mid] < nums[mid - 1]) {
                return nums[mid];
            }
            
            /*
            if the middle is greater than the start, then push right, 
            since the sequence is increasing. else, push left. 
            */
            if (nums[mid] > nums[0]) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        
        return Integer.MIN_VALUE;
    }
}