class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0 
        
        low = 0 
        high = len(height) - 1
        
        while low < high: 
            temp = min(height[low], height[high]) * (high - low)
            area = max(area, temp)
            if height[low] < height[high]:
                low += 1
            else: 
                high -= 1
            
        return area 