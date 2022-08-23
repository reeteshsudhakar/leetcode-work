class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> enumeration = new HashMap<>();
        int[] result = new int[2];
        
        for (int i = 0; i < nums.length; i++) {
            if (enumeration.containsKey(target - nums[i])) {
                result[0] = i;
                result[1] = enumeration.get(target - nums[i]);
            }
            
            enumeration.put(nums[i], i);
        }
        
        return result;
    }
}