class Solution {
    public int maxArea(int[] height) {
        int result = Integer.MIN_VALUE;
        
        int leftIdx = 0;
        int rightIdx = height.length - 1;
        
        while (leftIdx < rightIdx) {
            int area = Math.min(height[leftIdx], height[rightIdx]) 
                * (rightIdx - leftIdx);
            
            if (area > result) {
                result = area;
            }
            
            if (height[leftIdx] < height[rightIdx]) {
                leftIdx++;
            } else {
                rightIdx--;
            }
        }
        
        return result;
    }
}