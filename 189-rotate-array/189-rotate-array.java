class Solution {
    public void rotate(int[] nums, int k) {
        
        if (k % nums.length == 0) {
            return;
        }
        
        Map<Integer, Integer> placementMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            placementMap.put((i + k) % nums.length, nums[i]);
        }
        
        for (Map.Entry<Integer, Integer> entry : placementMap.entrySet()) {
            nums[entry.getKey()] = entry.getValue(); 
        }
    }
}