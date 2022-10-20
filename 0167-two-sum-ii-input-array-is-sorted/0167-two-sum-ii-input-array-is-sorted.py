class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        low = 0
        high = len(numbers) - 1
        
        while low < high: 
            temp = numbers[low] + numbers[high]
            
            if temp == target: 
                return [low + 1, high + 1]
            
            if temp < target: 
                low += 1
            else: 
                high -= 1
            
        