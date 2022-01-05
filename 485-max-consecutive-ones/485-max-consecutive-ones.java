class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        ArrayList<Integer> counts = new ArrayList<>();
        int counter = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                counts.add(counter);
                counter = 0;
            } else {
                counter++;
            }
            
        }
        
        counts.add(counter);
        return Collections.max(counts);

    }
}