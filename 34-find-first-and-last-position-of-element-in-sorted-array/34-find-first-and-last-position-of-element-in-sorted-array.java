class Solution {
    public int[] searchRange(int[] nums, int target) {
        if (nums.length == 0) {
            return new int[]{-1,-1};
        }
        
        int start = 0;
        int end = nums.length - 1;
        int first = -1;
        
        while (start <= end) {
            int middle = start + (end - start)/2;
            
            if (nums[middle] == target) {
                first = middle;
                end = middle - 1;
            } else if (nums[middle] > target) {
                end = middle - 1;
            } else {
                start = middle + 1;
            }
        }
        
        start = 0;
        end = nums.length - 1;
        int last = -1;
        
        while (start <= end) {
            int middle = start + (end - start)/2;
            
            if (nums[middle] == target) {
                last = middle;
                start = middle + 1;
            } else if (nums[middle] > target) {
                end = middle - 1;
            } else {
                start = middle + 1;
            }
        }
        return new int[]{first, last};
    }
}