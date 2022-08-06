class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> numsMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            if (numsMap.containsKey(nums[i])) {
                return true;
            }
            
            numsMap.put(nums[i], 1);
        }
        
        return false;
    }
}