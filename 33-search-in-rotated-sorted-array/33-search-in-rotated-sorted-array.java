class Solution {
    public int search(int[] nums, int target) {
        if (nums.length == 1) {
            return nums[0] == target ? 0 : -1;
        }
        
        int start = 0;
        int end = nums.length - 1;
        
        
        while (start <= end) {
            
            if (nums[start] == target) {
                return start;
            } else if (nums[end] == target) {
                return end;
            }

            int mid = start + (end - start) / 2;
            
            if (nums[mid] == target) {
                return mid;
            }
                        
            if (nums[start] < nums[mid]) {
                if (nums[mid] >= target && nums[start] < target) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            } else {
                if (nums[mid] < target && nums[end] >= target) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
        }
        
        return -1;
    }
}